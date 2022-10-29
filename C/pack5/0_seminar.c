#include <stdio.h>
#include <math.h>
#include <assert.h>

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

void runAutoTests() {
  int a[5] = {5, 4, 3, 2, 1};
  int sa[4] = {5, 4, 3, 2};

  /// revertArr
  int a0[5] = {1, 2, 3, 4, 5};
  int sa0[4] = {2, 3, 4, 5}; 

  revertArr(a0, 5);

  for (size_t i = 0; i < 5; i++) {
    assert(a0[i] == a[i]);
  }

  revertArr(sa0, 4);

  for (size_t i = 0; i < 4; i++) {
    assert(sa0[i] == sa[i]);
  }

  printf("revertArr tests passed!\n");
  /// 

  /// maxInArr
  assert(maxInArr(a, 5) == 5);

  printf("maxInArr tests passed!\n");
  ///

  /// findInArr
  assert(findInArr(a, 5, 3) == 2);
  assert(findInArr(a, 5, 10) == -1);
  printf("findInArr tests passed!\n");
  ///
  
  /// extractDigits
  int b[11];

  extractDigits(b, 11, 45234);

  int digits[] = {4, 5, 2, 3, 4};

  for (size_t i = 0; i < 5; i++) {
    assert(b[i] == digits[i]);
  }
  printf("extractDigits tests passed!\n");
  ///
  
  /// compareArrays
  int c0[] = {5, 8, 0, 2};
  int c1[] = {2, 2, 4, 0};
  int c3[] = {28, 4};
  assert(compareArrays(c0, 4, c1, 4) == 1);
  assert(compareArrays(c1, 4, c0, 4) == -1);
  assert(compareArrays(c0, 4, c0, 4) == 0);
  assert(compareArrays(c3, 2, c0, 4) == -1);
  printf("compareArrays tests passed!\n");
  ///

}

int main() {
  // printArr
  int a[] = {9, 10, 4, 5};
  printArr(a, 4);
  //

  // scanArr
  scanArr(a, 4);
  printArr(a, 4);
  //

  runAutoTests();

  return 0;
}
