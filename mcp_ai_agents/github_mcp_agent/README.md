# 🐙 GitHub MCP Agent

### 🎓 FREE Step-by-Step Tutorial 
**👉 [Click here to follow our complete step-by-step tutorial](https://www.theunwindai.com/p/build-an-mcp-github-agent-in-less-than-50-lines-of-code) and learn how to build this from scratch with detailed code walkthroughs, explanations, and best practices.**

A Streamlit application that allows you to explore and analyze GitHub repositories using natural language queries through the Model Context Protocol (MCP).

**✨ Now using the official [GitHub MCP Server](https://github.com/github/github-mcp-server) from GitHub!**

## Features

- **Natural Language Interface**: Ask questions about repositories in plain English
- **Comprehensive Analysis**: Explore issues, pull requests, repository activity, and code statistics
- **Interactive UI**: User-friendly interface with example queries and custom input
- **MCP Integration**: Leverages the Model Context Protocol to interact with GitHub's API
- **Real-time Results**: Get immediate insights on repository activity and health

## Setup

### Requirements

- **Python 3.10+** (Required - MCP SDK requires Python 3.10 or higher)
- **Docker** (for official GitHub MCP server)
  - Download and install from [docker.com](https://www.docker.com/get-started)
  - Make sure Docker is running before starting the app
- **OpenAI API Key**
- **GitHub Personal Access Token**

### Installation

#### Step 1: Install Python 3.10 or Higher

Choose one of the following methods:

**Option A: Using Homebrew (Recommended for macOS)**
```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3.10 or higher
brew install python@3.10

# Verify installation
python3.10 --version
```

**Option B: Using pyenv (For managing multiple Python versions)**
```bash
# Install pyenv
brew install pyenv

# Add to your ~/.zshrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# Reload shell
source ~/.zshrc

# Install Python 3.10 or higher
pyenv install 3.10.17
pyenv global 3.10.17

# Verify
python --version
```

**Option C: Download from Python.org**
1. Visit [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.10 or higher for macOS
3. Run the installer package
4. Verify with `python3.10 --version`

#### Step 2: Clone the Repository

```bash
git clone https://github.com/majidraza1228/llm-agents-learn.git
cd llm-agents-learn/mcp_ai_agents/github_mcp_agent
```

#### Step 3: Set Up Python Virtual Environment

```bash
# Create a virtual environment (recommended)
python3.10 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Step 4: Configure Environment Variables

Create or edit the `.env` file with your API keys:

```bash
# Edit .env file
nano .env
# or use your preferred editor
code .env
```

Add your keys to the `.env` file:
```env
# OpenAI API Key - Required for the AI agent
OPENAI_API_KEY=your_actual_openai_api_key_here

# GitHub Personal Access Token - Required for GitHub operations
# Get it from: https://github.com/settings/tokens
# Required scopes: repo, read:user, read:org
GITHUB_TOKEN=your_actual_github_personal_access_token_here
```

**Get your API keys:**
- **OpenAI API Key**: Get from [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- **GitHub Token**:
  1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
  2. Click "Generate new token (classic)"
  3. Select scopes: `repo`, `read:user`, `read:org`
  4. Copy the token and paste it in the `.env` file

#### Step 5: Verify Docker Installation

```bash
# Check Docker version
docker --version

# Verify Docker is running
docker ps
```

If Docker is not installed, download it from [docker.com](https://www.docker.com/get-started).

### Running the App

#### Method 1: Using Python Directly

```bash
# Navigate to the project directory
cd /path/to/llm-agents-learn/mcp_ai_agents/github_mcp_agent

# Activate virtual environment (if not already activated)
source venv/bin/activate

# Run the app
python3.10 -m streamlit run github_agent.py
```

The app will open in your browser at **http://localhost:8501**

#### Method 2: Using the Alias (Optional)

Add this to your `~/.zshrc` for easy access:

```bash
# Add alias to ~/.zshrc
echo 'alias github-agent="cd /path/to/llm-agents-learn/mcp_ai_agents/github_mcp_agent && source venv/bin/activate && streamlit run github_agent.py"' >> ~/.zshrc

# Reload shell
source ~/.zshrc

# Now run from anywhere with:
github-agent
```

### Using the App

1. Open your browser to **http://localhost:8501**
2. In the app interface:
   - Enter your OpenAI API key (or it will use the one from `.env`)
   - Enter your GitHub token (or it will use the one from `.env`)
   - Specify a repository to analyze
   - Select a query type or write your own
   - Click "Run Query"

### Stopping the App

Press `Ctrl + C` in the terminal where the app is running, or:

```bash
pkill -f streamlit
```

### Troubleshooting

**If you get "command not found: streamlit":**
```bash
pip install streamlit
```

**If you get module errors:**
```bash
pip install -r requirements.txt --upgrade
```

**If you get Python version errors:**
Make sure you're using Python 3.10 or higher:
```bash
python3.10 --version
```

**To check which Python you're using:**
```bash
which python3
python3 --version
```

### Example Queries

#### Issues
- "Show me issues by label"
- "What issues are being actively discussed?"
- "Find issues labeled as bugs"

#### Pull Requests
- "What PRs need review?"
- "Show me recent merged PRs"
- "Find PRs with conflicts"

#### Repository
- "Show repository health metrics"
- "Show repository activity patterns"
- "Analyze code quality trends"
