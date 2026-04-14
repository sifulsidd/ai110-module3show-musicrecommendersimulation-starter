flowchart TD
    A([User Preferences]) --> B[Load songs from CSV]
    B --> C[Set score = 0\nfor current song]
    C --> D{Genre match?}
    D -- Yes --> E[+2.0 pts]
    D -- No --> F{Mood match?}
    E --> F
    F -- Yes --> G[+1.5 pts]
    F -- No --> H{Likes acoustic\nAND acousticness ≥ 0.6?}
    G --> H
    H -- Yes --> I[+1.0 pts]
    H -- No --> J[Add similarity pts\nenergy, valence,\ndanceability, tempo,\ninstrumentalness,\nspeechiness, popularity]
    I --> J
    J --> K[Append song + score\nto results list]
    K --> L{More songs\nin CSV?}
    L -- Yes → next song --> C
    L -- No --> M[Sort results\nby score descending]
    M --> N([Return Top K Songs])

