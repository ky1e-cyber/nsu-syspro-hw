#include <stdio.h>

void swap(int* a, int* b) {
  int c = *a;
  *a = *b;
  *b = c;
}

void transpose(int arr[4][4]) {
  for (size_t i = 0; i < 4; i++) {
    for (size_t j = i; j < 4; j++) {
      swap(&(arr[i][j]), &(arr[j][i]));
    }
  }

}

void printArr(int arr[4][4]) {
  for (size_t i = 0; i < 4; i++) {
    for (size_t j = 0; j < 4; j++) {
      printf("%d ", arr[i][j]);
    }
    printf("\n");
  }
}

int main() {
  int arr[4][4];

  for (size_t i = 0; i < 4; i++) {
    for (size_t j = 0; j < 4; j++) {
      scanf("%d", &(arr[i][j]));
    }
    printf("\n");
  }
  printf("\n");

  transpose(arr);
  printArr(arr);

  return 0;
}
