#ifndef RING_BUFFER_H
#define RING_BUFFER_H

#include <stdint.h>

// Buffer circulaire
struct ring_buffer {
    uint8_t *buffer;
    volatile uint8_t head; // index d'écriture
    volatile uint8_t tail; // index de lecture
    uint8_t maxlen; // taille du tableau
};

void ring_buffer__init(struct ring_buffer *rb, uint8_t *buffer, uint8_t size);
void ring_buffer__push(struct ring_buffer *rb, uint8_t data); // appelé depuis ISR
uint8_t ring_buffer__pop(struct ring_buffer *rb, uint8_t *data); // appelé depuis le thread principal

#endif