#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

void nullCheck(void* ptr) {
    if (ptr == NULL) {
        exit(1);
    }
}

int** getTriangle(size_t size) {
    int** arr = (int**)malloc(size * sizeof(int*));
    nullCheck(arr);
    for (size_t i = 1; i <= size; i++) {
        arr[i - 1] = (int* )malloc(i * sizeof(int));
        nullCheck(arr[i - 1]);
    }

    return arr;
}

void setPascalTriangle(int** arr, size_t size) {
    for (size_t i = 0; i < size; i++) {
        arr[i][0] = 1;
        arr[i][i] = 1;
        for (size_t j = 1; j < i; j++) {
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j];
        }
    } 
}

void printTriangle(int** arr, size_t size) {
    for (size_t i = 0; i < size; i++) {
        for (size_t j = 0; j <= i; j++) {
            printf("%d ", arr[i][j]);
        }

        printf("\n");
    }
}
int main() {
    size_t n;
    scanf("%zu", &n);

    int** arr = getTriangle(n);

    setPascalTriangle(arr, n);
    printTriangle(arr, n);

    return 0;
}