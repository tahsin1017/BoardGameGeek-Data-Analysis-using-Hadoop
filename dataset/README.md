# Dataset

## Source

Dataset URL:

https://www.kaggle.com/datasets/jvanelteren/boardgamegeek-reviews

This project uses the **BoardGameGeek Reviews** dataset from Kaggle.

The file used for analysis is:

`games_detailed_info.csv`

The dataset contains detailed information about board games collected from BoardGameGeek.

## Raw Dataset Summary

- Raw rows: 21,631
- Raw columns: 56
- Duplicate game IDs: 0
- Invalid CSV rows: 0

## Preprocessing

The raw dataset contains list-valued fields such as categories and publishers.

To preserve one record per game:

- the first listed category is used as `primaryCategory`
- the first listed publisher is used as `primaryPublisher`

Rows missing a usable category or publisher were removed.

## Clean Dataset

Final cleaned file:

`boardgames.csv`

Final rows:

21,347

Final fields:

1. gameID
2. name
3. yearPublished
4. primaryPublisher
5. primaryCategory
6. minPlayers
7. maxPlayers
8. playingTime
9. usersRated
10. averageRating
11. owned
12. numComments
13. averageWeight

The cleaned dataset contains:

- 21,347 games
- 81 primary categories
- 3,824 primary publishers

The raw Kaggle dataset is not included in this repository because of its size.
