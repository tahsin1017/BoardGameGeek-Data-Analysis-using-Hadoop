A = LOAD '/boardgame/boardgames.csv' USING PigStorage(',')
    AS (
        gameID:chararray,
        name:chararray,
        yearPublished:int,
        primaryPublisher:chararray,
        primaryCategory:chararray,
        minPlayers:int,
        maxPlayers:int,
        playingTime:int,
        usersRated:long,
        averageRating:double,
        owned:long,
        numComments:long,
        averageWeight:double
    );

A2 = FILTER A BY primaryCategory IS NOT NULL
               AND primaryCategory != '';

B = GROUP A2 BY primaryCategory;

C = FOREACH B GENERATE
        group AS category,
        COUNT(A2) AS gameCount;

G = GROUP C ALL;

TOP5 = FOREACH G {
    S = ORDER C BY gameCount DESC;
    L = LIMIT S 5;
    GENERATE FLATTEN(L);
};

STORE TOP5 INTO '/boardgame/pig_top5_categories'
    USING PigStorage('|');
