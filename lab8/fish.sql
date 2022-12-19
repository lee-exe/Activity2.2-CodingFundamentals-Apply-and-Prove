CREATE TABLE fish (
    fish_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    class VARCHAR(25),
    fish_order VARCHAR(50),
    family VARCHAR(50)
);

INSERT INTO fish (fish_id, name, class, fish_order, family)
VALUES
    (1, 'Hammerhead Shark', 'Chondrichthyes', 'Carcharhiniformes', 'Sphyrnidae'),
    (2, 'Clownfish', 'Actinopterygii', 'Perciformes', 'Pomacentridae'),
    (3, 'Blue Whale', 'Mammalia', 'Cetacea', 'Balaenopteridae');
