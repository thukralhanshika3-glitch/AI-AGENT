from typing import TypedDict, List
from langgraph.graph import StateGraph, END

# ----- Shared State -----
class AgentState(TypedDict):
    topic: str
    research_data: List[str]  # A list of findings
    blog_post: str   

from langchain_community.tools.ddg_search import DuckDuckGoSearchRun

def researcher_node(state: AgentState):
    topic = state["topic"]
    print(f"Researcher is looking up: {topic}...")
    
    search = DuckDuckGoSearchRun()
    
    try:
        # You can tweak this query as you like
        results = search.run(f"key facts and latest news about {topic}")
    except Exception as e:
        results = f"Could not find data: {e}"
        
    print("Research complete.")
    
    # Only return the keys you want to update
    return {"research_data": state.get("research_data", []) + [results]}

    # Using a simple mock writer for demonstration
from langchain_core.prompts import ChatPromptTemplate

def writer_node(state: AgentState):
    print("Writer is drafting the post...")
    
    topic = state["topic"]
    data = state["research_data"][-1] if state["research_data"] else ""
    
    # Generate a mock blog post
    blog_post = f"""# {topic}

Based on the research findings, here's what we learned:

{data}

## Key Insights

The topic has been thoroughly researched and analyzed. The key findings indicate that:

1. There are significant developments happening in this space
2. The trends show continuous evolution and improvement
3. Industry experts are actively engaged in advancing this field
4. The future outlook is promising with many opportunities

## Conclusion

The research data collected provides strong evidence that this area will continue to grow and develop. 
Understanding these fundamentals will help navigate the landscape effectively.

This exploration demonstrates the importance of staying informed and adapting to changes in this dynamic field."""
    
    print("Writing complete.")
    return {"blog_post": blog_post}

    # ----- Build the LangGraph -----
workflow = StateGraph(AgentState)

workflow.add_node("Researcher", researcher_node)
workflow.add_node("Writer", writer_node)

# Flow: Start -> Researcher -> Writer -> END
workflow.set_entry_point("Researcher")
workflow.add_edge("Researcher", "Writer")
workflow.add_edge("Writer", END)

app = workflow.compile()
if __name__ == "__main__":
    print("Starting the Multi-Agent System...\n")
    
    inputs: AgentState = {
        "topic": "AI LIFECYCLE",
        "research_data": [],
        "blog_post": "",
    }
    
    result = app.invoke(inputs)
    
    print("\n---------------- FINAL OUTPUT ----------------\n")
    print(result["blog_post"])
