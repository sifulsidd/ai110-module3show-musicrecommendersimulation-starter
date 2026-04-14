from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    # ADDED: instrumentalness, speechiness, popularity — three new numerical
    # features that capture vocal presence, lyric density, and mainstream
    # appeal, giving the recommender more dimensions to score against.
    id: int = 0
    title: str = ""
    artist: str = ""
    genre: str = ""
    mood: str = ""
    energy: float = 0.5
    tempo_bpm: float = 100.0
    valence: float = 0.5
    danceability: float = 0.5
    acousticness: float = 0.5
    instrumentalness: float = 0.0  # 0=vocals present, 1=fully instrumental
    speechiness: float = 0.0       # 0=melodic, 1=spoken word / rap-heavy
    popularity: float = 0.5        # 0=niche, 1=mainstream chart hit

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    # ADDED: target_valence, target_danceability, target_tempo_bpm fill the
    # gap between Song's numerical fields and UserProfile's scoring targets —
    # every float on Song now has a corresponding preference to score against.
    favorite_genre: str = ""
    favorite_mood: str = ""
    target_energy: float = 0.5
    likes_acoustic: bool = False
    target_instrumentalness: float = 0.0   # how much the user prefers instrumental music
    target_speechiness: float = 0.05       # tolerance for rap/spoken word content
    target_popularity: float = 0.5         # 0=prefers niche discoveries, 1=prefers hits
    target_valence: float = 0.5            # preferred emotional positivity (0=sad, 1=happy)
    target_danceability: float = 0.5       # preferred rhythmic drive (0=still, 1=dancefloor)
    target_tempo_bpm: float = 100.0        # preferred beats per minute

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id":               int(row["id"]),
                "title":            row["title"],
                "artist":           row["artist"],
                "genre":            row["genre"],
                "mood":             row["mood"],
                "energy":           float(row["energy"]),
                "tempo_bpm":        float(row["tempo_bpm"]),
                "valence":          float(row["valence"]),
                "danceability":     float(row["danceability"]),
                "acousticness":     float(row["acousticness"]),
                "instrumentalness": float(row["instrumentalness"]),
                "speechiness":      float(row["speechiness"]),
                "popularity":       float(row["popularity"]),
            })
    return songs



def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, str]:
    """
    Scores a single song against a user preference dict.

    Scoring recipe:
      +2.0  flat bonus — genre match
      +1.5  flat bonus — mood match
      +1.0  flat bonus — both user and song are acoustic (acousticness >= 0.6)
      +0–1.5  energy similarity:        (1 - |song - user|) * 1.5
      +0–1.0  valence similarity:       (1 - |song - user|) * 1.0
      +0–1.0  danceability similarity:  (1 - |song - user|) * 1.0
      +0–0.75 tempo similarity:         (1 - |song - user| / 110) * 0.75  (normalized over 110 BPM range)
      +0–0.5  instrumentalness similarity: (1 - |song - user|) * 0.5
      +0–0.5  speechiness similarity:   (1 - |song - user|) * 0.5
      +0–0.25 popularity similarity:    (1 - |song - user|) * 0.25
      ─────────────────────────────────
      Maximum possible score: 10.0

    Returns a (score, explanation) tuple.
    """
    score = 0.0
    reasons = []

    # --- Flat match bonuses ---
    if song["genre"] == user_prefs.get("genre", ""):
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] == user_prefs.get("mood", ""):
        score += 1.5
        reasons.append("mood match (+1.5)")

    if user_prefs.get("acousticness", 0.5) >= 0.6 and song["acousticness"] >= 0.6:
        score += 1.0
        reasons.append("acoustic preference match (+1.0)")

    # --- Similarity points ---
    # Formula: (1 - |song_value - user_target|) * max_points
    # Produces a value between 0 and max_points — closer = more points.
    energy_pts = (1 - abs(song["energy"] - user_prefs.get("energy", 0.5))) * 1.5
    score += energy_pts
    reasons.append(f"energy similarity (+{energy_pts:.2f})")

    valence_pts = (1 - abs(song["valence"] - user_prefs.get("valence", 0.5))) * 1.0
    score += valence_pts
    reasons.append(f"valence similarity (+{valence_pts:.2f})")

    dance_pts = (1 - abs(song["danceability"] - user_prefs.get("danceability", 0.5))) * 1.0
    score += dance_pts
    reasons.append(f"danceability similarity (+{dance_pts:.2f})")

    # Tempo is normalized by 110 (the BPM range in this dataset: ~58–168)
    # to keep it on the same 0–1 scale as the other features.
    tempo_pts = max(0.0, 1 - abs(song["tempo_bpm"] - user_prefs.get("tempo_bpm", 100.0)) / 110) * 0.75
    score += tempo_pts
    reasons.append(f"tempo similarity (+{tempo_pts:.2f})")

    instr_pts = (1 - abs(song["instrumentalness"] - user_prefs.get("instrumentalness", 0.0))) * 0.5
    score += instr_pts
    reasons.append(f"instrumentalness similarity (+{instr_pts:.2f})")

    speech_pts = (1 - abs(song["speechiness"] - user_prefs.get("speechiness", 0.05))) * 0.5
    score += speech_pts
    reasons.append(f"speechiness similarity (+{speech_pts:.2f})")

    pop_pts = (1 - abs(song["popularity"] - user_prefs.get("popularity", 0.5))) * 0.25
    score += pop_pts
    reasons.append(f"popularity similarity (+{pop_pts:.2f})")

    return score, ", ".join(reasons)


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = []
    for song in songs:
        score, explanation = score_song(user_prefs, song)
        scored.append((song, score, explanation))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
