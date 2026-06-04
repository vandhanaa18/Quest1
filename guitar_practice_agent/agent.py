from google.adk.agents import LlmAgent

def get_strumming_pattern(song_name: str):
    """
    Returns strumming pattern.
    """

    patterns = {
        "Shape of You": "D D U U D U",
        "Perfect": "D D U D U"
    }

    return {
        "song": song_name,
        "pattern": patterns.get(
            song_name,
            "D D U U D U"
        )
    }


def generate_practice_plan(song_name: str):
    """
    Generates beginner practice plan.
    """

    return {
        "Day 1": "Learn first two chords",
        "Day 2": "Learn remaining chords",
        "Day 3": "Practice transitions",
        "Day 4": "Practice strumming",
        "Day 5": "Play complete song"
    }


guitar_practice_agent = LlmAgent(
    name="guitar_practice_agent",
    model="gemini-2.0-flash",
    description="Helps users practice guitar songs.",
    instruction="""
    Help users learn songs.

    Use:
    - get_strumming_pattern
    - generate_practice_plan

    whenever users ask about practice.
    """,
    tools=[
        get_strumming_pattern,
        generate_practice_plan
    ]
)