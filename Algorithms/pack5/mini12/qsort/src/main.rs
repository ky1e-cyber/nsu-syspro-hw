struct Solution {}

fn qsort_lomuto_standart(slice: &mut [i32]) {
    let len = slice.len();

    if len < 2 {return;}

    if slice.first() > slice.last() {
        slice.swap(0, len - 1);
    }

    if len == 2 {return;}

    let pivot = slice[0];

    let mut first = 1;
    let mut are_same = true;

    while slice[first] < pivot {
        are_same = false;
        first += 1;
        
        if first >= len - 1 {
            slice.swap(0, len - 2);
            qsort_lomuto_standart(&mut slice[0..len - 2]);
            return;
        }
    }

    for read in first..(len - 1) {
        if slice[read] < pivot {
            are_same = false;
            slice.swap(first, read);
            first += 1;
        } else if (slice[read] > pivot) {
            are_same = false;
        }
    }

    if are_same {
        return;
    }

    slice.swap(0, first - 1);

    qsort_lomuto_standart(&mut slice[0 ..(first - 1)]);
    qsort_lomuto_standart(&mut slice[first..len]);

}

impl Solution {
    pub fn sort_array(mut nums: Vec<i32>) -> Vec<i32> {
        qsort_lomuto_standart(&mut nums);
        return nums;
    }
}

fn main() {
    let mut v = vec![5,1,1,2,0,0];

    println!("{:?}", Solution::sort_array(v));
}