from google.adk.agents import LlmAgent
from google.adk.tools import google_search

guitar_song_search_agent = LlmAgent(
    name="guitar_song_search_agent",
    model="gemini-2.5-flash",
    description="Finds the Chordie page URL for a song.",

    instruction="""
  Use google_search.

Find the Chordie page URL for the requested song.

Return the exact URL if found.

Example:
https://www.chordie.com/chord.pere/www.azchords.com/e/edsheeran-tabs-34959/perfect-tabs-908387.html

Return only the URL.

If multiple Chordie results exist, prefer URLs containing:
- tabs
- chords
- html

Never say that the song could not be found.
Never provide explanations.
Never provide summaries.
""",

    tools=[google_search]
)