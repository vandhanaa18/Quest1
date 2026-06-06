import requests
from bs4 import BeautifulSoup
import re


def get_song_chords(song_url: str):

    try:
        response = requests.get(
            song_url,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        soup = BeautifulSoup(response.text, "html.parser")

        text = soup.get_text()

        chords = re.findall(r'\[([^\]]+)\]', text)

        unique_chords = []

        for chord in chords:

            if (
                "verse" in chord.lower()
                or "chorus" in chord.lower()
                or "cborus" in chord.lower()
                or "solo" in chord.lower()
                or "pre-" in chord.lower()
                or "fill" in chord.lower()
                or "interlude" in chord.lower()
            ):
                continue

            chord = chord.strip("()")

            if chord not in unique_chords:
                unique_chords.append(chord)

        return {
            "source": "BeautifulSoup",
            "number_of_chords": len(unique_chords),
            "url_used": song_url,
            "chords": unique_chords
        }

    except Exception as e:
        return {
            "url_used": song_url,
            "error": str(e)
        }