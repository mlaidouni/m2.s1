.text
	; initalisation des registres r18, r19 et r20 à 0xFF
    ldi r18, 0xFF
    ldi r19, 0xFF
    ldi r20, 0xFF

loop:
    subi r18, 1 ; décrémente en gérant le flag de retenue
    sbci r19, 0 ; décrémente en tenant compte d’une éventuelle retenue venant du précédent octet
    sbci r20, 0
    brne loop   ; tant que Z=0 → continuer
end:

    rjmp end	; boucle infinie