/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

#define swap(a, b) {    \
    a ^= b;             \
    b ^= a;             \
    a ^= b;             \
}

void merge_sort(int* nums, size_t nums_size, int* buff, size_t buff_size) {

}

int* merge_sort_inplace(int* nums, size_t size) {
    return nums;
}

int* sortArray(int* nums, int numsSize, int* returnSize){

}


