INSERT INTO player(name) VALUES ('Tom');
INSERT INTO player(name) VALUES ('Matt');
INSERT INTO player(name) VALUES ('Mark');
INSERT INTO player(name) VALUES ('Sam');

/* Tom wins 16 games against matt */
INSERT INTO game (winner, opponent, gamedate) VALUES
    (1, 2, datetime('2012-11-16 13:12:22')),
    (1, 2, datetime('2012-11-16 12:12:22')),
    (1, 2, datetime('2012-11-16 11:12:22')),
    (1, 2, datetime('2012-11-16 10:12:22')),
    (1, 2, datetime('2012-11-16 09:12:22')),
    (1, 2, datetime('2012-11-16 08:12:22')),
    (1, 2, datetime('2012-11-16 07:12:22')),
    (1, 2, datetime('2012-11-16 06:12:22')),
    (1, 2, datetime('2012-11-16 06:12:22')),
    (1, 2, datetime('2012-11-15 06:12:22')),
    (1, 2, datetime('2012-11-15 05:12:22')),
    (1, 2, datetime('2012-11-20 03:12:22')),
    (1, 2, datetime('2012-11-20 01:12:22')),
    (1, 2, datetime('2012-11-16 03:12:22')),
    (1, 2, datetime('2012-11-28 03:12:04')),
    (1, 2, datetime('2012-11-16 03:12:44'));

/* Matt wins 14 games against Tom */
INSERT INTO game (winner, opponent, gamedate) VALUES
    (2, 1, datetime('2012-11-19 12:12:22')),
    (2, 1, datetime('2012-11-19 11:12:22')),
    (2, 1, datetime('2012-11-19 10:12:22')),
    (2, 1, datetime('2012-11-19 09:12:22')),
    (2, 1, datetime('2012-11-19 08:12:22')),
    (2, 1, datetime('2012-11-19 07:12:22')),
    (2, 1, datetime('2012-11-19 06:12:22')),
    (2, 1, datetime('2012-11-19 06:12:22')),
    (2, 1, datetime('2012-11-19 06:12:22')),
    (2, 1, datetime('2012-11-19 05:12:22')),
    (2, 1, datetime('2012-11-29 03:12:22')),
    (2, 1, datetime('2012-11-29 01:12:22')),
    (2, 1, datetime('2012-11-19 03:12:22')),
    (2, 1, datetime('2012-11-29 03:12:04'));

/* Tom wins 10 games against Sam */
INSERT INTO game (winner, opponent, gamedate) VALUES
    (1, 3, datetime('2012-11-16 07:12:22')),
    (1, 3, datetime('2012-11-16 06:12:22')),
    (1, 3, datetime('2012-11-16 06:12:22')),
    (1, 3, datetime('2012-11-15 06:12:22')),
    (1, 3, datetime('2012-11-15 05:12:22')),
    (1, 3, datetime('2012-11-20 03:12:22')),
    (1, 3, datetime('2012-11-20 01:12:22')),
    (1, 3, datetime('2012-11-16 03:12:22')),
    (1, 3, datetime('2012-11-28 03:12:04')),
    (1, 3, datetime('2012-11-16 03:12:44'));

/* Sam and Mark play some games */
INSERT INTO game (winner, opponent, gamedate) VALUES
    (3, 4, datetime('2007-11-16 07:12:22')),
    (3, 4, datetime('2007-11-16 06:12:22')),
    (3, 4, datetime('2007-11-16 06:12:22')),
    (3, 4, datetime('2007-11-15 06:12:22')),
    (3, 4, datetime('2007-11-15 05:12:22')),
    (3, 4, datetime('2007-11-20 03:12:22')),
    (4, 3, datetime('2007-11-20 01:12:22')),
    (4, 3, datetime('2007-11-16 03:12:22')),
    (4, 3, datetime('2007-11-28 03:12:04')),
    (4, 3, datetime('2007-11-16 03:12:44'));
