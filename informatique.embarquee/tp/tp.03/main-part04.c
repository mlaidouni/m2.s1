#include <avr/io.h>        
#include <avr/interrupt.h> 
#include <avr/sleep.h>     
#include <avr/wdt.h>


const uint8_t pattern[] = {1,0,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0  };
volatile uint8_t pattern_idx = 0;

void led_on(void)  { PORTB |= _BV(PORTB5); }   // Met le bit PB5 à 1 → LED allumée
void led_off(void) { PORTB &= ~_BV(PORTB5); }  // Met le bit PB5 à 0 → LED éteinte

ISR(WDT_vect)
{
    if (pattern[pattern_idx])
        led_on();
    else
        led_off();

    pattern_idx++;

    // Si on atteint la fin du tableau, on revient au début (motif en boucle)
    if (pattern_idx >= (sizeof(pattern) / sizeof(pattern[0])))
        pattern_idx = 0;
}

void WDT_Init(void)
{
    cli();  // Désactive les interruptions globales pendant la configuration

    MCUSR &= ~(1 << WDRF);  // Efface le flag de reset Watchdog (au cas où il a été déclenché précédemment)

    // Autorise la modification du registre WDTCSR pendant 4 cycles d’horloge
    WDTCSR |= (1 << WDCE) | (1 << WDE);

    /*
     * Configuration du registre WDTCSR :
     * - WDIE : active les interruptions du WDT (au lieu d’un reset)
     * - WDP2 + WDP0 : définit le prescaler pour une période ≈ 500 ms
     */
    WDTCSR = (1 << WDIE) | (1 << WDP2) | (1 << WDP0);

    sei();  // Réactive les interruptions globales
}

int main(void)
{
    DDRB = _BV(DDB5);
    PORTB = 0;  

    //Désactivation des modules inutilisés pour économiser de l’énergie
     
    PRR = _BV(PRADC) | _BV(PRUSART0) | _BV(PRSPI) | _BV(PRTWI);

    // Initialisation du Watchdog Timer
    WDT_Init();

    /*
     * Configuration du mode de sommeil :
     * SLEEP_MODE_IDLE → mode léger, le CPU dort mais les interruptions et les E/S restent actives.
     * (SLEEP_MODE_PWR_DOWN désactiverait trop de modules, la LED ne changerait pas d’état.)
     */
    set_sleep_mode(SLEEP_MODE_IDLE);

    while (1)
    {
        sleep_mode();  // Endort le MCU, réveillé par ISR(WDT_vect)
    }
}