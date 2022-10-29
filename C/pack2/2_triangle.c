#include <stdio.h>
#include <inttypes.h>

int main() {
    uint32_t n = 0;
    scanf("%d", &n);
    uint32_t k = 1;
    for (uint32_t i = 0; i <= (((n * (n + 1)) / 2) - 1); ) {
        for (uint32_t j = 0; j < k; j++) {
            printf("%d", i++);
        }
        printf("\n");
        k++;

    }
    return 0;
}