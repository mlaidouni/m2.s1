# TP 4

## Partie 1

## Partie 2

### Question 1

RX0 → PD0
TX0 → PD1

### Question 2

Les broches PD0 (RX) et PD1 (TX) sont reliées au convertisseur USB-Série intégré à la carte.
Cela permet la communication série entre le PC et le microcontrôleur via le port USB.

### Question 7

La LED reste allumée 5 secondes pour chaque caractère reçu.

## Partie 3

### Question 1

- Buffer vide: head == tail
- Buffer plein (avec la solution N-1): (head + 1) % N == tail
