#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>
#include <math.h>
#include <assert.h>

void nullCheck(void* ptr) {
  if (ptr == NULL) {
    exit(1);
  }
}

int max(int a, int b) {
  return a > b ? a : b;
}

int countDigits(int a) {
  return ((int)log10f(fabs((float)a) + 0.5f)) + 1;
}

void swap(int* a, int* b) {
  int c = *a;
  *a = *b;
  *b = c;
}

void scanArr(int* arr, size_t size) {
  for (size_t i = 0; i < size; i++) {
    scanf("%d", arr + i);
  }
}

void printArr(int* arr, size_t size) {
  for (size_t i = 0; i < size; i++) {
    printf("%d ", *(arr + i));
  }

  printf("\n");
}

void revertArr(int* arr, size_t size) {
  for (size_t i = 0; i < (size / 2); i++) {
    swap(arr + size - i - 1, arr + i);
  }
}

int maxInArr(int* arr, size_t size) {
  int max_value = arr[0];

  if (size == 1) {
    return max_value;
  }

  for (size_t i = 1; i < size; i++) {
    max_value = max(max_value, arr[i]);
  }

  return max_value;

}

int findInArr(int* arr, size_t size, int x) {
  for (size_t i = 0; i < size; i++) {
    if (arr[i] == x) {
      return i;
    }

  }

  return -1;
}

void extractDigits(int *arr, size_t size, int x) {
  int len = countDigits(x);
  
  assert(len <= size);

  for (int i = (len - 1); i >= 0; i--) { // segfault if i is size_t (C moment)
    arr[i] = x % 10;
    x /= 10;
  }

  
}

int compareArrays(int *arr1, size_t size1, int* arr2, size_t size2) {
  if (size1 != size2) {
    return size1 < size2 ? -1 : 1;  
  }

  for (size_t i = 0; i < size1; i++) {
    if (arr1[i] > arr2[i]) {
      return 1;
    }

    if (arr1[i] < arr2[i]) {
      return -1;
    }
  }

  return 0;
}

void runTest(int* arr, size_t n) {
    scanArr(arr, n);
    printf("printArr:\n");
    printArr(arr, n);
    
    revertArr(arr, n);
    printf("revertArr:\n");
    printArr(arr, n);

    printf("maxInArr: %d\n", maxInArr(arr, n));

    printf("findInArr(5): %d\n", findInArr(arr, n, 5));

    extractDigits(arr, n, 123);
    printf("extractDigits(123):\n");
    printArr(arr, n);

    int arr1[] = {1, 3, 4};
    printf("compareArrays({1, 3, 4}): %d\n", compareArrays(arr, n, arr1, 3));

} 

int main() {
    int n0 = 1;
    scanf("%d", &n0);

    if (n0 < 3) {
        printf("Array size must be >= than 3! (for some tests)\n");
        return 1;
    }

    size_t n = (size_t)n0; 
    int* arr = (int* )malloc(n * sizeof(int));

    nullCheck(arr);

    runTest(arr, n);
    return 0;
}