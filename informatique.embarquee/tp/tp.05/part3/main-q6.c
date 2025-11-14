#include <avr/io.h>
#include <avr/interrupt.h>

#define NB_LEVELS 5

const uint8_t pwm_levels[NB_LEVELS] = {0, 64, 128, 192, 255};
volatile int8_t idx = 0; // index actuel
volatile int8_t direction = 1; // 1 = montée, -1 = descente
volatile uint16_t overflow_count = 0;

ISR(TIMER0_OVF_vect) {
    overflow_count++;
    if(overflow_count >= 6) {
        overflow_count = 0;
        OCR0A = pwm_levels[idx];

        // Incrémenter ou décrémenter selon la direction
        idx += direction;

        // Inverser la direction si on atteint un bout
        if(idx >= NB_LEVELS - 1) direction = -1;
        else if(idx <= 0) direction = 1;
    }
}

int main(void) {
    DDRD |= _BV(DDD6); // LED sur PD6

    // Timer0 Fast PWM, non-inversé
    TCCR0A = _BV(COM0A1) | _BV(WGM00) | _BV(WGM01);
    TCCR0B = _BV(CS02) | _BV(CS00); // prescaler 1024

    OCR0A = pwm_levels[0];
    TIMSK0 = _BV(TOIE0); // activer interruption overflow
    sei();

    while(1);
}
