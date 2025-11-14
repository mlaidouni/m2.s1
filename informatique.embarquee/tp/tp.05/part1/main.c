#include <avr/io.h>
#include <util/delay.h>
#include "buzzer.h"

int main() {
    buzzer__init();

    while (1) {
        buzzer__play(880);   // Note A5
        _delay_ms(1000);

        buzzer__stop();
        _delay_ms(1000);
    }
}
