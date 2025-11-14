#include <avr/io.h>
#include <avr/interrupt.h>

#define NB_LEVELS 5

// Tableau des valeurs OCR0A pour différents duty cycles
const uint8_t pwm_levels[NB_LEVELS] = {0, 64, 128, 192, 255};
volatile uint8_t idx = 0;

ISR(TIMER0_OVF_vect) {
    OCR0A = pwm_levels[idx];      // mettre la nouvelle intensité
    idx++;
    if(idx >= NB_LEVELS) idx = 0; // revenir au début
}

int main(void) {
    // LED connectée sur PD6 (OC0A)
    DDRD |= _BV(DDD6);

    // Timer0 en Fast PWM, non-inversé
    TCCR0A = _BV(COM0A1) | _BV(WGM00) | _BV(WGM01);
    TCCR0B = _BV(CS02) | _BV(CS00); // prescaler 1024

    OCR0A = pwm_levels[0]; // valeur initiale

    TIMSK0 = _BV(TOIE0); // activer interruption overflow
    sei();               // activer interruptions globales

    while(1); // boucle principale
}
