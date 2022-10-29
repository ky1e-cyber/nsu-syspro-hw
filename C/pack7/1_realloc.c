#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>
#include <assert.h>

void nullCheck(void* ptr) {
  if (ptr == NULL) {
    exit(1);
  }
}

void arrCopy(int* arr_from, int* arr_to, size_t size_from, size_t size_to) {
  assert(size_from <= size_to);

  for (size_t i = 0; i < size_from; i++) {
    arr_to[i] = arr_from[i];
  }

}

int* reallocArr(int* arr, size_t size, size_t newsize) {
  assert(newsize != 0 && size <= newsize);

  int* new_arr = (int*) malloc(newsize * sizeof(int));
  nullCheck(new_arr);

  if (size == 0) {
    free(arr);
    return new_arr;
  }

  arrCopy(arr, new_arr, size, newsize);
  free(arr);
  return new_arr;
}

int main() {
  int cur;
  size_t size = 0;
  int* arr = (int* )malloc(sizeof(int));
  nullCheck(arr);

  scanf("%d", &cur);
  
  while (cur != 0) {
    arr = reallocArr(arr, size, size + 1);
    arr[size] = cur;
    size++;
    scanf("%d", &cur);
  }
  
  for (size_t i = 0; i < size; i++) {
    printf("%d ", arr[i]);
  }

  printf("\n");

  free(arr);
  return 0;
}

