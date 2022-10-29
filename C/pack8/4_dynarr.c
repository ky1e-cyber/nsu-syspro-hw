#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

#define DYN_ARR_MULTIPLIER 2

void nullCheck(void* ptr) {
    if (ptr == NULL) {
        exit(1);
    }
}

void scanArr(int** retArr, size_t* retCap, size_t* retLen) {
    int* arr = (int* )malloc(sizeof(int));
    nullCheck(arr);
    size_t cap = 1;
    size_t len = 0;

    int cur;
    scanf("%d", &cur);

    while (cur != 0) {
        if (cap <= len) {
            cap = (int)(cap * DYN_ARR_MULTIPLIER);
            arr = (int* )realloc(arr, cap * sizeof(int));
            nullCheck(arr);
           
        }
        arr[len++] = cur;
        scanf("%d", &cur);
    }

    *retArr = arr;
    *retCap = cap;
    *retLen = len;
}

void printArr(int* arr, size_t size) {
  for (size_t i = 0; i < size; i++) {
    printf("%d ", *(arr + i));
  }

  printf("\n");
}

int main() {
    size_t len;
    size_t cap;
    int* arr;

    scanArr(&arr, &cap, &len);
    printArr(arr, len);

    return 0;
}