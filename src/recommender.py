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
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float
    instrumentalness: float   # 0=vocals present, 1=fully instrumental
    speechiness: float        # 0=melodic, 1=spoken word / rap-heavy
    popularity: float         # 0=niche, 1=mainstream chart hit

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    # ADDED: target_valence, target_danceability, target_tempo_bpm fill the
    # gap between Song's numerical fields and UserProfile's scoring targets —
    # every float on Song now has a corresponding preference to score against.
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool
    target_instrumentalness: float   # how much the user prefers instrumental music
    target_speechiness: float        # tolerance for rap/spoken word content
    target_popularity: float         # 0=prefers niche discoveries, 1=prefers hits
    target_valence: float            # preferred emotional positivity (0=sad, 1=happy)
    target_danceability: float       # preferred rhythmic drive (0=still, 1=dancefloor)
    target_tempo_bpm: float          # preferred beats per minute

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
    # TODO: Implement CSV loading logic
    print(f"Loading songs from {csv_path}...")
    return []

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    return []
