use std::time;

macro_rules! profile {
    ($($token:tt)+) => { {
        let _now = time::Instant::now();
        $($token)+;
        _now.elapsed()
    }

    };
}

fn qsort_lomuto_standart(slice: &mut [i32]) -> () {

    let len = slice.len();

    if len < 2 {
        return;
    }

    if slice.first() > slice.last() {
        slice.swap(0, len - 1);
    }

    let pivot = slice[0];

    let mut first_pos = 1;
    while slice[first_pos] <= pivot {
        first_pos += 1;
        if first_pos >= len {break;}
    }

    for read in (first_pos + 1)..len {
        if slice[read] <= pivot {
            slice.swap(first_pos, read);
            first_pos += 1;
        }
    }

    slice.swap(0, first_pos - 1);
    qsort_lomuto_standart(&mut slice[0..(first_pos - 1)]);
    qsort_lomuto_standart(&mut slice[first_pos..len]);

    return; 
}

fn qsort_hoare(slice: &mut [i32]) -> () {
    let len =slice.len();

    if len < 2 {
        return;
    }

    if slice.first() > slice.last() {
        slice.swap(0, len - 1);
    }

    let pivot = slice[0];

    let pivot_pos =  {
        let mut left: usize = 1;
        let mut right: usize = len - 1;
        'outer: loop {
            while (slice[left] <= pivot) & (slice[right] >= pivot) {
                if left == right + 1 {
                    break 'outer left;
                }
                left += 1;
                right -= 1;
            }
            //        v  v
            // [1, 2, 3, 4, 5, 6]
            //

            while slice[left] <= pivot {
                

            }

            while slice[right] >= pivot {
                right -= 1;
                if right == 0 {
                    break 'outer 0;
                }
            }

            while slice[left] <= pivot {
                left += 1;
                if left == len {
                    break 'outer len - 1;
                }
            }

            if left > right {
                break right;
            }

            slice.swap(left, right);
        }
    };

    slice.swap(0, pivot_pos);
    qsort_hoare(&mut slice[0..pivot_pos]);
    qsort_hoare(&mut slice[pivot_pos + 1..len]);

}

fn qsort_lomuto_branchless(slice: &mut [i32]) -> () {
    let len = slice.len();

    if len < 2 {
        return;
    }

    if slice.first() > slice.last() {
        slice.swap(0, len - 1);
    }

    let pivot = slice[0];

    let mut first_pos = 1;
    while slice[first_pos] <= pivot {
        first_pos += 1;
        if first_pos >= len {break;}
    }

    for read in (first_pos + 1)..len {
        let x = slice[read];

        let smaller = (slice[read] <= pivot) as usize;
        let delta = smaller * (read - first_pos);

        slice[first_pos + delta] = slice[first_pos];
        slice[read - delta] = x;

        first_pos += smaller;
    }
    slice.swap(0, first_pos - 1);
    qsort_lomuto_branchless(&mut slice[0..(first_pos - 1)]);
    qsort_lomuto_branchless(&mut slice[first_pos..len]);

    return;

}

pub fn sort_array(nums: Vec<i32>) -> Vec<i32> {
    let mut copy = nums.clone();
    qsort_hoare(&mut copy);
    return copy;
}

fn main() {
    let mut v = vec![2, 2, 2, 2, 2, 2, 2, 2, 2];
    qsort_hoare(&mut v);

    println!("{:?}", v);
    // let mut a_copy2 = a;
    // println!("{:?}", profile!(qsort_lomuto_standart(&mut a_copy1)));
    // println!("{:?}", profile!(qsort_lomuto_branchless(&mut a_copy2)));
}
