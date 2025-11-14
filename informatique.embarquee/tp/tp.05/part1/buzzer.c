#include <avr/io.h>
#include "buzzer.h"

#define F_CPU 16000000UL

void buzzer__init(void) {
    // PB1 = OC1A en sortie
    DDRB |= (1 << PB1);

    // Mode CTC (WGM12 = 1)
    TCCR1A = 0;
    TCCR1B = (1 << WGM12);

    // Désactive OC1A (pas encore de signal)
    TCCR1A &= ~(1 << COM1A0);

    // Prescaler = 8
    TCCR1B |= (1 << CS11);
}

void buzzer__play(int16_t freq) {
    // Active le toggle sur OC1A
    TCCR1A |= (1 << COM1A0);

    // Calcul OCR1A pour fréquence donnée
    uint16_t ocr = (F_CPU / (2 * 8 * freq)) - 1;
    OCR1A = ocr;
}

void buzzer__stop(void) {
    // Désactive le toggle sur OC1A
    TCCR1A &= ~(1 << COM1A0);

    // Met la broche à 0
    PORTB &= ~(1 << PB1);
}
