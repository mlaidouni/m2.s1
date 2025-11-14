#ifndef BUZZER_H
#define BUZZER_H

#include <stdint.h>

void buzzer__init(void);
void buzzer__play(int16_t freq);
void buzzer__stop(void);

#endif