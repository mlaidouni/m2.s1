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

$N_{cycles} = 1 + (N_{initial} - 1) \times 3 + 2 = 3 * N_{initial}$  
$N_{initial} = \frac{N_{cycles}}{3}$

## Question 3

Comme la carte est cadencée à 16 MHz, la période d'horloge est de :

$T_{horloge} = \frac{1}{16 MHz} = 62.5 ns$

Le temps d'exécution total est donc de :

$T_{execution} = N_{cycles} \times T_{horloge} = 765 \times 62.5 ns = 47.81 \mu s$

Pour augmenter ce temps, on peut augmenter la valeure initiale chargée. Mais comme on utilise un registre 8 bits, la valeur maximale est 255. On peut donc envisager d'utiliser plusieurs registres pour écrire une valeur plus grande.

### Question 5

- subi : 1 cycle
- sbci : 1 cycle
- brne : 1 cycle si saut, 2 cycles sinon

0xFFFFFF = 16 777 215

$1 + 16 777 215 \times 5 + 5 = 83 886 081$ cycles, sans compter les cycles de `rjmp`.

On a donc :

$N_{cycles} = 1 + (N_{initial} - 1) \times 4 + 5 = ?_{initial} \times 4 + 2$  
$N_{initial} = \frac{N_{cycles} - 2}{4}$

## Question 6

Nombre de cycles en 500 ms :
$N_{cycles} = 16 \times 10^6 \times 0.5 = 8 \times 10^6$ cycles

Nombre initial :

$N_{initial} = \frac{8 \times 10^6 - 2}{4} = 1 999 999.5 \approx 2 \times 10^6$

Il faut donc initialiser les registres avec la valeur 2 000 000, soit 0x1E8480.

- r18 = 0x80
- r19 = 0x84
- r20 = 0x1E
