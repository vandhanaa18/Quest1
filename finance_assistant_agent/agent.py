from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from typing import Dict
from google.adk.tools.agent_tool import AgentTool
from investment_plan_agent.agent import investment_plan_agent
def get_user_personal_finance_details() -> Dict:
    """
       gets users personal finance details like salary,expense and saving capacity.
    """
    return{
        "salary":50000,
        "expense":40000,
        "savings":10000
    }


finance_assistance_agent = LlmAgent(
    name="finance_assistance_agent",
    model="gemini-2.5-flash",
    description="A simple finance assistant that helps with user's finance goals.",
    instruction="""You are a friendly finance assistant.
        You can help answer user's generic questions on finance and help plan their finance goals.Be more friendly and positive.
        you have two tools to use and complete your task.
        1. get_user_personal_finance_details - this tool will give you the user's current financial detail
        2. investment_plan_agent - this tool can perform google search to get any latest information from website and will be able to ask more details from user and plan their saving goal.
         ALWAYS use the investment_plan_agent with google_search tool when asked about:
    stock prices (eg: "tesla stock price","tesla latest price")
    market data,financial news,or company information
    Any questions containg words like "latest","current","today","now","recent""",
    tools=[AgentTool(investment_plan_agent),get_user_personal_finance_details] 
)

root_agent = finance_assistance_agent