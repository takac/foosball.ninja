CREATE TABLE player(id INTEGER primary key autoincrement, name VARCHAR(50));
CREATE TABLE game(id INTEGER primary key autoincrement, winner INTEGER,
    opponent INTEGER, gamedate DATE,
    FOREIGN KEY(winner) references player(id),
    foreign key(opponent) references player(id));
