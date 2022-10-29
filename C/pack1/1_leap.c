#include <stdio.h>
#include <inttypes.h>

int main() {
    uint32_t year = 0;
    scanf("%d", &year);
    if ((year % 400 == 0) || ((year % 4 == 0 && year % 100 == 0))) {
        printf("Leap\n");
    } else {
        printf("Is not Leap\n");
    }
    return 0;
}