.text
	; sbi pour mettre un bit à 1 (et allumer la LED)
	; cbi pour mettre un bit à 0 (et éteindre la LED)
	sbi 0x04, 5    ; configure PB5 en output
	cbi 0x05, 5   ; met PB5 à 1 (etat haut)
	
loop:
	rjmp loop      ; boucle infinie