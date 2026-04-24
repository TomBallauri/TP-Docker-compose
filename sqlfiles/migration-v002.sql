USE ynov_ci;

CREATE TABLE utilisateurs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL
);

INSERT INTO utilisateurs (nom, email) VALUES
    ('Alice Martin', 'alice@example.com'),
    ('Bob Dupont', 'bob@example.com'),
    ('Charlie Durand', 'charlie@example.com'),
    ('Diana Moreau', 'diana@example.com');
