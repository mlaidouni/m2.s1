#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include <stdint.h>

const uint8_t pattern[] = {1,0,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0};

/* Doit être globale volatile pour être utilisée dans l'ISR */
volatile uint8_t pattern_idx = 0;

/* On pilote maintenant PD4 */
void led_on(void)  { PORTD |= _BV(PORTD4); }
void led_off(void) { PORTD &= ~_BV(PORTD4); }

/* Interruption Timer1 CompareA */
ISR(TIMER1_COMPA_vect)
{
    if (pattern[pattern_idx]) led_on();
    else led_off();

    pattern_idx++;
    if (pattern_idx >= sizeof(pattern)/sizeof(pattern[0]))
        pattern_idx = 0;
}

int main (void)
{
    // On configure PD4 comme sortie
    DDRD = _BV(DDD4);
    PORTD = 0; // LED éteinte au départ

    // Désactiver les modules non utilisés pour économiser de l'énergie
    PRR = _BV(PRADC) | _BV(PRUSART0) | _BV(PRSPI) | _BV(PRTWI);

    // Configuration Timer1 en mode CTC, prescaler 256
    TCCR1A = 0;
    TCCR1B = _BV(WGM12) | _BV(CS12);
    OCR1A = 31249; // interruption toutes les 500ms à 16MHz

    // Activation interruption Timer1 CompareA
    TIMSK1 = _BV(OCIE1A);

    // Activation interruptions globales
    sei();

    // Mode sommeil IDLE
    set_sleep_mode(SLEEP_MODE_IDLE);

    // Boucle principale
    for (;;) sleep_mode();
}
