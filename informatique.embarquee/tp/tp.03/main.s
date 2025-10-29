# 1 "main.c"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "main.c"
# 1 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/io.h" 1 3
# 99 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/io.h" 3
# 1 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/sfr_defs.h" 1 3
# 126 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/sfr_defs.h" 3
# 1 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/inttypes.h" 1 3
# 37 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/inttypes.h" 3
# 1 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/lib/avr-gcc/9/gcc/avr/9.4.0/include/stdint.h" 1 3 4
# 9 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/lib/avr-gcc/9/gcc/avr/9.4.0/include/stdint.h" 3 4
# 1 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/stdint.h" 1 3 4
# 125 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/stdint.h" 3 4

# 125 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/stdint.h" 3 4
typedef signed int int8_t __attribute__((__mode__(__QI__)));
typedef unsigned int uint8_t __attribute__((__mode__(__QI__)));
typedef signed int int16_t __attribute__ ((__mode__ (__HI__)));
typedef unsigned int uint16_t __attribute__ ((__mode__ (__HI__)));
typedef signed int int32_t __attribute__ ((__mode__ (__SI__)));
typedef unsigned int uint32_t __attribute__ ((__mode__ (__SI__)));

typedef signed int int64_t __attribute__((__mode__(__DI__)));
typedef unsigned int uint64_t __attribute__((__mode__(__DI__)));
# 146 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/stdint.h" 3 4
typedef int16_t intptr_t;




typedef uint16_t uintptr_t;
# 163 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/stdint.h" 3 4
typedef int8_t int_least8_t;




typedef uint8_t uint_least8_t;




typedef int16_t int_least16_t;




typedef uint16_t uint_least16_t;




typedef int32_t int_least32_t;




typedef uint32_t uint_least32_t;







typedef int64_t int_least64_t;






typedef uint64_t uint_least64_t;
# 217 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/stdint.h" 3 4
typedef int8_t int_fast8_t;




typedef uint8_t uint_fast8_t;




typedef int16_t int_fast16_t;




typedef uint16_t uint_fast16_t;




typedef int32_t int_fast32_t;




typedef uint32_t uint_fast32_t;







typedef int64_t int_fast64_t;






typedef uint64_t uint_fast64_t;
# 277 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/stdint.h" 3 4
typedef int64_t intmax_t;




typedef uint64_t uintmax_t;
# 10 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/lib/avr-gcc/9/gcc/avr/9.4.0/include/stdint.h" 2 3 4
# 38 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/inttypes.h" 2 3
# 77 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/inttypes.h" 3
typedef int32_t int_farptr_t;



typedef uint32_t uint_farptr_t;
# 127 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/sfr_defs.h" 2 3
# 100 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/io.h" 2 3
# 252 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/io.h" 3
# 1 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/iom328p.h" 1 3
# 253 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/io.h" 2 3
# 585 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/io.h" 3
# 1 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/portpins.h" 1 3
# 586 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/io.h" 2 3

# 1 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/common.h" 1 3
# 588 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/io.h" 2 3

# 1 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/version.h" 1 3
# 590 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/io.h" 2 3






# 1 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/fuse.h" 1 3
# 239 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/fuse.h" 3
typedef struct
{
    unsigned char low;
    unsigned char high;
    unsigned char extended;
} __fuse_t;
# 597 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/io.h" 2 3


# 1 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/lock.h" 1 3
# 600 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/avr/io.h" 2 3
# 2 "main.c" 2
# 1 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/util/delay.h" 1 3
# 45 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/util/delay.h" 3
# 1 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/util/delay_basic.h" 1 3
# 40 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/util/delay_basic.h" 3
static __inline__ void _delay_loop_1(uint8_t __count) __attribute__((__always_inline__));
static __inline__ void _delay_loop_2(uint16_t __count) __attribute__((__always_inline__));
# 80 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/util/delay_basic.h" 3
void
_delay_loop_1(uint8_t __count)
{
 __asm__ volatile (
  "1: dec %0" "\n\t"
  "brne 1b"
  : "=r" (__count)
  : "0" (__count)
 );
}
# 102 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/util/delay_basic.h" 3
void
_delay_loop_2(uint16_t __count)
{
 __asm__ volatile (
  "1: sbiw %0,1" "\n\t"
  "brne 1b"
  : "=w" (__count)
  : "0" (__count)
 );
}
# 46 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/util/delay.h" 2 3
# 1 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/math.h" 1 3
# 144 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/math.h" 3
__attribute__((__const__)) extern float cosf (float __x);
__attribute__((__const__)) extern double cos (double __x) __asm("cosf");




__attribute__((__const__)) extern float sinf (float __x);
__attribute__((__const__)) extern double sin (double __x) __asm("sinf");




__attribute__((__const__)) extern float tanf (float __x);
__attribute__((__const__)) extern double tan (double __x) __asm("tanf");





static inline float fabsf (float __x)
{
    return __builtin_fabsf (__x);
}

static inline double fabs (double __x)
{
    return __builtin_fabs (__x);
}





__attribute__((__const__)) extern float fmodf (float __x, float __y);
__attribute__((__const__)) extern double fmod (double __x, double __y) __asm("fmodf");
# 192 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/math.h" 3
extern float modff (float __x, float *__iptr);


extern double modf (double __x, double *__iptr) __asm("modff");




__attribute__((__const__)) extern float sqrtf (float __x);


__attribute__((__const__)) extern double sqrt (double __x) __asm("sqrtf");




__attribute__((__const__)) extern float cbrtf (float __x);
__attribute__((__const__)) extern double cbrt (double __x) __asm("cbrtf");
# 219 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/math.h" 3
__attribute__((__const__)) extern float hypotf (float __x, float __y);
__attribute__((__const__)) extern double hypot (double __x, double __y) __asm("hypotf");






__attribute__((__const__)) extern float squaref (float __x);
__attribute__((__const__)) extern double square (double __x) __asm("squaref");





__attribute__((__const__)) extern float floorf (float __x);
__attribute__((__const__)) extern double floor (double __x) __asm("floorf");





__attribute__((__const__)) extern float ceilf (float __x);
__attribute__((__const__)) extern double ceil (double __x) __asm("ceilf");
# 259 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/math.h" 3
__attribute__((__const__)) extern float frexpf (float __x, int *__pexp);
__attribute__((__const__)) extern double frexp (double __x, int *__pexp) __asm("frexpf");






__attribute__((__const__)) extern float ldexpf (float __x, int __exp);
__attribute__((__const__)) extern double ldexp (double __x, int __exp) __asm("ldexpf");




__attribute__((__const__)) extern float expf (float __x);
__attribute__((__const__)) extern double exp (double __x) __asm("expf");




__attribute__((__const__)) extern float coshf (float __x);
__attribute__((__const__)) extern double cosh (double __x) __asm("coshf");




__attribute__((__const__)) extern float sinhf (float __x);
__attribute__((__const__)) extern double sinh (double __x) __asm("sinhf");




__attribute__((__const__)) extern float tanhf (float __x);
__attribute__((__const__)) extern double tanh (double __x) __asm("tanhf");






__attribute__((__const__)) extern float acosf (float __x);
__attribute__((__const__)) extern double acos (double __x) __asm("acosf");






__attribute__((__const__)) extern float asinf (float __x);
__attribute__((__const__)) extern double asin (double __x) __asm("asinf");





__attribute__((__const__)) extern float atanf (float __x);
__attribute__((__const__)) extern double atan (double __x) __asm("atanf");







__attribute__((__const__)) extern float atan2f (float __y, float __x);
__attribute__((__const__)) extern double atan2 (double __y, double __x) __asm("atan2f");




__attribute__((__const__)) extern float logf (float __x);
__attribute__((__const__)) extern double log (double __x) __asm("logf");




__attribute__((__const__)) extern float log10f (float __x);
__attribute__((__const__)) extern double log10 (double __x) __asm("log10f");




__attribute__((__const__)) extern float powf (float __x, float __y);
__attribute__((__const__)) extern double pow (double __x, double __y) __asm("powf");





__attribute__((__const__)) extern int isnanf (float __x);
__attribute__((__const__)) extern int isnan (double __x) __asm("isnanf");
# 358 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/math.h" 3
__attribute__((__const__)) extern int isinff (float __x);
__attribute__((__const__)) extern int isinf (double __x) __asm("isinff");





__attribute__((__const__)) static inline int isfinitef (float __x)
{
    unsigned char __exp;
    __asm__ (
 "mov	%0, %C1		\n\t"
 "lsl	%0		\n\t"
 "mov	%0, %D1		\n\t"
 "rol	%0		"
 : "=r" (__exp)
 : "r" (__x) );
    return __exp != 0xff;
}


static inline int isfinite (double __x)
{
    return isfinitef (__x);
}






__attribute__((__const__)) static inline float copysignf (float __x, float __y)
{
    __asm__ (
 "bst	%D2, 7	\n\t"
 "bld	%D0, 7	"
 : "=r" (__x)
 : "0" (__x), "r" (__y) );
    return __x;
}

__attribute__((__const__)) static inline double copysign (double __x, double __y)
{
    __asm__ (
 "bst	%r1+%2-1, 7" "\n\t"
 "bld	%r0+%2-1, 7"
 : "+r" (__x)
 : "r" (__y), "n" (4));
    return __x;
}
# 416 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/math.h" 3
__attribute__((__const__)) extern int signbitf (float __x);
__attribute__((__const__)) extern int signbit (double __x) __asm("signbitf");





__attribute__((__const__)) extern float fdimf (float __x, float __y);
__attribute__((__const__)) extern double fdim (double __x, double __y) __asm("fdimf");







__attribute__((__const__)) extern float fmaf (float __x, float __y, float __z);
__attribute__((__const__)) extern double fma (double __x, double __y, double __z) __asm("fmaf");






__attribute__((__const__)) extern float fmaxf (float __x, float __y);
__attribute__((__const__)) extern double fmax (double __x, double __y) __asm("fmaxf");






__attribute__((__const__)) extern float fminf (float __x, float __y);
__attribute__((__const__)) extern double fmin (double __x, double __y) __asm("fminf");





__attribute__((__const__)) extern float truncf (float __x);
__attribute__((__const__)) extern double trunc (double __x) __asm("truncf");
# 466 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/math.h" 3
__attribute__((__const__)) extern float roundf (float __x);
__attribute__((__const__)) extern double round (double __x) __asm("roundf");
# 479 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/math.h" 3
__attribute__((__const__)) extern long lroundf (float __x);
__attribute__((__const__)) extern long lround (double __x) __asm("lroundf");
# 493 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/math.h" 3
__attribute__((__const__)) extern long lrintf (float __x);
__attribute__((__const__)) extern long lrint (double __x) __asm("lrintf");
# 47 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/util/delay.h" 2 3
# 86 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/util/delay.h" 3
static __inline__ void _delay_us(double __us) __attribute__((__always_inline__));
static __inline__ void _delay_ms(double __ms) __attribute__((__always_inline__));
# 165 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/util/delay.h" 3
void
_delay_ms(double __ms)
{
 double __tmp ;



 uint32_t __ticks_dc;
 extern void __builtin_avr_delay_cycles(unsigned long);
 __tmp = ((
# 174 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/util/delay.h"
          16000000UL
# 174 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/util/delay.h" 3
               ) / 1e3) * __ms;
# 184 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/util/delay.h" 3
  __ticks_dc = (uint32_t)(ceil(fabs(__tmp)));


 __builtin_avr_delay_cycles(__ticks_dc);
# 210 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/util/delay.h" 3
}
# 254 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/util/delay.h" 3
void
_delay_us(double __us)
{
 double __tmp ;



 uint32_t __ticks_dc;
 extern void __builtin_avr_delay_cycles(unsigned long);
 __tmp = ((
# 263 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/util/delay.h"
          16000000UL
# 263 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/util/delay.h" 3
               ) / 1e6) * __us;
# 273 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/util/delay.h" 3
  __ticks_dc = (uint32_t)(ceil(fabs(__tmp)));


 __builtin_avr_delay_cycles(__ticks_dc);
# 300 "/opt/homebrew/Cellar/avr-gcc@9/9.4.0_1/avr/include/util/delay.h" 3
}
# 3 "main.c" 2




# 6 "main.c"
void led_on() {
 
# 7 "main.c" 3
(*(volatile uint8_t *)((0x05) + 0x20)) 
# 7 "main.c"
      |= 
# 7 "main.c" 3
         (1 << (5))
# 7 "main.c"
                    ;
}

void led_off() {
 
# 11 "main.c" 3
(*(volatile uint8_t *)((0x05) + 0x20)) 
# 11 "main.c"
      &= ~
# 11 "main.c" 3
          (1 << (5))
# 11 "main.c"
                     ;
}

int main (void)
{
 int tab[] = {1,0,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0};

    
# 18 "main.c" 3
   (*(volatile uint8_t *)((0x04) + 0x20)) 
# 18 "main.c"
        = 
# 18 "main.c" 3
          (1 << (5))
# 18 "main.c"
                   ;
    
# 19 "main.c" 3
   (*(volatile uint8_t *)((0x05) + 0x20)) 
# 19 "main.c"
         = 0;

    for(;;) {
  for (int i = 0; i < sizeof(tab)/sizeof(tab[0]); i++) {
   if (tab[i] == 1) led_on();
   else if (tab[i] == 0) led_off();
   _delay_ms(500);
  }
    }
}
