#include <avr/io.h>
#include <util/delay.h>

#define BLINK_DELAY_MS 500

/* Note [cours 6, page 36]
On préfère les variable stockées sur 1 octet (uint8_t), 
plutôt que sur plusieurs octets (int -> 2 octets).
*/

const uint8_t pattern[] = {1,0,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0};

void led_on(void) { PORTB |= _BV(PORTB5); }

void led_off(void) { PORTB &= ~_BV(PORTB5); }

int main (void)
{
    DDRB = _BV(DDB5);
    PORTB = 0;

    for(;;) {
		for (int i = 0; i < sizeof(pattern)/sizeof(pattern[0]); i++) {
			if (pattern[i] == 1) led_on();
			else if (pattern[i] == 0) led_off();
			_delay_ms(BLINK_DELAY_MS);
		}   
    }
}
