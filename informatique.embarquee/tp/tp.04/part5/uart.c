#include <avr/io.h>
#include <avr/interrupt.h>
#include "uart.h"
#include "ring_buffer.h"

#define RX_BUFFER_SIZE 64
#define TX_BUFFER_SIZE 64

static struct ring_buffer rx_buffer;
static struct ring_buffer tx_buffer;
static uint8_t rx_data[RX_BUFFER_SIZE];
static uint8_t tx_data[TX_BUFFER_SIZE];

void UART__init(void) {
    uint16_t ubrr = MYUBRR;
    UBRR0H = (uint8_t)(ubrr >> 8);
    UBRR0L = (uint8_t)ubrr;

    ring_buffer__init(&rx_buffer, rx_data, RX_BUFFER_SIZE);
    ring_buffer__init(&tx_buffer, tx_data, TX_BUFFER_SIZE);

    UCSR0B = (1 << RXEN0) | (1 << TXEN0) | (1 << RXCIE0); // Active RX/TX + interruption
    UCSR0C = (1 << UCSZ01) | (1 << UCSZ00);

    sei();
}

// ----- Réception -----
ISR(USART_RX_vect) {
    uint8_t data = UDR0; // lit la donnée reçue
    ring_buffer__push(&rx_buffer, data); // la stocke
}

uint8_t UART__getc(void) {
    uint8_t data;
    if (ring_buffer__pop(&rx_buffer, &data)) return data;
    return 0; // rien à lire (valeure par défaut)
}

// ----- Transmission -----

ISR(USART_UDRE_vect) {
    uint8_t data;
    if (ring_buffer__pop(&tx_buffer, &data)) {
        UDR0 = data; // envoie le prochain octet
    } else {
        UCSR0B &= ~(1 << UDRIE0); // plus rien à envoyer → désactive l’interruption
    }
}

void UART__putc(uint8_t data) {
    ring_buffer__push(&tx_buffer, data);
    UCSR0B |= (1 << UDRIE0); // active l’interruption Data Register Empty
}
