#include <avr/io.h>

int main(void)
{
    DDRD |= _BV(DDD6); // PB3 comme sortie

    // Timer0 Fast PWM, non-inversé
    TCCR0A = _BV(COM0A1) | _BV(WGM01) | _BV(WGM00); 
    TCCR0B = _BV(CS01); // prescaler 8

    OCR0A = 25; // 10% duty cycle

    while(1); // boucle infinie
}
