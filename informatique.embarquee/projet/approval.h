#ifndef APPROVAL_H
#define APPROVAL_H

#include <stdint.h>

/* Pin mapping for ATmega328P
 * LED on D10 -> PB2
 * BUTTON on D2 -> PD2 (active LOW with internal pull-up)
 */

#define LED_PORT    PORTB
#define LED_DDR     DDRB
#define LED_PIN_REG PINB
#define LED_BIT     PB2

#define BUTTON_PORT    PORTD
#define BUTTON_DDR     DDRD
#define BUTTON_PIN_REG PIND
#define BUTTON_BIT     PD2

#define BUTTON_PRESSED 0

void approval_init(void);

#endif
