from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from guitar_learning_agent.tools.chords_tool import get_song_chords
from guitar_learning_agent.tools.fingering_tool import get_chord_fingering

from guitar_learning_agent.guitar_practice_agent.agent import guitar_practice_agent
from guitar_learning_agent.guitar_song_search_agent.agent import guitar_song_search_agent


guitar_learning_agent = LlmAgent(
    name="guitar_learning_agent",
    model="gemini-2.5-flash",
    description="A guitar learning assistant.",

    instruction="""
    You are a friendly guitar learning assistant.

    You help users:

    - Learn songs
    - Find guitar chords
    - Learn chord fingerings
    - Get strumming patterns
    - Create practice plans

    Use guitar_song_search_agent whenever users ask:

    - learn a song
    - guitar chords
    - chord progression
    - song chords

    Use get_chord_fingering whenever users ask:

    - how to play a chord
    - chord fingering
    - finger placement

    Use guitar_practice_agent whenever users ask:

    - practice plans
    - strumming patterns
    - song practice schedules

    Always provide beginner-friendly explanations.
    When get_song_chords returns chords, ALWAYS display only the chords returned by the tool.
    Never generate your own chord progression.
    Never guess chords.
    """,

    tools=[
        get_song_chords,
        get_chord_fingering,
        AgentTool(guitar_practice_agent),
        AgentTool(guitar_song_search_agent)
    ]
)

root_agent = guitar_learning_agent