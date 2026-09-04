import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.expanduser("~/boardgame_lab")
RESULTS_DIR = os.path.join(BASE_DIR, "results", "pig")
OUT_DIR = os.path.join(BASE_DIR, "visualizations", "pig")
os.makedirs(OUT_DIR, exist_ok=True)

# -----------------------------
# Pig-1: Top 5 Categories
# -----------------------------
pig1 = pd.read_csv(
    os.path.join(RESULTS_DIR, "pig1_top5_categories.txt"),
    sep="|",
    header=None,
    names=["Category", "GameCount"]
)

plt.figure(figsize=(10, 6))
plt.bar(pig1["Category"], pig1["GameCount"])
plt.title("Pig-1: Top 5 Primary Categories")
plt.xlabel("Primary Category")
plt.ylabel("Number of Games")
plt.xticks(rotation=20, ha="right")
for i, v in enumerate(pig1["GameCount"]):
    plt.text(i, v + 20, str(v), ha="center", fontsize=9)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "pig1_top5_categories.png"), dpi=300)
plt.close()

# -----------------------------
# Pig-2: Top 10 Most Rated
# -----------------------------
pig2 = pd.read_csv(
    os.path.join(RESULTS_DIR, "pig2_top10_most_rated.txt"),
    sep="|",
    header=None,
    names=["gameID", "name", "category", "usersRated"]
)

plt.figure(figsize=(11, 7))
plt.barh(pig2["name"], pig2["usersRated"])
plt.title("Pig-2: Top 10 Most-Rated Games")
plt.xlabel("Users Rated")
plt.ylabel("Game Name")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "pig2_top10_most_rated.png"), dpi=300)
plt.close()

# -----------------------------
# Pig-3: Top 10 Most Owned
# -----------------------------
pig3 = pd.read_csv(
    os.path.join(RESULTS_DIR, "pig3_top10_most_owned.txt"),
    sep="|",
    header=None,
    names=["gameID", "name", "category", "owned"]
)

plt.figure(figsize=(11, 7))
plt.barh(pig3["name"], pig3["owned"])
plt.title("Pig-3: Top 10 Most-Owned Games")
plt.xlabel("Ownership Count")
plt.ylabel("Game Name")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "pig3_top10_most_owned.png"), dpi=300)
plt.close()

# -----------------------------
# Pig-4: Top 10 Most Rated by Category
# Use Card Game category as a representative visualization
# -----------------------------
pig4 = pd.read_csv(
    os.path.join(RESULTS_DIR, "pig4_top10_rated_by_category.txt"),
    sep="|",
    header=None,
    names=["gameID", "name", "category", "usersRated"]
)

pig4_card = pig4[pig4["category"] == "Card Game"].copy()
pig4_card = pig4_card.sort_values("usersRated", ascending=False).head(10)

plt.figure(figsize=(11, 7))
plt.barh(pig4_card["name"], pig4_card["usersRated"])
plt.title("Pig-4: Top 10 Most-Rated Card Games")
plt.xlabel("Users Rated")
plt.ylabel("Game Name")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "pig4_card_game_top10_rated.png"), dpi=300)
plt.close()

# -----------------------------
# Pig-5: Top 10 Most Owned by Category
# Use Card Game category as a representative visualization
# -----------------------------
pig5 = pd.read_csv(
    os.path.join(RESULTS_DIR, "pig5_top10_owned_by_category.txt"),
    sep="|",
    header=None,
    names=["gameID", "name", "category", "owned"]
)

pig5_card = pig5[pig5["category"] == "Card Game"].copy()
pig5_card = pig5_card.sort_values("owned", ascending=False).head(10)

plt.figure(figsize=(11, 7))
plt.barh(pig5_card["name"], pig5_card["owned"])
plt.title("Pig-5: Top 10 Most-Owned Card Games")
plt.xlabel("Ownership Count")
plt.ylabel("Game Name")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "pig5_card_game_top10_owned.png"), dpi=300)
plt.close()

print("Done. Pig visualizations saved in:")
print(OUT_DIR)
