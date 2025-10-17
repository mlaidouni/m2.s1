# TP 2

## Partie 1

- **Question 1** : PB5
- **Question 2** : Le GPIO

## Partie 2

### Question 2

- ldi : 1 cycle
- dec : 1 cycle
- brne : 1 cycle si saut, 2 cycles sinon

$1 + 254 \times 3 + 2 = 765$ cycles, sans compter les cycles de `rjmp`.

On a donc :

$N_{cycles} = 1 + (N_{initial} - 1) * 3 + 2 = 3 * N_{initial}$  
$N_{initial} = \frac{N_{cycles}}{3}$
