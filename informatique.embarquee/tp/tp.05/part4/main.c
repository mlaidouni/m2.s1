#include <avr/io.h>
#include <util/delay.h>

void adc_init(void)
{
    // Référence = AVcc (5V), entrée ADC0 = PC0
    ADMUX = (1 << REFS0);

    // ADC activé, prescaler = 128 -> 16MHz / 128 = 125kHz
    ADCSRA = (1 << ADEN) | (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
}

uint16_t adc_read(void)
{
    ADCSRA |= (1 << ADSC);         // lancer conversion
    while (ADCSRA & (1 << ADSC));  // attendre la fin
    return ADC;                    // renvoie un entier 0–1023
}

int main(void)
{
    // LED sur PD6 (OC0A)
    DDRD |= (1 << DDD6);

    // PWM Timer0 Fast PWM, non inversé
    TCCR0A = (1 << COM0A1) | (1 << WGM00) | (1 << WGM01);
    TCCR0B = (1 << CS01); // prescaler = 8 (fréquence PWM élevée)

    adc_init();

    while (1)
    {
        uint16_t pot = adc_read();   // 0 à 1023

        // mise à l'échelle vers 0-255
        OCR0A = pot >> 2;            // équivalent à /4

        _delay_ms(10);
    }
}
