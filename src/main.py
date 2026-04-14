"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs, UserProfile


def main() -> None:

    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # --- User Preference Profiles ---

    # Persona 1 — "Jordan": gym-goer who wants maximum energy and danceability.
    # Loves mainstream pop anthems with bright, happy vibes and fast tempos.
    high_energy_pop = {
        "genre":            "pop",
        "mood":             "happy",
        "energy":           0.92,       # very high intensity
        "valence":          0.85,       # upbeat and positive
        "danceability":     0.90,       # made for movement
        "tempo_bpm":        128,        # classic dance/EDM tempo
        "acousticness":     0.10,       # prefers produced electronic sound
        "instrumentalness": 0.05,       # wants vocals front and center
        "speechiness":      0.08,       # melodic, not rap-heavy
        "popularity":       0.85,       # loves chart hits
    }

    # Persona 2 — "Sam": late-night student who studies to mellow background music.
    # Drawn to instrumental, acoustic textures at a slow, unhurried pace.
    chill_lofi = {
        "genre":            "lofi",
        "mood":             "chill",
        "energy":           0.30,       # low intensity, background-friendly
        "valence":          0.55,       # gently positive, not euphoric
        "danceability":     0.45,       # some groove, not a dancefloor vibe
        "tempo_bpm":        78,         # slow and relaxed
        "acousticness":     0.80,       # organic, warm textures
        "instrumentalness": 0.80,       # mostly music, minimal vocals
        "speechiness":      0.04,       # no rapping or spoken word
        "popularity":       0.35,       # prefers underground / niche finds
    }

    # Persona 3 — "Riley": headbanging metal fan who craves raw intensity.
    # Wants dark, aggressive songs with maximum energy and very fast tempos.
    deep_intense_rock = {
        "genre":            "rock",
        "mood":             "intense",
        "energy":           0.95,       # as loud and aggressive as possible
        "valence":          0.20,       # dark, brooding emotional tone
        "danceability":     0.35,       # not danceable — headbang territory
        "tempo_bpm":        160,        # fast, driving rhythm
        "acousticness":     0.05,       # electric guitars, distortion — no acoustic
        "instrumentalness": 0.15,       # heavy vocals/screaming are part of the appeal
        "speechiness":      0.10,       # some lyrical intensity is fine
        "popularity":       0.40,       # appreciates cult classics over pop crossovers
    }

    profiles = [
        ("High-Energy Pop  (Jordan)", high_energy_pop),
        ("Chill Lofi       (Sam)",    chill_lofi),
        ("Deep Intense Rock (Riley)", deep_intense_rock),
    ]

    for label, user_prefs in profiles:
        print(f"\n{'='*55}")
        print(f"Profile: {label}")
        print(f"{'='*55}")
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print("\nTop recommendations:\n")
        for rec in recommendations:
            song, score, explanation = rec
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
