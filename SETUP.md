# Setup Guide

This guide will help you set up your development environment for working with MCP AI Agents and RAG Tutorials.

## 📋 Prerequisites

- **Python 3.10+** (recommended: Python 3.11+)
- **pip 24.0+**
- **Git**
- API keys for the services you want to use

## 🚀 Quick Setup

### 1. Clone the Repository

```bash
git clone https://github.com/majidraza1228/llm-agents-learn.git
cd llm-agents-learn
```

### 2. Create a Virtual Environment

**Using venv (recommended):**
```bash
# Create virtual environment
python -m venv venv

# Activate on macOS/Linux
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```

**Using conda:**
```bash
conda create -n llm-agents python=3.11
conda activate llm-agents
```

### 3. Set Up Environment Variables

```bash
# Copy the example .env file
cp .env.example .env

# Open .env in your favorite editor
nano .env
# or
code .env
```

**Add your API keys:**
```bash
# Required for most projects
OPENAI_API_KEY=sk-...your-key-here

# For GitHub MCP Agent
GITHUB_TOKEN=ghp_...your-token-here

# For Google/Gemini projects
GOOGLE_API_KEY=...your-key-here

# For other services (optional, add as needed)
ANTHROPIC_API_KEY=...
COHERE_API_KEY=...
SERP_API_KEY=...
```

### 4. Install Dependencies

**Option A: Install for specific project**
```bash
# Navigate to project directory
cd mcp_ai_agents/github_mcp_agent

# Install requirements
pip install -r requirements.txt
```

**Option B: Install common dependencies**
```bash
# Install the base dependencies used across most projects
pip install streamlit agno openai anthropic google-generativeai python-dotenv
```

### 5. Run Your First Agent

```bash
# For MCP Agents
cd mcp_ai_agents/github_mcp_agent
streamlit run github_agent.py

# For RAG Tutorials
cd rag_tutorials/local_rag_agent
streamlit run local_rag_agent.py
```

## 🔑 Getting API Keys

### OpenAI
1. Go to [platform.openai.com](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create new secret key
5. Add to `.env` as `OPENAI_API_KEY`

### GitHub Token
1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Generate new token (classic)
3. Select scopes: `repo`, `read:org`
4. Copy token
5. Add to `.env` as `GITHUB_TOKEN`

### Google AI (Gemini)
1. Go to [ai.google.dev](https://ai.google.dev/)
2. Get API key from Google AI Studio
3. Add to `.env` as `GOOGLE_API_KEY`

### Anthropic (Claude)
1. Go to [console.anthropic.com](https://console.anthropic.com/)
2. Get API key
3. Add to `.env` as `ANTHROPIC_API_KEY`

### SerpAPI (Web Search)
1. Go to [serpapi.com](https://serpapi.com/)
2. Sign up for free tier
3. Get API key
4. Add to `.env` as `SERP_API_KEY`

## 📁 Project Structure

```
llm-agents-learn/
├── .env.example          # Template for environment variables
├── .env                  # Your actual keys (NOT committed)
├── .gitignore           # Git ignore rules
├── README.md            # Main documentation
├── SETUP.md             # This file
├── utils/               # Shared utilities
│   ├── __init__.py
│   └── env_loader.py    # Environment variable loader
├── mcp_ai_agents/       # MCP agent projects
│   ├── github_mcp_agent/
│   ├── notion_mcp_agent/
│   └── ...
└── rag_tutorials/       # RAG tutorial projects
    ├── local_rag_agent/
    ├── gemini_agentic_rag/
    └── ...
```

## 🔧 Using Environment Variables in Your Code

### Method 1: Using the env_loader utility

```python
from utils.env_loader import load_env, get_api_key, get_model_config

# Load environment variables
load_env()

# Get API keys
openai_key = get_api_key("OPENAI_API_KEY")
github_token = get_api_key("GITHUB_TOKEN", required=False)

# Get model configuration
config = get_model_config("openai")
# Returns: {'api_key': 'sk-...', 'model': 'gpt-4o'}
```

### Method 2: Using python-dotenv directly

```python
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Access variables
openai_key = os.getenv("OPENAI_API_KEY")
github_token = os.getenv("GITHUB_TOKEN")
```

### Method 3: In Streamlit apps

```python
import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Try to load from environment first
env_api_key = os.getenv("OPENAI_API_KEY", "")

# Provide UI input with environment value as default
api_key = st.text_input(
    "OpenAI API Key",
    value=env_api_key,
    type="password",
    help="Can be set in .env file as OPENAI_API_KEY"
)
```

## 🐳 Docker Setup (Optional)

Some MCP agents use Docker (like GitHub MCP Agent):

```bash
# Install Docker Desktop from docker.com

# Verify installation
docker --version

# Pull required images (for GitHub MCP Agent)
docker pull ghcr.io/github/github-mcp-server
```

## 📊 Testing Your Setup

### Quick Test Script

Create a file `test_setup.py`:

```python
from utils.env_loader import load_env, get_api_key
import sys

# Load environment
load_env(verbose=True)

# Test common API keys
keys_to_test = [
    "OPENAI_API_KEY",
    "GITHUB_TOKEN",
    "GOOGLE_API_KEY",
    "ANTHROPIC_API_KEY",
]

print("\n🔍 Testing API Keys:")
print("-" * 50)

for key in keys_to_test:
    try:
        value = get_api_key(key, required=False)
        if value:
            print(f"✓ {key}: {value[:4]}...{value[-4:]}")
        else:
            print(f"⚠ {key}: Not set")
    except Exception as e:
        print(f"✗ {key}: Error - {e}")

print("-" * 50)
print("\n✓ Setup test complete!")
```

Run it:
```bash
python test_setup.py
```

## 🔒 Security Checklist

- [ ] `.env` file is created and contains your keys
- [ ] `.env` is listed in `.gitignore`
- [ ] `.env` file is NOT committed to git
- [ ] API keys are not hardcoded in any Python files
- [ ] You understand which keys are required for your projects
- [ ] You have rotated any keys that were accidentally exposed

## ❓ Troubleshooting

### "ModuleNotFoundError: No module named 'dotenv'"
```bash
pip install python-dotenv
```

### "API key not found"
1. Check `.env` file exists in repository root
2. Verify key names match exactly (case-sensitive)
3. Ensure no quotes around values in `.env`
4. Restart your Python/Streamlit process

### "Permission denied" with Docker
```bash
# On Linux/Mac, add your user to docker group
sudo usermod -aG docker $USER
# Log out and back in
```

### Environment variables not loading
1. Verify `.env` file location (should be in repository root)
2. Check for typos in variable names
3. Ensure `load_dotenv()` is called before accessing variables
4. Try absolute path: `load_dotenv('/full/path/to/.env')`

## 📚 Next Steps

Once setup is complete:

1. **Explore MCP Agents**: Start with [GitHub MCP Agent](mcp_ai_agents/github_mcp_agent/)
2. **Try RAG Tutorials**: Begin with [Basic RAG Chain](rag_tutorials/rag_chain/)
3. **Read the main [README.md](README.md)** for project overview
4. **Check individual project READMEs** for specific instructions

## 🆘 Getting Help

- Check project-specific READMEs in each folder
- Review error messages carefully
- Ensure all prerequisites are installed
- Verify API keys are valid and have proper permissions

---

**Happy Building! 🚀**
