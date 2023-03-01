#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include "merge_sort.h"


void print_array(int* arr, size_t arr_size) {
    printf("[");
    for (size_t i = 0; i < arr_size; i++) 
        printf("%d, ", arr[i]);

    printf("]\n");
}

void run_merge_sort() {
    int buff_size4[4] = {0};
    int buff_size5[5] = {0};
    int buff_size10[10] = {0};
    int buff_size19[19] = {0};

    int arr_size4[4] = {1, 2, 3, 4};
    int arr_size5[5] = {5, 4, 3, 2, 1};
    int arr_size10[10] = {1, 22, 27, 34, 59, 84, 49, 63, 94, 9};
    int arr_size19[19] = {31, 12, 55, 22, 98, 85, 74, 11, 38, 99, 4, 39, 62, 25, 57, 73, 37, 92, 58};

    int* sorted = merge_sort(arr_size4, 4, buff_size4, 4);
    print_array(sorted, 4);

    sorted = merge_sort(arr_size10, 10, buff_size10, 10);
    print_array(sorted, 10);

    sorted = merge_sort(arr_size19, 19, buff_size19, 19);
    print_array(sorted, 19);
}

int main() {

    run_merge_sort();
    return 0;
}

    