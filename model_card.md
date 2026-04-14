# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

The system works best for users with strongly defined, consistent preferences — particularly listeners whose genre, mood, and audio features all point in the same direction. In testing, the Chill Lofi profile (Sam) achieved the highest scores in the entire experiment, with Library Rain scoring 9.62 and Midnight Coding close behind at 9.57, because that persona stacked genre, mood, acoustic, and low-energy signals that all reinforced each other across both flat bonuses and continuous similarity. The multi-dimensional continuous scoring captures genuine audio nuance that a genre-only recommender would miss — for example, Storm Runner appeared in Jordan's High-Energy Pop top five purely because its energy profile matched, even though it is a rock song, which reflects real listening behavior where genre boundaries blur at the extremes. The system also produces intuitively correct separation at the top of each ranked list: in every profile tested, the #1 recommendation was a clear and defensible choice that a human curator would likely agree with. Finally, the transparent explanation string printed alongside each score makes it easy to audit why a song was recommended, which is a meaningful advantage over black-box approaches — a user can immediately see whether a high score came from a genre match or from genuine audio similarity.  

---

## 6. Limitations and Bias 

The most significant weakness uncovered during testing is that the scoring formula treats genre and mood as all-or-nothing string matches — a "rock" preference earns zero credit for a "metal" or "alternative" song, even though those genres share nearly identical audio characteristics. This forces the system into a rigid filter bubble: users whose preferred genre label does not exactly match a label in the dataset permanently lose up to 2.5 points of flat bonus with no warning or fallback, while listeners of well-represented genres like "pop" benefit from that bonus on every matching song. The system also contains a structural imbalance that silently favors acoustic music listeners — they can earn a hidden +1.0 bonus unavailable to any non-acoustic user, meaning an EDM or hip-hop listener's theoretical maximum score is always 1.0 point lower no matter how perfectly a song matches their other preferences. Additionally, with energy weighted at three times any other continuous feature, moderate-energy listeners (those targeting around 0.5) receive near-identical energy scores across almost every song in the catalog, effectively collapsing that dimension and forcing their rankings to be decided by lower-weighted features like speechiness and popularity. Finally, the system does not consider listening context, time of day, recently played history, or explicit dislike signals — meaning a user who has heard the top-recommended song fifty times will receive it again, with no mechanism for variety or novelty.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
