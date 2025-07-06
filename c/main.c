#include "pico/stdlib.h"

int main()
{
    /* Setup. */
    const uint RED_PIN = 4;
    const uint AMBER_PIN = 3;
    const uint GREEN_PIN = 5;

    gpio_init(RED_PIN);
    gpio_set_dir(RED_PIN, GPIO_OUT);
    gpio_init(AMBER_PIN);
    gpio_set_dir(AMBER_PIN, GPIO_OUT);
    gpio_init(GREEN_PIN);
    gpio_set_dir(GREEN_PIN, GPIO_OUT);

    /* Begin by making sure all LEDs are off. */
    gpio_put(RED_PIN, 0);
    gpio_put(AMBER_PIN, 0);
    gpio_put(GREEN_PIN, 0);

    while(true) {
        /* Red. */
        gpio_put(RED_PIN, 1);
        sleep_ms(3000);

        /* Red and amber. */
        gpio_put(AMBER_PIN, 1);
        sleep_ms(1000);

        /* Green. */
        gpio_put(RED_PIN, 0);
        gpio_put(AMBER_PIN, 0);
        gpio_put(GREEN_PIN, 1);
        sleep_ms(5000);

        /* Amber. */
        gpio_put(AMBER_PIN, 1);
        sleep_ms(2000);

        /* Amber off (red comes on at top of loop). */
        gpio_put(AMBER_PIN, 0);
    }

    /* Never reached, keeps compiler happy. */
    return 0;
}
