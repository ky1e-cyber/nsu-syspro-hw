#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>
#include <assert.h>

void nullCheck(void* ptr) {
    if (ptr == NULL) {
        exit(1);
    }
}

int* initHeapArr(int* arr, size_t size) {
    int* hArr = (int* )malloc(size * sizeof(int));
    nullCheck(hArr);

    for (size_t i = 0; i < size; i++) {
        hArr[i] = arr[i];
    }

    return hArr;
}

int isEqArray(int* arr1, int* arr2, size_t size) {
    for (size_t i = 0; i < size; i++) {
        if (arr1[i] != arr2[i]) {
            return 0;
        }
    }
    return 1;
}

int findSubArr(int* arr, size_t sizeArr, int* sub, size_t sizeSub) {
    if (sizeSub > sizeArr) {
        return -1;
    }

    for (size_t i = 0; i <= sizeArr - sizeSub; i++) {
        if (isEqArray(arr + i, sub, sizeSub)) {
            return i;
        }    
    }
    
    return -1;
}

void allignArray(int* arr, size_t* arrLen, size_t startInd) {
    size_t localLen = *arrLen;

    if (localLen == 0 || startInd == 0) {
        return;
    }

    if (startInd >= localLen) {
        *arrLen = 0;
        return;
    }

    for (size_t ind = startInd; ind < localLen; ind++) {
        arr[ind - startInd] = arr[ind];
    }

    *arrLen = localLen - startInd;
}

void removeSubArr(int** arr, size_t* lenArr, int* sub, size_t lenSub) {
    size_t newLen = *lenArr;
    int* newArr = *arr;

    if (newLen == 0 || lenSub == 0) {
        return;
    }

    size_t ind = 0;
    while ((newLen >= lenSub) && (ind <= (newLen - lenSub))) {
        if (isEqArray(newArr + ind, sub, lenSub)) {
            size_t sliceLen = newLen - ind;
            allignArray(newArr + ind, &sliceLen, lenSub);
            newLen = ind + sliceLen;
        } else {
            ind++;
        }
    }

    newArr = (int* )realloc(newArr, newLen * sizeof(int));
    nullCheck(newArr);
    *lenArr = newLen;
}

void runTest(int test_number, int** arr, size_t lenArr, int* sub, size_t lenSub, int* res, size_t lenRes) {
    removeSubArr(arr, &lenArr, sub, lenSub);

    int* localArr = *arr;
    assert(lenArr == lenRes);

    for (size_t i = 0; i < lenArr; i++) {
        assert(localArr[i] == res[i]);
    }

    printf("Test %d passed\n", test_number);
}

void runTests() {
    int* arr;
    size_t lenArr;
    int* sub;
    size_t lenSub;
    int* res;
    size_t lenRes;


    // Test 1
    arr = (int []){1, 2, 1, 4, 1};
    lenArr = 5;
    arr = initHeapArr(arr, lenArr);
    sub = (int []){1};
    lenSub = 1;
    res = (int []){2, 4};
    lenRes = 2;
    runTest(1, &arr, lenArr, sub, lenSub, res, lenRes);
    //

    // Test 2
    arr = (int []){0, 1, 2, 3, 1, 2, 4};
    lenArr = 7;
    arr = initHeapArr(arr, lenArr);
    sub = (int []){1, 2};
    lenSub = 2;
    res = (int []){0, 3, 4};
    lenRes = 3;
    runTest(2, &arr, lenArr, sub, lenSub, res, lenRes);
    //

    // Test 3
    arr = (int []){0, 1, 2, 3, 1, 2, 4};
    lenArr = 7;
    arr = initHeapArr(arr, lenArr);
    sub = NULL;
    lenSub = 0;
    res = (int []){0, 1, 2, 3, 1, 2, 4};
    lenRes = 7;
    runTest(3, &arr, lenArr, sub, lenSub, res, lenRes);
    //

}

int main() {
    runTests();
    return 0;
}