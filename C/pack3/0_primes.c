#include <stdio.h>
#include <inttypes.h>
#include <assert.h>

int isPrime(int n) {
    assert(n >= 2);
    for (int k = 2; k <= n / 2; k++) {
        if ((n % k) == 0) {
            return 0;
        }
    }
    return 1;
}

int main() {

    int n = 0;
    scanf("%d", &n);
    if (n < 2) {
        printf("ERROR: No prime numbers < 2");
        return 1;
    }

    for (int i = 2; i <= n; i++) {
        if (isPrime(i)) {
            printf("%d ", i);
        }
    }

    printf("\n");

    return 0;
}