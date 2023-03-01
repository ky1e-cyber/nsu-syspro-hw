/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include "merge_sort.h"

#define min(a, b) ((a) < (b) ? (a) : (b))



void swap(int* a, int* b) {
    *a ^= *b;
    *b ^= *a;
    *a ^= *b;
}

void merge(int* xs, int* ys, size_t xs_size, size_t ys_size, int* dest, size_t dest_size) {
    assert(dest_size >= (xs_size + ys_size));

    size_t xs_ind = 0;
    size_t ys_ind = 0;
    size_t ind = 0;

    for ( ; ind < min(xs_size, ys_size) ; ind++) {
        swap(dest + ind, xs[xs_ind] < ys[ys_ind] ? (xs + (xs_ind++)) : (ys + (ys_ind++)));
    }

    while (xs_ind < xs_size) 
        swap(dest + (ind++), xs + (xs_ind++));

    while (ys_ind < ys_size)
        swap(dest + (ind++), ys + (ys_ind++));
}

int* merge_sort(int* nums, size_t nums_size, int* dest, size_t dest_size) {
    assert(dest_size >= nums_size);

    if (nums_size <= 1) {
        swap(nums, dest); 
        return dest;
    } 

    if (nums_size == 2) {
        size_t ind_of_less = nums[0] < nums[1] ? 0 : 1;
        swap(nums + ind_of_less, dest);
        swap(nums + (1 - ind_of_less), dest + 1);
        return dest;
    }

    size_t pivot = nums_size / 2;
    size_t ys_size = nums_size - pivot;
    size_t xs_sizes = nums_size - ys_size;

    merge_sort_inplace(nums, pivot, dest, dest_size);
    merge_sort_inplace(nums + pivot, nums_size - pivot, dest, dest_size);

    merge(nums, nums + pivot, pivot, nums_size - pivot, dest, dest_size);
    return dest;
}

int* merge_sort_inplace(int* nums, size_t nums_size, int* buff, size_t buff_size) {
    assert(buff_size >= nums_size);

    if (nums_size <= 1) 
        return nums;

    if ((nums_size == 2) && (nums[0] > nums[1])) 
        swap(nums, nums + 1);


    merge_sort(nums, nums_size, buff, buff_size);

    for (size_t i = 0; i < nums_size; i++) 
        swap(buff + i, nums + i);

    return nums;
}

int* sortArray(int* nums, int numsSize, int* returnSize) {
    int* dest = (int* ) malloc(sizeof(int) * numsSize);
    *returnSize = numsSize;

    if (numsSize <= 1) {
        swap(nums, dest); 
        return dest;
    } 

    if (numsSize == 2) {
        size_t ind_of_less = nums[0] < nums[1] ? 0 : 1;
        swap(nums + ind_of_less, dest);
        swap(nums + (1 - ind_of_less), dest + 1);
        return dest;
    }

    size_t pivot = (numsSize / 2) + (numsSize % 2);

    merge_sort();

    return dest;
}
