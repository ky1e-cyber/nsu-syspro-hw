#include <stdio.h>

void swap(int* a, int* b) {
    int c = *a;
    *a = *b;
    *b = c;
}

void cursed_swap(int* a, int* b) {
    *a = (*a) ^ (*b);
    *b = (*a) ^ (*b);
    *a = (*a) ^ (*b);
}

int main() {
    int a = 1;
    int b = 2;
    swap(&a, &b);
    printf("%d %d\n", a, b);
    return 0;
}