#include <stdlib.h>

#define min(a, b) (a) < (b) ? (a) : (b)
#define max(a ,b) (a) > (b) ? (a) : (b)

typedef struct {
  int* segmentTree;
  size_t size;
} NumArray;


void segmentTreeBuild(int* tree, int* arr, size_t v, size_t tl, size_t tr) {
  if (tl == tr) {
    tree[v] = arr[tl];
    return;
  }

  size_t tm = (tl + tr) >> 1;

  segmentTreeBuild(tree, arr, v << 1, tl, tm);
  segmentTreeBuild(tree, arr, (v << 1) + 1, tm + 1, tr);

  tree[v] = tree[v << 1] + tree[(v << 1) + 1];
}


void segmentTreeUpdate(int* tree, size_t ind, int value, size_t v, size_t tl, size_t tr) {

  if (tl == tr) {
    tree[v] = value;
    return;
  }

  size_t tm = (tl + tr) >> 1;

  if (ind <= tm) {
    segmentTreeUpdate(tree, ind, value, v << 1, tl, tm);
  } else {
    segmentTreeUpdate(tree, ind, value, (v << 1) + 1, tm + 1, tr);
  }

  tree[v] = tree[v << 1] + tree[(v << 1) + 1];
}

int segmentTreeGetSum(int* tree, size_t v, size_t tl, size_t tr, size_t l, size_t r) {
  if ((tl == l) && (tr == r)) return tree[v];

  size_t tm = (tl + tr) >> 1;

  int res = 0;

  if (l <= tm) 
    res += segmentTreeGetSum(tree, v << 1, tl, tm, l, min(r, tm));
  if (r >= tm + 1) 
    res += segmentTreeGetSum(tree, (v << 1) + 1, tm + 1, tr, max(l, tm + 1), r);

  return res;
}

NumArray* numArrayCreate(int* nums, int numsSize) {
  NumArray* obj = (NumArray*) malloc(sizeof(NumArray));
  
  obj->segmentTree = (int*) malloc(4 * numsSize * sizeof(int));
  obj->size = numsSize;

  segmentTreeBuild(obj->segmentTree, nums, 1, 0, numsSize - 1);

  return obj;
}

void numArrayUpdate(NumArray* obj, int index, int val) {
    segmentTreeUpdate(obj->segmentTree, index, val, 1, 0, (obj->size) - 1);
}

int numArraySumRange(NumArray* obj, int left, int right) {
    return segmentTreeGetSum(obj->segmentTree, 1, 0, (obj->size) - 1, left, right);
}

void numArrayFree(NumArray* obj) {
  free(obj->segmentTree);
  free(obj);
}

/**
 * Your NumArray struct will be instantiated and called as such:
 * NumArray* obj = numArrayCreate(nums, numsSize);
 * numArrayUpdate(obj, index, val);
 
 * int param_2 = numArraySumRange(obj, left, right);
 
 * numArrayFree(obj);
*/
