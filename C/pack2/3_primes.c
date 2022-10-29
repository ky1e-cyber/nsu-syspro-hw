#include <stdio.h>
#include <inttypes.h>

int main() {

    uint64_t n = 0;
    scanf("%ld", &n);
    if (n < 2) {
        printf("ERROR: No prime numbers < 2");
        return 1;
    }

    for (uint64_t k = 2; k <= n / 2; k++) {
        if ((n % k) == 0) {
            printf("is not prime\n");
            return 0;
        }
    }

    printf("is prime\n");
    return 0;
}