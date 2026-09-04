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

A2 = FILTER A BY usersRated IS NOT NULL;

G = GROUP A2 ALL;

TOP10 = FOREACH G {
    S = ORDER A2 BY usersRated DESC;
    L = LIMIT S 10;
    GENERATE FLATTEN(L);
};

R = FOREACH TOP10 GENERATE
        gameID,
        name,
        primaryCategory,
        usersRated;

STORE R INTO '/boardgame/pig_top10_most_rated'
    USING PigStorage('|');
