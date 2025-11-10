-- Création de la table items
CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

-- Insertion de deux items pour test
INSERT INTO items (name) VALUES ('Item 1'), ('Item 2');
INSERT INTO items (name) VALUES ('Test 1'), ('Test 2');
