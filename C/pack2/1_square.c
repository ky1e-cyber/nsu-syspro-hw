#include <stdio.h>
#include <inttypes.h>


int main() {
    uint32_t n = 0;
    scanf("%d", &n);

    for (uint32_t i = 0; i < (n * n); i += n) {
        for (uint32_t j = 0; j < n; j++) {
            printf("%10d\t", i + j);
        }
        printf("\n");
    }

}