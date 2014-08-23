INSERT INTO player(name) VALUES ('Tom');
INSERT INTO player(name) VALUES ('Matt');
INSERT INTO player(name) VALUES ('Mark');
INSERT INTO player(name) VALUES ('Sam');

/* Tom wins 16 games against matt */
INSERT INTO game (winner, opponent, gamedate) VALUES
    (1, 2, date('now')),
    (1, 2, date('now')),
    (1, 2, date('now')),
    (1, 2, date('now')),
    (1, 2, date('now')),
    (1, 2, date('now')),
    (1, 2, date('now')),
    (1, 2, date('now')),
    (1, 2, date('now')),
    (1, 2, date('now')),
    (1, 2, date('now')),
    (1, 2, date('now')),
    (1, 2, date('now')),
    (1, 2, date('now')),
    (1, 2, date('now')),
    (1, 2, date('now'));

/* Matt wins 14 games against Tom */
INSERT INTO game (winner, opponent, gamedate) VALUES
    (2, 1, date('now')),
    (2, 1, date('now')),
    (2, 1, date('now')),
    (2, 1, date('now')),
    (2, 1, date('now')),
    (2, 1, date('now')),
    (2, 1, date('now')),
    (2, 1, date('now')),
    (2, 1, date('now')),
    (2, 1, date('now')),
    (2, 1, date('now')),
    (2, 1, date('now')),
    (2, 1, date('now')),
    (2, 1, date('now'));

/* Tom wins 10 games against Sam */
INSERT INTO game (winner, opponent, gamedate) VALUES
    (1, 3, date('now')),
    (1, 3, date('now')),
    (1, 3, date('now')),
    (1, 3, date('now')),
    (1, 3, date('now')),
    (1, 3, date('now')),
    (1, 3, date('now')),
    (1, 3, date('now')),
    (1, 3, date('now')),
    (1, 3, date('now'));
