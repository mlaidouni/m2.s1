#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>

/* Note [cours 6, page 36]
On préfère les variable stockées sur 1 octet (uint8_t), 
plutôt que sur plusieurs octets (int -> 2 octets).
*/

const uint8_t pattern[] = {1,0,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0};

/* Doit être globale volatile pour être utilisée dans l'ISR */
volatile uint8_t pattern_idx = 0;

void led_on(void) { PORTB |= _BV(PORTB5); }
void led_off(void) { PORTB &= ~_BV(PORTB5); }

/* Interruption Timer1 CompareA */
ISR(TIMER1_COMPA_vect)
{
    if (pattern[pattern_idx]) led_on();
    else led_off();

    pattern_idx++;
    if (pattern_idx >= (sizeof(pattern)/sizeof(pattern[0])))
        pattern_idx = 0;
}

int main (void)
{
	// On configure la LED en sortie
    DDRB = _BV(DDB5);
    PORTB = 0;

	// On désactive les modules non utilisés du MCU pour économiser de l'énergie
	// [doc page 53] On utilse Timer1, donc on désactive ADC, Analog Comparator
	PRR = _BV(PRADC) | _BV(PRUSART0) | _BV(PRSPI) | _BV(PRTWI);

	// On configure le Timer1 en mode CTC, OCR1A comme TOP et le prescaler à 256
	/* Voir la page 141 de la doc.
	https://ww1.microchip.com/downloads/en/DeviceDoc/ATmega48A-PA-88A-PA-168A-PA-328-P-DS-DS40002061B.pdf

	[doc page 141] Pour mettre en mode CTC avec OCR1A comme TOP, il faut choisir le mode 4 (WGM13:0 = 0100)

	Pour cela, il faut mettre à 0 les bits WGM10 et WGM11, via TCCR1A [doc page 140]
	Il faut mettre à 0 le bit WGM13 (pour que le TOP soit OCR1A), via TCCR1B [doc page 142]
	Il faut mettre à 1 le bit WGM12, via TCCR1B [doc page 142]
	Pour choisir un prescaler de 256, il faut mettre à 1 le bit CS12 et à 0 les bits CS11 et CS10, via TCCR1B [doc page 143]
	*/
	TCCR1A = 0;
	TCCR1B = _BV(WGM12) | _BV(CS12);
	OCR1A = 31249; // Pour une interruption toutes les 500ms à 16MHz

	// On active les interruptions du Timer1 CompareA [doc page 144]
	TIMSK1 = _BV(OCIE1A);

	// On active les interruptions globales
	sei();

	// On met le MCU en mode sommeil (on a besoin de conserver Timer1 actif)
	set_sleep_mode(SLEEP_MODE_IDLE);

	for (;;) sleep_mode(); // Boucle principale : on dort en attendant les interruptions de Timer1
}
