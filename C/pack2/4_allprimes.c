#include <stdio.h>
#include <inttypes.h>

int isPrime(uint64_t n) {
    for (uint64_t k = 2; k <= n / 2; k++) {
        if ((n % k) == 0) {
            return 0;
        }
    }
    return 1;
}

int main() {

    uint64_t n = 0;
    scanf("%ld", &n);
    if (n < 2) {
        printf("ERROR: No prime numbers < 2");
        return 1;
    }

    for (uint64_t i = 2; i <= n; i++) {
        if (isPrime(i)) {
            printf("%ld\n ", i);
        }
    }

    return 0;
}