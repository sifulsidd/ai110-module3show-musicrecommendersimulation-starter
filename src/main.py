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

    # ADDED: Single test profile used for all recommendation comparisons.
    # Persona — "Alex": a late-night, low-energy listener who prefers
    # acoustic and instrumental sounds over high-intensity electronic music.
    # Changing values here automatically updates both the OOP and functional paths.
    test_user = UserProfile(
        favorite_genre="lofi",            # broad style preference
        favorite_mood="chill",            # listening intent
        target_energy=0.38,               # calm, not intense
        target_valence=0.62,              # moderately positive, not euphoric
        target_danceability=0.55,         # some groove, not a dancefloor vibe
        target_tempo_bpm=80,              # slow to mid tempo
        likes_acoustic=True,              # prefers organic over electronic sound
        target_instrumentalness=0.75,     # prefers music without heavy vocals
        target_speechiness=0.04,          # dislikes rap / spoken word content
        target_popularity=0.45,           # leans niche over mainstream
    )

    # Derive the dict from test_user so both paths always stay in sync
    user_prefs = {
        "genre":            test_user.favorite_genre,
        "mood":             test_user.favorite_mood,
        "energy":           test_user.target_energy,
        "valence":          test_user.target_valence,
        "danceability":     test_user.target_danceability,
        "tempo_bpm":        test_user.target_tempo_bpm,
        "acousticness":     0.80,
        "instrumentalness": test_user.target_instrumentalness,
        "speechiness":      test_user.target_speechiness,
        "popularity":       test_user.target_popularity,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    # ADDED: print active profile so simulation output shows whose taste is
    # being used for comparisons — makes manual testing easier to interpret.
    print(f"\nActive profile: {test_user}")
    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
