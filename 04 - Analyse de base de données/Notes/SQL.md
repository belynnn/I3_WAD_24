# SELECT
## Requête simples sur un seul

### Sélectionne quelques les colonnes (champs) d'un tableau (table)
SELECT nom, prix_unitaire FROM article

### Sélectionne toutes les colonnes (champs) d'un tableau (table)
SELECT * FROM article

## Requête avec un filtre simple sur un seul tableau
SELECT nom FROM article WHERE prix_unitaire > 2

## Requête avec un filtre double sur un seul tableau
SELECT nom FROM article WHERE prix_unitaire > 2 AND prix_unitaire < 4

### Chercher du chocolat
SELECT * FROM article WHERE nom = "chocolat"

SELECT * FROM `article` WHERE `nom` = 'chocolat' or prix_unitaire < 2; 

## Requête à 2 tableaux (JOIN) - jointure à plusieurs tableaux
// ANCIEN NOTATION
SELECT * FROM client, commande WHERE client.id = commande.idClient