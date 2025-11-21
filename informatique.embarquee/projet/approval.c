#include <avr/io.h>
#include <avr/interrupt.h>
#include "approval.h"

/* Compteurs pour le timeout */
static volatile uint8_t tick_count = 0;    // compte les interruptions de 500 ms
static volatile uint8_t timeout_flag = 0;  // devient 1 après 10 s (20 × 500 ms)

/* Allume et éteint la LED */
static inline void led_on(void)  { LED_PORT |= _BV(LED_BIT); }
static inline void led_off(void) { LED_PORT &= ~_BV(LED_BIT); }
static inline void led_toggle(void) { LED_PORT ^= _BV(LED_BIT); }

/* Initialisation de Timer1 pour des interruptions toutes les 500 ms
   (OCR1A = 31249 avec prescaler 256 à 16 MHz -> 0.5 s) */
static void timer1_init(void) {
	TCCR1A = 0; // CTC mode
    OCR1A = 31249; // 500ms à 16MHz, prescaler 256
    TCCR1B = _BV(WGM12) | _BV(CS12); 
	TIMSK1 = _BV(OCIE1A);
    sei(); // On active les interruptions globales
}

/* Initialisation des E/S et du Timer1 */
void approval_init(void) {
    LED_DDR |= _BV(LED_BIT);
    LED_PORT &= ~_BV(LED_BIT); // LED éteinte au démarrage

    tick_count = 0;
    timeout_flag = 0;

    // TODO: configuration du bouton (entrée avec pull-up)

    timer1_init();
}

/* Comportement dans l'ISR lorsque le timeout est atteint :
   - arrêter le toggle de la LED
   - éteindre la LED
*/
static void approval_timeout_isr_handler(void) {
	if (tick_count >= 20) { // 20 * 500 ms = 10 s
        timeout_flag = 1;
        TIMSK1 &= ~_BV(OCIE1A); // désactive l'interruption pour arrêter le toggle
        led_off();              // éteint la LED au timeout
    }
}

/* Accès au timeout depuis le reste du programme */
uint8_t approval_timeout(void) {
    return timeout_flag;
}

/* Réinitialise le timeout */
void approval_timeout_clear(void) {
    cli();
    timeout_flag = 0;
    tick_count = 0;
    TIMSK1 |= _BV(OCIE1A); // réactive l'interruption
    sei();
}

/* Interruption Timer1 CompareA */
ISR(TIMER1_COMPA_vect)
{
	// Si timeout déjà atteint, on ne fait rien
	// TODO: Renvoyer l'erreur
    if (timeout_flag) return; 

    led_toggle();

	// Incrémenter le compteur de ticks
    tick_count++;
    approval_timeout_isr_handler();
}
