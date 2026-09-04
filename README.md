# BoardGameGeek Data Analysis using Hadoop

A Big Data Analytics project analyzing BoardGameGeek game data using Hadoop MapReduce and Apache Pig.

## Project Overview

This project contains:

- 3 Hadoop MapReduce analyses
- 5 Apache Pig analyses
- HDFS-based dataset storage
- Python preprocessing
- Verified result files
- Execution screenshots

## Technologies Used

- Hadoop 3.4.1
- Apache Pig 0.17.0
- Java / OpenJDK 11
- Python 3
- HDFS
- YARN
- macOS

## Dataset

The project uses `games_detailed_info.csv` from the BoardGameGeek Reviews dataset.

Raw dataset:

- 21,631 rows
- 56 columns
- 0 duplicate game IDs
- 0 malformed CSV rows

After preprocessing:

- 21,347 games
- 13 fields
- 81 primary categories
- 3,824 primary publishers

The preprocessing script is:

`preprocessing/prepare_boardgames.py`

### Cleaned Schema

```text
gameID
name
yearPublished
primaryPublisher
primaryCategory
minPlayers
maxPlayers
playingTime
usersRated
averageRating
owned
numComments
averageWeight
Hadoop MapReduce Analyses
MR-1: Most Owned Board Game

Finds the game with the highest owned value.

30549    Pandemic    168364

Pandemic is the most-owned game in the cleaned dataset with 168,364 owners.

Source:

MapReduce/MR1_MostOwned/

Result:

results/mapreduce/mr1_most_owned.txt

MR-2: Rating and Engagement Summary

Produces one record for each game containing:

average rating
users rated
comments

Total output records:

21347

Pandemic example:

30549    7.58896    109006    17305

Source:

MapReduce/MR2_RatingEngagement/

Result:

results/mapreduce/mr2_rating_summary.txt

MR-3: Games per Publisher

Counts games for each primary publisher.

Top 10:

(Self-Published)     543
(Web published)      380
Hasbro                379
Decision Games (I)    272
GMT Games             268
Ravensburger          255
AMIGO                  249
(Public Domain)       214
KOSMOS                 212
999 Games              208

Total primary publishers:

3824

Source:

MapReduce/MR3_GamesPerPublisher/

Result:

results/mapreduce/mr3_games_per_publisher.txt

Apache Pig Analyses
Pig-1: Top 5 Primary Categories
Card Game|4615
Abstract Strategy|1544
Adventure|1144
Action / Dexterity|1057
Animals|1049

Result:

results/pig/pig1_top5_categories.txt

Pig-2: Top 10 Most-Rated Games

Here, "Most-Rated" means the largest number of users who submitted ratings (usersRated), not the highest average score.

30549|Pandemic|Medical|109006
822|Carcassonne|City Building|108776
13|Catan|Economic|108064
68448|7 Wonders|Ancient|90021
36218|Dominion|Card Game|81582
9209|Ticket to Ride|Trains|76207
178900|Codenames|Card Game|74456
167791|Terraforming Mars|Economic|74269
173346|7 Wonders Duel|Ancient|69528
31260|Agricola|Animals|66107

Result:

results/pig/pig2_top10_most_rated.txt

Pig-3: Top 10 Most-Owned Games
30549|Pandemic|Medical|168364
13|Catan|Economic|167733
822|Carcassonne|City Building|161299
68448|7 Wonders|Ancient|120466
178900|Codenames|Card Game|119753
173346|7 Wonders Duel|Ancient|111275
36218|Dominion|Card Game|106956
9209|Ticket to Ride|Trains|105748
167791|Terraforming Mars|Economic|101872
129622|Love Letter|Card Game|98395

Result:

results/pig/pig3_top10_most_owned.txt

Pig-4: Top 10 Most-Rated Games by Category

Games are grouped by primaryCategory, sorted by usersRated, and the top 10 from each category are retained.

81 categories represented
800 output rows

Example — Card Game:

36218|Dominion|Card Game|81582
178900|Codenames|Card Game|74456
148228|Splendor|Card Game|64734
129622|Love Letter|Card Game|59484
39856|Dixit|Card Game|54525
28143|Race for the Galaxy|Card Game|48919
1927|Munchkin|Card Game|43759
98778|Hanabi|Card Game|41588
11|Bohnanza|Card Game|40113
50|Lost Cities|Card Game|39535

Result:

results/pig/pig4_top10_rated_by_category.txt

Pig-5: Top 10 Most-Owned Games by Category

Games are grouped by primaryCategory, sorted by owned, and the top 10 from each category are retained.

81 categories represented
800 output rows

Example — Card Game:

178900|Codenames|Card Game|119753
36218|Dominion|Card Game|106956
129622|Love Letter|Card Game|98395
148228|Splendor|Card Game|92366
1927|Munchkin|Card Game|78849
39856|Dixit|Card Game|76535
98778|Hanabi|Card Game|68643
133473|Sushi Go!|Card Game|65495
11|Bohnanza|Card Game|60282
28143|Race for the Galaxy|Card Game|59758

Result:

results/pig/pig5_top10_owned_by_category.txt

Hadoop Environment

The cleaned dataset was stored in HDFS at:

/boardgame/boardgames.csv

MapReduce and Pig results were also written under /boardgame/.

Project Structure
boardgame_lab/
├── MapReduce/
│   ├── MR1_MostOwned/
│   ├── MR2_RatingEngagement/
│   └── MR3_GamesPerPublisher/
├── PigAnalysis/
├── preprocessing/
├── dataset/
├── results/
│   ├── mapreduce/
│   └── pig/
├── screenshots/
└── report/
Key Findings
Pandemic is the most-owned game with 168,364 owners.
Pandemic has the largest number of user ratings with 109,006 ratings.
Card Game is the largest primary category with 4,615 games.
(Self-Published) is the largest primary publisher group with 543 games.
The cleaned dataset contains 21,347 games.
Notes

(Self-Published), (Web published), and (Public Domain) are values contained in the source dataset and are not preprocessing errors.

Apache Pig 0.17.0 was executed in MapReduce mode with Hadoop 3.4.1. Nested ORDER BY operations inside grouped FOREACH blocks are used for the ranking analyses.

Author

Tahsin Ahmed Rafi

Department of Computer Science and Engineering
Premier University, Chittagong
Hadoop MapReduce Analyses
MR-1: Most Owned Board Game

Finds the game with the highest owned value.

30549    Pandemic    168364

Pandemic is the most-owned game in the cleaned dataset with 168,364 owners.

Source:

MapReduce/MR1_MostOwned/

Result:

results/mapreduce/mr1_most_owned.txt

MR-2: Rating and Engagement Summary

Produces one record for each game containing:

average rating
users rated
comments

Total output records:

21347

Pandemic example:

30549    7.58896    109006    17305

Source:

MapReduce/MR2_RatingEngagement/

Result:

results/mapreduce/mr2_rating_summary.txt

MR-3: Games per Publisher

Counts games for each primary publisher.

Top 10:

(Self-Published)     543
(Web published)      380
Hasbro                379
Decision Games (I)    272
GMT Games             268
Ravensburger          255
AMIGO                  249
(Public Domain)       214
KOSMOS                 212
999 Games              208

Total primary publishers:

3824

Source:

MapReduce/MR3_GamesPerPublisher/

Result:

results/mapreduce/mr3_games_per_publisher.txt

Apache Pig Analyses
Pig-1: Top 5 Primary Categories
Card Game|4615
Abstract Strategy|1544
Adventure|1144
Action / Dexterity|1057
Animals|1049

Result:

results/pig/pig1_top5_categories.txt

Pig-2: Top 10 Most-Rated Games

Here, "Most-Rated" means the largest number of users who submitted ratings (usersRated), not the highest average score.

30549|Pandemic|Medical|109006
822|Carcassonne|City Building|108776
13|Catan|Economic|108064
68448|7 Wonders|Ancient|90021
36218|Dominion|Card Game|81582
9209|Ticket to Ride|Trains|76207
178900|Codenames|Card Game|74456
167791|Terraforming Mars|Economic|74269
173346|7 Wonders Duel|Ancient|69528
31260|Agricola|Animals|66107

Result:

results/pig/pig2_top10_most_rated.txt

Pig-3: Top 10 Most-Owned Games
30549|Pandemic|Medical|168364
13|Catan|Economic|167733
822|Carcassonne|City Building|161299
68448|7 Wonders|Ancient|120466
178900|Codenames|Card Game|119753
173346|7 Wonders Duel|Ancient|111275
36218|Dominion|Card Game|106956
9209|Ticket to Ride|Trains|105748
167791|Terraforming Mars|Economic|101872
129622|Love Letter|Card Game|98395

Result:

results/pig/pig3_top10_most_owned.txt

Pig-4: Top 10 Most-Rated Games by Category

Games are grouped by primaryCategory, sorted by usersRated, and the top 10 from each category are retained.

81 categories represented
800 output rows

Example — Card Game:

36218|Dominion|Card Game|81582
178900|Codenames|Card Game|74456
148228|Splendor|Card Game|64734
129622|Love Letter|Card Game|59484
39856|Dixit|Card Game|54525
28143|Race for the Galaxy|Card Game|48919
1927|Munchkin|Card Game|43759
98778|Hanabi|Card Game|41588
11|Bohnanza|Card Game|40113
50|Lost Cities|Card Game|39535

Result:

results/pig/pig4_top10_rated_by_category.txt

Pig-5: Top 10 Most-Owned Games by Category

Games are grouped by primaryCategory, sorted by owned, and the top 10 from each category are retained.

81 categories represented
800 output rows

Example — Card Game:

178900|Codenames|Card Game|119753
36218|Dominion|Card Game|106956
129622|Love Letter|Card Game|98395
148228|Splendor|Card Game|92366
1927|Munchkin|Card Game|78849
39856|Dixit|Card Game|76535
98778|Hanabi|Card Game|68643
133473|Sushi Go!|Card Game|65495
11|Bohnanza|Card Game|60282
28143|Race for the Galaxy|Card Game|59758

Result:

results/pig/pig5_top10_owned_by_category.txt

Hadoop Environment

The cleaned dataset was stored in HDFS at:

/boardgame/boardgames.csv

MapReduce and Pig results were also written under /boardgame/.

Project Structure
boardgame_lab/
├── MapReduce/
│   ├── MR1_MostOwned/
│   ├── MR2_RatingEngagement/
│   └── MR3_GamesPerPublisher/
├── PigAnalysis/
├── preprocessing/
├── dataset/
├── results/
│   ├── mapreduce/
│   └── pig/
├── screenshots/
└── report/
Key Findings
Pandemic is the most-owned game with 168,364 owners.
Pandemic has the largest number of user ratings with 109,006 ratings.
Card Game is the largest primary category with 4,615 games.
(Self-Published) is the largest primary publisher group with 543 games.
The cleaned dataset contains 21,347 games.
Notes

(Self-Published), (Web published), and (Public Domain) are values contained in the source dataset and are not preprocessing errors.

Apache Pig 0.17.0 was executed in MapReduce mode with Hadoop 3.4.1. Nested ORDER BY operations inside grouped FOREACH blocks are used for the ranking analyses.

Author

Tahsin Ahmed Rafi

Department of Computer Science and Engineering
Premier University, Chittagong
