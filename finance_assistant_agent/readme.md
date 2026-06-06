 Finance Assistant Agent

 About the Project

This is a Finance Assistant Agent built using Google ADK and Gemini 2.5 Flash.

The agent helps users with:

* Spending analysis
* Savings planning
* Financial goal planning
* Investment-related queries
* Latest financial information using Google Search

 Tools Used

* Google ADK
* Gemini 2.5 Flash
* Google Search Tool
* Custom Finance Tool (`get_user_personal_finance_details`)


 How to Run

1. Create and activate virtual environment

python -m venv .venv
.venv\Scripts\Activate.ps1


2. Install dependencies


pip install -r requirements.txt


3. Add your API key in `.env`

GOOGLE_API_KEY=YOUR_API_KEY


4. Start the agent
adk web

5. Open:

* Gemini acts as the reasoning engine.
* The agent uses tool calling to retrieve information.
* Google Search is used for current financial information.
* The finance tool provides user financial details for analysis and planning.
