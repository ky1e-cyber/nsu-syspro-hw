#include <inttypes.h>
#include <stdio.h>

int main() {
    uint32_t n = 0;
    scanf("%d", &n);

    for (uint32_t i = 0; i <= n; i++) {
        int f = 0;
        if (i % 3 == 0) {
            printf("fizz ");
            f = 1;
        }
        if (i % 5 == 0) {
            printf("buzz");
            f = 1;
        }
        if (!f) {
            printf("%d", i);
        }
        printf("\n");
        
    }
    return 0;
}