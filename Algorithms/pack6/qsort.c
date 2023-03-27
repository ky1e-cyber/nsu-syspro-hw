#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

void swap_p(int* p1, int* p2) {
    int c = *p1;
    *p1 = *p2;
    *p2 = c;
}

int* qsort_lomuto_naive(int* first, int* last) {
    assert(first <= last);

    if ((last - first) < 2) {
        return first;
    }

    last--;

    if (*first > *last) {
        swap_p(first, last);
    }

    int* pivot_pos = first;
    int pivot = *first;

    printf("pivot: %d\n", pivot);

    do {
        first++;
    } while (*first < pivot);

    assert(first <= last);

    for (int* read = first + 1; read < last; read++) {
        int x = *read;

        if (x < pivot) {
            *read = *first;
            *first = x;
            first++;
        }
    }

    assert(*first >= pivot);
    first--;
    *pivot_pos = *first;
    *first = pivot;
    
    return first;

}

int main() {

    int* arr = (int* ) malloc(sizeof(int) * 5);

    arr[0] = 10;
    arr[1] = 11;
    arr[2] = 32;
    arr[3] = 12;
    arr[4] = 1;

    int* a = qsort_lomuto_naive(arr, arr + 9);

    printf("%zu\n", a - arr);

    return 0;
}