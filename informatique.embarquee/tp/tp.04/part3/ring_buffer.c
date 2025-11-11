#include "ring_buffer.h"
#include <util/atomic.h> // pour ATOMIC_BLOCK (sections critiques atomiques)

void ring_buffer__init(struct ring_buffer *rb, uint8_t *buffer, uint8_t size) {
    rb->buffer = buffer;
    rb->maxlen = size;
    rb->head = 0;
    rb->tail = 0;
}

void ring_buffer__push(struct ring_buffer *rb, uint8_t data) {
    uint8_t next = rb->head + 1;
    if (next >= rb->maxlen) next = 0; // On a fait le tour

    if (next == rb->tail) {  // buffer plein → écrasement
        uint8_t new_tail = rb->tail + 1;
        if (new_tail >= rb->maxlen) new_tail = 0;
        rb->tail = new_tail;
    }

    rb->buffer[rb->head] = data;
    rb->head = next;
}

uint8_t ring_buffer__pop(struct ring_buffer *rb, uint8_t *data) {
    uint8_t is_empty;

    ATOMIC_BLOCK(ATOMIC_RESTORESTATE) { // Désactive temporairement les interruptions
        is_empty = (rb->head == rb->tail);
    }

    if (is_empty) return 0; // vide

    *data = rb->buffer[rb->tail];

    ATOMIC_BLOCK(ATOMIC_RESTORESTATE) {
        uint8_t next = rb->tail + 1;
        if (next >= rb->maxlen) next = 0;
        rb->tail = next;
    }

    return 1;
}
