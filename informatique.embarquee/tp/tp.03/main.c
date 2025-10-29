#include <avr/io.h>
#include <util/delay.h>

#define BLINK_DELAY_MS 500

void led_on() {
	PORTB |= _BV(PORTB5);
}

void led_off() {
	PORTB &= ~_BV(PORTB5);
}

int main (void)
{
	int tab[] = {1,0,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0};

    DDRB = _BV(DDB5);
    PORTB = 0;

    for(;;) {
		for (int i = 0; i < sizeof(tab)/sizeof(tab[0]); i++) {
			if (tab[i] == 1) led_on();
			else if (tab[i] == 0) led_off();
			_delay_ms(BLINK_DELAY_MS);
		}   
    }
}
