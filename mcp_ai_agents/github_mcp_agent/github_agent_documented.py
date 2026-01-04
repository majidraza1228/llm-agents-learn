"""
GitHub MCP Agent - A Streamlit application for interacting with GitHub repositories using AI

This application uses the Model Context Protocol (MCP) to enable natural language queries
about GitHub repositories. It combines the GitHub MCP server with an AI agent powered by
OpenAI to provide intelligent insights about issues, pull requests, and repository activity.

Architecture:
    - Frontend: Streamlit web interface
    - MCP Server: GitHub's official MCP server (runs in Docker)
    - AI Agent: Agno framework with OpenAI GPT models
    - Communication: Async operations with MCP protocol over stdio
"""

# ============================================================================
# IMPORTS
# ============================================================================

import asyncio  # Async/await support for non-blocking operations with MCP server
import os  # Operating system interface for environment variables
import streamlit as st  # Web framework for building the UI
from textwrap import dedent  # Utility to clean up multi-line strings (for agent instructions)
from agno.agent import Agent  # Agno's Agent class for creating AI agents
from agno.run.agent import RunOutput  # Type hint for agent execution results
from agno.tools.mcp import MCPTools  # MCP integration for Agno agents
from mcp import StdioServerParameters  # Configuration for MCP server communication via stdio

# ============================================================================
# STREAMLIT PAGE CONFIGURATION
# ============================================================================

# Configure the Streamlit page settings (must be the first Streamlit command)
st.set_page_config(
    page_title="🐙 GitHub MCP Agent",  # Browser tab title
    page_icon="🐙",  # Browser tab icon (octopus for GitHub)
    layout="wide"  # Use full width of the browser
)

# ============================================================================
# HEADER SECTION
# ============================================================================

# Display the main page header with custom HTML styling
st.markdown(
    "<h1 class='main-header'>🐙 GitHub MCP Agent</h1>",
    unsafe_allow_html=True  # Allow HTML rendering for custom styling
)

# Display subtitle explaining the app's purpose
st.markdown("Explore GitHub repositories with natural language using the Model Context Protocol")

# ============================================================================
# SIDEBAR - AUTHENTICATION & HELP
# ============================================================================

with st.sidebar:  # Create a sidebar for authentication and example queries
    # Section header for authentication inputs
    st.header("🔑 Authentication")

    # OpenAI API Key input field
    openai_key = st.text_input(
        "OpenAI API Key",  # Label displayed above the input field
        type="password",  # Hide the input characters for security
        help="Required for the AI agent to interpret queries and format results"  # Tooltip text
    )
    # If user provided an OpenAI key, store it in environment variables
    if openai_key:
        os.environ["OPENAI_API_KEY"] = openai_key

    # GitHub Personal Access Token input field
    github_token = st.text_input(
        "GitHub Token",  # Label displayed above the input field
        type="password",  # Hide the token for security
        help="Create a token with repo scope at github.com/settings/tokens"  # Instructions tooltip
    )
    # If user provided a GitHub token, store it in environment variables
    if github_token:
        os.environ["GITHUB_TOKEN"] = github_token

    # Horizontal divider line in the sidebar
    st.markdown("---")

    # Display example queries section
    st.markdown("### Example Queries")

    # Issues-related example queries
    st.markdown("**Issues**")
    st.markdown("- Show me issues by label")  # Example: filter issues by specific labels
    st.markdown("- What issues are being actively discussed?")  # Example: find active discussions

    # Pull Requests-related example queries
    st.markdown("**Pull Requests**")
    st.markdown("- What PRs need review?")  # Example: find PRs awaiting review
    st.markdown("- Show me recent merged PRs")  # Example: see recently merged changes

    # Repository-level example queries
    st.markdown("**Repository**")
    st.markdown("- Show repository health metrics")  # Example: overall repo statistics
    st.markdown("- Show repository activity patterns")  # Example: analyze commit/PR patterns

    # Another horizontal divider
    st.markdown("---")

    # Reminder note for users
    st.caption("Note: Always specify the repository in your query if not already selected in the main input.")

# ============================================================================
# MAIN INTERFACE - REPOSITORY & QUERY TYPE SELECTION
# ============================================================================

# Create two columns with 3:1 width ratio
col1, col2 = st.columns([3, 1])

# Left column (wider) - Repository input
with col1:
    repo = st.text_input(
        "Repository",  # Label for the input field
        value="Shubhamsaboo/awesome-llm-apps",  # Default repository to analyze
        help="Format: owner/repo"  # Tooltip explaining the required format
    )

# Right column (narrower) - Query type selection
with col2:
    query_type = st.selectbox(
        "Query Type",  # Label for the dropdown
        [
            "Issues",  # Pre-configured query about repository issues
            "Pull Requests",  # Pre-configured query about PRs
            "Repository Activity",  # Pre-configured query about repo activity
            "Custom"  # User writes their own custom query
        ]
    )

# ============================================================================
# QUERY TEMPLATE GENERATION
# ============================================================================

# Generate pre-filled query text based on selected query type
if query_type == "Issues":
    # Template for finding bug issues in the repository
    query_template = f"Find issues labeled as bugs in {repo}"
elif query_type == "Pull Requests":
    # Template for finding recently merged pull requests
    query_template = f"Show me recent merged PRs in {repo}"
elif query_type == "Repository Activity":
    # Template for analyzing code quality trends
    query_template = f"Analyze code quality trends in {repo}"
else:
    # Empty template for custom queries (user types from scratch)
    query_template = ""

# Text area for user to enter or modify their query
query = st.text_area(
    "Your Query",  # Label for the text area
    value=query_template,  # Pre-fill with the template (if not custom)
    placeholder="What would you like to know about this repository?"  # Placeholder text
)

# ============================================================================
# ASYNC FUNCTION - GITHUB AGENT EXECUTION
# ============================================================================

async def run_github_agent(message):
    """
    Execute the GitHub agent with the user's query.

    This function:
    1. Validates that required API keys are present
    2. Configures the GitHub MCP server to run in Docker
    3. Creates an AI agent with MCP tools for GitHub API access
    4. Executes the user's query and returns formatted results

    Args:
        message (str): The user's natural language query about a GitHub repository

    Returns:
        str: Formatted markdown response with GitHub data and insights
             OR error message if something went wrong

    Architecture Flow:
        User Query → AI Agent → MCP Server (Docker) → GitHub API → Response
    """

    # Validate GitHub token is present
    if not os.getenv("GITHUB_TOKEN"):
        return "Error: GitHub token not provided"

    # Validate OpenAI API key is present
    if not os.getenv("OPENAI_API_KEY"):
        return "Error: OpenAI API key not provided"

    try:
        # ========================================================================
        # MCP SERVER CONFIGURATION
        # ========================================================================

        # Configure parameters for the GitHub MCP server
        # This server runs in a Docker container and communicates via stdio
        server_params = StdioServerParameters(
            command="docker",  # Use Docker to run the MCP server
            args=[
                "run",  # Docker run command
                "-i",  # Interactive mode (keep STDIN open)
                "--rm",  # Remove container after it exits
                "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",  # Pass GitHub token as env var
                "-e", "GITHUB_TOOLSETS",  # Pass toolsets configuration as env var
                "ghcr.io/github/github-mcp-server"  # Official GitHub MCP server image
            ],
            env={
                **os.environ,  # Include all current environment variables
                "GITHUB_PERSONAL_ACCESS_TOKEN": os.getenv('GITHUB_TOKEN'),  # GitHub auth token
                "GITHUB_TOOLSETS": "repos,issues,pull_requests"  # Enable specific GitHub API toolsets
            }
        )

        # ========================================================================
        # MCP TOOLS CONTEXT MANAGER
        # ========================================================================

        # Create an async context manager for MCP tools
        # This handles connection lifecycle (connect, use, disconnect)
        async with MCPTools(server_params=server_params) as mcp_tools:

            # ====================================================================
            # AGENT CREATION
            # ====================================================================

            # Create an AI agent with access to GitHub MCP tools
            agent = Agent(
                tools=[mcp_tools],  # Provide MCP tools for GitHub API access
                instructions=dedent("""\
                    You are a GitHub assistant. Help users explore repositories and their activity.
                    - Provide organized, concise insights about the repository
                    - Focus on facts and data from the GitHub API
                    - Use markdown formatting for better readability
                    - Present numerical data in tables when appropriate
                    - Include links to relevant GitHub pages when helpful
                """),  # System instructions defining the agent's behavior
                markdown=True,  # Enable markdown formatting in responses
            )

            # ====================================================================
            # QUERY EXECUTION
            # ====================================================================

            # Execute the agent asynchronously with a 120-second timeout
            # agent.arun() runs the agent with the user's message
            # asyncio.wait_for() adds a timeout to prevent hanging
            response: RunOutput = await asyncio.wait_for(
                agent.arun(message),  # Run the agent with the user's query
                timeout=120.0  # Maximum 2 minutes for execution
            )

            # Return the agent's response content (markdown formatted)
            return response.content

    except asyncio.TimeoutError:
        # Handle case where agent execution takes longer than 120 seconds
        return "Error: Request timed out after 120 seconds"

    except Exception as e:
        # Catch all other exceptions and return error message
        return f"Error: {str(e)}"

# ============================================================================
# QUERY EXECUTION BUTTON & RESULTS DISPLAY
# ============================================================================

# Create a primary action button to execute the query
if st.button("🚀 Run Query", type="primary", use_container_width=True):

    # Validation: Check if OpenAI API key is provided
    if not openai_key:
        st.error("Please enter your OpenAI API key in the sidebar")

    # Validation: Check if GitHub token is provided
    elif not github_token:
        st.error("Please enter your GitHub token in the sidebar")

    # Validation: Check if user entered a query
    elif not query:
        st.error("Please enter a query")

    # All validations passed - execute the agent
    else:
        # Display a spinner while the agent processes the query
        with st.spinner("Analyzing GitHub repository..."):

            # If repository is specified and not already in the query, append it
            if repo and repo not in query:
                full_query = f"{query} in {repo}"  # Add repository context
            else:
                full_query = query  # Use query as-is

            # Run the async agent function synchronously using asyncio.run()
            # This blocks until the agent completes or times out
            result = asyncio.run(run_github_agent(full_query))

        # Display results section header
        st.markdown("### Results")

        # Display the agent's response as markdown
        st.markdown(result)

# ============================================================================
# HELP SECTION - DISPLAYED WHEN NO RESULTS YET
# ============================================================================

# Check if 'result' variable exists in local scope (i.e., query was executed)
if 'result' not in locals():
    # If no query has been run yet, display help information
    st.markdown(
        """<div class='info-box'>
        <h4>How to use this app:</h4>
        <ol>
            <li>Enter your <strong>OpenAI API key</strong> in the sidebar (powers the AI agent)</li>
            <li>Enter your <strong>GitHub token</strong> in the sidebar</li>
            <li>Specify a repository (e.g., Shubhamsaboo/awesome-llm-apps)</li>
            <li>Select a query type or write your own</li>
            <li>Click 'Run Query' to see results</li>
        </ol>
        <p><strong>How it works:</strong></p>
        <ul>
            <li>Uses the official GitHub MCP server via Docker for real-time access to GitHub API</li>
            <li>AI Agent (powered by OpenAI) interprets your queries and calls appropriate GitHub APIs</li>
            <li>Results are formatted in readable markdown with insights and links</li>
            <li>Queries work best when focused on specific aspects like issues, PRs, or repository info</li>
        </ul>
        </div>""",
        unsafe_allow_html=True  # Allow HTML rendering for styled help box
    )
