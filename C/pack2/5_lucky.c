#include <stdio.h>
#include <inttypes.h>

uint32_t min(uint32_t a, uint32_t b) {
    return (a > b) ? b : a;
}

uint32_t max(uint32_t a, uint32_t b) {
    return (a > b) ? a : b;
}

int isLucky(uint32_t n) {

    if ((n >= 100000) && (n <= 999999)) {
        uint8_t a = 0;
        uint8_t b = 0;
        b += n % 10;
        b += (n /= 10) % 10;
        b += (n /= 10) % 10;
        n /= 10;
        a += n % 10;
        a += (n /= 10) % 10;
        a += (n /= 10) % 10;
        return a == b;

    }

    return 0;
}

int main() {
    uint32_t r, l = 0;
    scanf("%d", &l);
    scanf("%d", &r);
    

    if (l > r) {
        printf("ERROR: R must be > L");
        return 1;
    }

    l = max(l, 100000);
    r = min(999999, r);

    for (uint32_t i = l; i <= r; i++) {
        if (isLucky(i)) {
            printf("%d\n", i);
        }
    }
    return 0;
}