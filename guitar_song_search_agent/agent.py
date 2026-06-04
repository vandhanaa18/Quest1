from google.adk.agents import LlmAgent
from google.adk.tools import google_search

guitar_song_search_agent = LlmAgent(
    name="guitar_song_search_agent",
    model="gemini-2.0-flash",
    description="Searches the web for guitar song chords.",

    instruction="""
    ALWAYS use google_search when users ask:

    - learn a song
    - guitar chords
    - chord progression
    - song chords

    After searching:

1. Give only:
   - song chords
   - chord progression

2. Do NOT provide:
   - chord fingering
   - strumming pattern
   - practice plans

3. Ask the user what they want next:
   - chord fingering
   - strumming pattern
   - practice plan

Keep the response concise.

    """,

    tools=[google_search]
)