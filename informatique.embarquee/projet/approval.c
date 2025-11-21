#include <avr/io.h>
#include <avr/interrupt.h>
#include "approval.h"

/* Allume et éteint la LED */
void led_on(void) { LED_PORT |= _BV(LED_BIT); }
void led_off(void) { LED_PORT &= ~_BV(LED_BIT); }
static inline void led_toggle(void) { LED_PORT ^= _BV(LED_BIT); }

/* Initialisation de Timer1 pour des interruptions toutes les 1ms */
static void timer1_init(void) {
    TCCR1A = 0;      // CTC mode
    OCR1A = 31249;                // 500ms à 16MHz
    TCCR1B = _BV(WGM12) | _BV(CS12); 
	TIMSK1 = _BV(OCIE1A);
    sei(); // On active les interruptions globales
}

/* Initialisation des E/S et du Timer1 */
void approval_init(void) {
    LED_DDR = _BV(LED_BIT);
    LED_PORT = 0;

	// TODO: Boutton

	// Initialisation de Timer1 pour les interruptions toutes les 1ms
    timer1_init();
}

/* Interruption Timer1 CompareA */
ISR(TIMER1_COMPA_vect)
{
	// On alterne l'état de la LED
	led_toggle();
}
