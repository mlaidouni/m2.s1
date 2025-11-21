#include <avr/io.h>
#include <avr/interrupt.h>
#include "approval.h"

int main (void)
{
	// Initalisation de la LED
	approval_init();

	// On désactive les modules non utilisés du MCU pour économiser de l'énergie
	// [doc page 53] On utilse Timer1, donc on désactive ADC, Analog Comparator
	// PRR = _BV(PRADC) | _BV(PRUSART0) | _BV(PRSPI) | _BV(PRTWI);


	// On met le MCU en mode sommeil (on a besoin de conserver Timer1 actif)
	// set_sleep_mode(SLEEP_MODE_IDLE);

	while (1) ;
}
