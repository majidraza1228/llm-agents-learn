# LLM Agents Learn

A curated collection of **MCP AI Agents** and **RAG (Retrieval Augmented Generation) Tutorials** to help you learn and build production-ready AI applications.

## 📂 Repository Structure

This repository contains two main sections:

### 🔌 MCP AI Agents

Model Context Protocol (MCP) agents that integrate with various services and tools to create powerful AI assistants.

**What's Inside:**
- **[Browser MCP Agent](mcp_ai_agents/browser_mcp_agent/)** - AI agent that can browse the web and interact with web pages
- **[GitHub MCP Agent](mcp_ai_agents/github_mcp_agent/)** - Manage GitHub repositories, issues, and pull requests using AI
- **[Notion MCP Agent](mcp_ai_agents/notion_mcp_agent/)** - Integrate with Notion to manage notes, databases, and pages
- **[Multi MCP Agent](mcp_ai_agents/multi_mcp_agent/)** - Coordinate multiple MCP servers for complex workflows
- **[AI Travel Planner MCP Agent Team](mcp_ai_agents/ai_travel_planner_mcp_agent_team/)** - Multi-agent system for planning travel itineraries

**Key Features:**
- Production-ready MCP server implementations
- Integration with popular services (GitHub, Notion, Browser automation)
- Multi-agent orchestration examples
- Real-world use cases and applications

### 📚 RAG Tutorials

Comprehensive tutorials covering various RAG (Retrieval Augmented Generation) implementations and techniques.

**What's Inside:**

#### Agentic RAG
- **[Agentic RAG with Embedding Gemma](rag_tutorials/agentic_rag_embedding_gemma/)** - Using Gemma embeddings for intelligent retrieval
- **[Agentic RAG with Reasoning](rag_tutorials/agentic_rag_with_reasoning/)** - Add reasoning capabilities to your RAG pipeline
- **[Agentic RAG Math Agent](rag_tutorials/agentic_rag_math_agent/)** - Specialized RAG for mathematical problem-solving
- **[Agentic RAG GPT-5](rag_tutorials/agentic_rag_gpt5/)** - Advanced RAG implementation with GPT-5

#### Local & Cloud RAG
- **[Local RAG Agent](rag_tutorials/local_rag_agent/)** - Run RAG entirely on your local machine
- **[Llama 3.1 Local RAG](rag_tutorials/llama3.1_local_rag/)** - Local RAG using Llama 3.1
- **[Qwen Local RAG](rag_tutorials/qwen_local_rag/)** - Local RAG with Qwen models
- **[Deepseek Local RAG Agent](rag_tutorials/deepseek_local_rag_agent/)** - Local RAG using Deepseek models
- **[Gemini Agentic RAG](rag_tutorials/gemini_agentic_rag/)** - Cloud-based RAG with Google Gemini

#### Advanced RAG Techniques
- **[Corrective RAG (CRAG)](rag_tutorials/corrective_rag/)** - Self-correcting RAG for improved accuracy
- **[Autonomous RAG](rag_tutorials/autonomous_rag/)** - Fully autonomous retrieval and generation
- **[Hybrid Search RAG](rag_tutorials/hybrid_search_rag/)** - Combine semantic and keyword search
- **[Local Hybrid Search RAG](rag_tutorials/local_hybrid_search_rag/)** - Hybrid search running locally
- **[Vision RAG](rag_tutorials/vision_rag/)** - RAG for images and visual content

#### Specialized RAG Applications
- **[RAG Agent with Cohere](rag_tutorials/rag_agent_cohere/)** - Using Cohere's powerful models
- **[Contextual AI RAG Agent](rag_tutorials/contextualai_rag_agent/)** - Context-aware retrieval
- **[RAG Database Routing](rag_tutorials/rag_database_routing/)** - Route queries to appropriate databases
- **[RAG-as-a-Service](rag_tutorials/rag-as-a-service/)** - Deploy RAG as a scalable service
- **[AI Blog Search](rag_tutorials/ai_blog_search/)** - Search and retrieve blog content
- **[Basic RAG Chain](rag_tutorials/rag_chain/)** - Fundamental RAG implementation

**Key Learning Areas:**
- Vector databases and embeddings
- Semantic vs. hybrid search
- Local vs. cloud deployment
- Agentic retrieval strategies
- Production deployment patterns
- Multi-modal RAG (text + images)

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher (recommended: Python 3.11+)
- pip 24.0 or higher (upgrade with: `pip install --upgrade pip`)
- API keys for cloud-based models (OpenAI, Anthropic, Google, etc.)

### Quick Start

1. **Set up environment variables**

   ```bash
   # Copy the example .env file
   cp .env.example .env

   # Edit .env and add your API keys
   # Never commit the .env file to git!
   ```

   The `.env` file should contain your API keys:
   ```bash
   OPENAI_API_KEY=your_openai_key_here
   GITHUB_TOKEN=your_github_token_here
   GOOGLE_API_KEY=your_google_key_here
   # ... and other keys as needed
   ```

2. **Navigate to a project directory**

   ```bash
   cd mcp_ai_agents/github_mcp_agent
   # or
   cd rag_tutorials/local_rag_agent
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   Most projects use Streamlit:
   ```bash
   streamlit run github_agent.py
   # or
   streamlit run local_rag_agent.py
   ```

5. **Follow project-specific instructions**

   Each project has its own README with detailed setup instructions, configuration steps, and usage examples.

### 🔐 Security Best Practices

- **Never commit `.env` files** - They contain sensitive API keys
- **Use `.env.example`** - Template for required environment variables
- **Rotate API keys regularly** - For enhanced security
- **Use environment-specific files** - `.env.development`, `.env.production`
- **Check `.gitignore`** - Ensures `.env` files are excluded from git

## 🎓 Learning Path

### For Beginners
Start with these foundational projects:
1. [Basic RAG Chain](rag_tutorials/rag_chain/) - Understand core RAG concepts
2. [Local RAG Agent](rag_tutorials/local_rag_agent/) - Build your first RAG application
3. [GitHub MCP Agent](mcp_ai_agents/github_mcp_agent/) - Learn MCP basics

### For Intermediate Developers
Progress to more advanced implementations:
1. [Agentic RAG with Reasoning](rag_tutorials/agentic_rag_with_reasoning/)
2. [Hybrid Search RAG](rag_tutorials/hybrid_search_rag/)
3. [Multi MCP Agent](mcp_ai_agents/multi_mcp_agent/)

### For Advanced Users
Tackle complex architectures:
1. [Corrective RAG](rag_tutorials/corrective_rag/)
2. [AI Travel Planner MCP Agent Team](mcp_ai_agents/ai_travel_planner_mcp_agent_team/)
3. [RAG-as-a-Service](rag_tutorials/rag-as-a-service/)

## 🛠️ Technologies Used

- **LLM Providers:** OpenAI, Anthropic (Claude), Google (Gemini), Cohere, Local models (Llama, Qwen, Deepseek)
- **Frameworks:** LangChain, LlamaIndex, OpenAI SDK, Anthropic SDK
- **Vector Databases:** ChromaDB, Pinecone, Weaviate, FAISS
- **MCP Servers:** Official MCP implementations, custom servers
- **Tools:** Python, Streamlit, FastAPI, Docker

## 📖 Documentation

Each project includes:
- Detailed README with setup instructions
- Code comments and explanations
- Example use cases
- Configuration options
- Troubleshooting guide

## 🤝 Contributing

Contributions are welcome! If you have:
- Bug fixes
- New RAG techniques
- Additional MCP agent implementations
- Documentation improvements

Please feel free to open an issue or submit a pull request.

## 📝 License

This repository follows the same license as the original awesome-llm-apps repository.

## 🙏 Acknowledgments

This collection is built upon the excellent work from the broader LLM and AI community. Special thanks to all contributors who have shared their knowledge and implementations.

## 🔗 Related Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Anthropic Claude Documentation](https://docs.anthropic.com/)
- [LangChain Documentation](https://docs.langchain.com/)

---

**Happy Learning! 🚀**

Start building powerful AI applications with MCP agents and RAG today.
