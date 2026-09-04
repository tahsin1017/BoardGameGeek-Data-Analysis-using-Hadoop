import csv
import ast
import os

INPUT = "raw/games_detailed_info.csv"
OUTPUT = "clean/boardgames.csv"

HEADER = [
    "gameID",
    "name",
    "yearPublished",
    "primaryPublisher",
    "primaryCategory",
    "minPlayers",
    "maxPlayers",
    "playingTime",
    "usersRated",
    "averageRating",
    "owned",
    "numComments",
    "averageWeight"
]

def parse_first_list_item(value):
    if not value or not value.strip():
        return ""

    try:
        parsed = ast.literal_eval(value)
        if isinstance(parsed, list) and parsed:
            return str(parsed[0]).strip()
    except Exception:
        pass

    return ""

def clean_text(value):
    if value is None:
        return ""

    value = str(value)

    # Keep each Hadoop record on one physical line
    value = value.replace("\r", " ").replace("\n", " ")

    # Final dataset is comma-delimited, so remove embedded commas
    value = value.replace(",", " ")

    # Collapse repeated whitespace
    value = " ".join(value.split())

    return value.strip()

total = 0
written = 0
skip_no_category = 0
skip_no_publisher = 0
skip_missing_id = 0
skip_missing_name = 0

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)

with open(INPUT, newline="", encoding="utf-8-sig") as fin, \
     open(OUTPUT, "w", newline="", encoding="utf-8") as fout:

    reader = csv.DictReader(fin)
    writer = csv.writer(fout, lineterminator="\n")

    # No header in final Hadoop file, matching the old YouTube project
    for row in reader:
        total += 1

        game_id = clean_text(row.get("id", ""))
        name = clean_text(row.get("primary", ""))

        if not game_id:
            skip_missing_id += 1
            continue

        if not name:
            skip_missing_name += 1
            continue

        category = clean_text(
            parse_first_list_item(row.get("boardgamecategory", ""))
        )

        publisher = clean_text(
            parse_first_list_item(row.get("boardgamepublisher", ""))
        )

        if not category:
            skip_no_category += 1
            continue

        if not publisher:
            skip_no_publisher += 1
            continue

        output_row = [
            game_id,
            name,
            clean_text(row.get("yearpublished", "")),
            publisher,
            category,
            clean_text(row.get("minplayers", "")),
            clean_text(row.get("maxplayers", "")),
            clean_text(row.get("playingtime", "")),
            clean_text(row.get("usersrated", "")),
            clean_text(row.get("average", "")),
            clean_text(row.get("owned", "")),
            clean_text(row.get("numcomments", "")),
            clean_text(row.get("averageweight", ""))
        ]

        writer.writerow(output_row)
        written += 1

print("=== PREPROCESSING SUMMARY ===")
print("Raw rows            :", total)
print("Written rows        :", written)
print("Skipped no ID       :", skip_missing_id)
print("Skipped no name     :", skip_missing_name)
print("Skipped no category :", skip_no_category)
print("Skipped no publisher:", skip_no_publisher)
print("Output              :", OUTPUT)
