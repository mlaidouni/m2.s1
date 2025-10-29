# TP 2

## Partie 2

### Question 1

C'est l'instruction SEI. On l'effectue avec la fonction `sei()`.

### Question 2

Fréquence d'horloge : 16 MHz
timer 8-bit Counter0 : 256 valeurs (0 à 255)
Pas de prescaler : 1

$T_{overflow}$ = $\frac{256}{16 000 000}$ = 16 µs$

### Question 3

Durée maximale configurable entre deux TOV : prescaler /1024

$T_{overflow\_max}$ = $\frac{256 \times 1024}{16 000 000}$ = 16.384 ms

### Question 4

En utilisant le timer 16-bit Counter1 :

Fréquence d'horloge : 16 MHz
Timer 16-bit Counter1 : 65536 valeurs (0 à 65535)
Pas de prescaler : 1

$T_{overflow}$ = $\frac{65536}{16 000 000}$ = 4.096 ms$

Durée maximale configurable entre deux TOV : prescaler /1024

$T_{overflow\_max}$ = $\frac{65536 \times 1024}{16 000 000}$ = 4.194304 s

### Question 5

Pour avoir une interruption toutes les 500ms, n reprend la formule vue en question 4.

$T_{interruption}$ = $\frac{(OCR1A + 1) \times prescaler}{16 000 000}$
$OCR1A$ = $\frac{T_{interruption} \times 16 000 000}{prescaler} - 1$

avec $T_{interruption}$ = 0.5s

| prescaler | OCR1A  | T_interruption réelle |
| --------- | ------ | --------------------- |
| 8         | 999999 | 0.5s                  |
| 64        | 12499  | 0.5s                  |
| 256       | 31249  | 0.5s                  |
| 1024      | 15624  | 0.503s                |

On choisit donc un prescaler de 256 et OCR1A = 31249 pour avoir une interruption toutes les 500ms.
