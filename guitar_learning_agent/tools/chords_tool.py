import requests

def get_song_chords(song_name: str):
    """
    Searches online for guitar chords.
    """

    query = song_name.replace(" ", "+")

    url = f"https://www.ultimate-guitar.com/search.php?search_type=title&value={query}"

    try:
        requests.get(url)

        return {
            "song": song_name,
            "status": "Chord search completed",
            "url": url
        }

    except Exception as e:
        return {
            "error": str(e)
        }