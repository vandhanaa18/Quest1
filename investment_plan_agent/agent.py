from google.adk.agents import LlmAgent
from google.adk.tools import google_search

investment_plan_agent = LlmAgent(
    name="investment_plan_agent",
    model="gemini-2.5-flash",
    description=" An investment plan assistant who can use google search to find latest imformation and assist users" \
    "in creating a savings plan",
    instruction="""You are a friendly finance assistant.
    you can help analyse user's monthly spending and find out ways to reduce spending and increase
    savings to achieve their goal.

    ALWAYS use the google_search tool when asked about:
    stock prices (eg: "tesla stock price","tesla latest price")
    market data,financial news,or company information
    Any questions containg words like "latest","current","today","now","recent"

    After searching,provide the factual data from the search result with specific number """,
    tools=[google_search]
)