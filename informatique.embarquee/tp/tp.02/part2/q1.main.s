.text
	ldi r24, 0xFF ; initialiser (donc charger) la valeur 0xFF dans le registre r24
	
loop:
	dec r24       ; décrémenter r24
	brne loop   ; si r24 != 0, alors Z == 0, donc on saute à loop
	
end:
	rjmp end      ; boucle infinie