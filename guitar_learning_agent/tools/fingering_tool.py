from guitar_learning_agent.data.chord_patterns import CHORD_PATTERNS

def get_chord_fingering(chord: str):
    """
    Returns fingering pattern for a chord.
    """

    pattern = CHORD_PATTERNS.get(chord)

    if pattern:
        return {
            "chord": chord,
            "fingering": pattern
        }

    return {
        "message": f"No fingering found for {chord}"
    }