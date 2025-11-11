#ifndef UART_H
#define UART_H

#include <avr/io.h>
#include <stdint.h>

#define BAUD 9600
#define MYUBRR (F_CPU/16/BAUD - 1)

// Prototypes des fonctions
void UART__init(void);
uint8_t UART__getc(void);
void UART__putc(uint8_t data);

#endif