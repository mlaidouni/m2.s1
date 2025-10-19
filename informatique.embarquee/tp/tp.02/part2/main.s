.text
.global main
.global sleep_500_ms

main:
    ; Initialisation pile (Stack Pointer)
    ldi r16, 0xFF
    out 0x3D, r16
    ldi r16, 0x08
    out 0x3E, r16

    ; LED sur PB5 en sortie
    sbi 0x04, 5

loop:
    sbi 0x05, 5          ; allume la LED
    rcall sleep_500_ms
    cbi 0x05, 5          ; éteint la LED
    rcall sleep_500_ms
    rjmp loop


; --- sleep_500_ms function (≈500 ms using 3-byte downcounter)
sleep_500_ms:
    ; initial counter = 0x1E8480 (~2_000_000 decimal)
    ldi r18, 0x80
    ldi r19, 0x84
    ldi r20, 0x1E
.sleep_loop:
    subi r18, 1
    sbci r19, 0
    sbci r20, 0
    brne .sleep_loop
    ret
