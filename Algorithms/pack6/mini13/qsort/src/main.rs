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
    while (first_pos < len) & (slice[first_pos] <= pivot) {
        first_pos += 1;
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
    let len = slice.len();

    if len < 2 {
        return;
    }

    if slice.first() > slice.last() {
        slice.swap(0, len - 1);
    }

    let pivot = slice[0];

    let mut left: usize = 1;
    let mut right: usize = len - 1;

    let pivot_pos = loop {
        while slice[left] <= pivot {
            left += 1;
        }

        while slice[right] > pivot {
            right -= 1;
        }

        if right <= left {
            slice.swap(0, right);
            break right;
        }

        slice.swap(left, right);
    };

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
    while (first_pos < len) & (slice[first_pos] <= pivot) {
        first_pos += 1;
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

fn main() {
    let a = [10, 6, 31, 213, 12, 1, 23123, 12, 123, 32213213, 99999, 54535, 1111];
    let mut a_copy1 = a;
    qsort_hoare(&mut a_copy1);

    println!("{:?}", a_copy1);
    // let mut a_copy2 = a;
    // println!("{:?}", profile!(qsort_lomuto_standart(&mut a_copy1)));
    // println!("{:?}", profile!(qsort_lomuto_branchless(&mut a_copy2)));
}
