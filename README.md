# AI-AGENT

A multi-agent AI system built with LangGraph that combines research and content generation capabilities.

## Features

- **Researcher Agent**: Searches the web for information about any topic using DuckDuckGo
- **Writer Agent**: Generates comprehensive blog posts based on research findings
- **LangGraph Integration**: Uses LangGraph for orchestrating agent workflows
- **State Management**: Shared state for seamless data flow between agents

## Architecture

```
Start → Researcher Agent → Writer Agent → End
         (searches web)    (writes blog)
```

The system uses a shared `AgentState` that passes research data from the researcher to the writer, demonstrating multi-agent collaboration.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/thukralhanshika3-glitch/AI-AGENT.git
cd AI-AGENT
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the agent system:

```bash
python INDEX.PY
```

To change the research topic, edit the `inputs` dictionary in `INDEX.PY`:

```python
inputs: AgentState = {
    "topic": "Your topic here",
    "research_data": [],
    "blog_post": "",
}
```

## Example Output

The system generates:
1. Research findings from web search
2. A structured blog post with:
   - Title and introduction
   - Comprehensive content based on research
   - Key insights section
   - Conclusion

## Dependencies

- `langgraph`: Agent workflow orchestration
- `langchain`: LLM framework
- `ddgs`: DuckDuckGo search integration

## License

MIT

## Author

Built with LangGraph and LangChain for multi-agent AI systems
