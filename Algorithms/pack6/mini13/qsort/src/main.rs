use std::time;

macro_rules! profile {
    ($($token:tt)+) => { {
        let _now = time::Instant::now();
        $($token)+;
        _now.elapsed()
    }

    };
}

fn qsort_lomuto_standart(slice: &mut [i32]) {
    let len = slice.len();

    if len < 2 {return;}

    if slice.first() > slice.last() {
        slice.swap(0, len - 1);
    }

    if len == 2 {return;}

    let pivot = slice[0];

    let mut first = 1;

    while slice[first] < pivot {
        first += 1;

        if first >= len - 1 {
            slice.swap(0, len - 2);
            qsort_lomuto_standart(&mut slice[0..len - 2]);
            return;
        }
    }

    for read in first..(len - 1) {
        if slice[read] < pivot {
            slice.swap(first, read);
            first += 1;
        }
    }

    slice.swap(0, first - 1);

    qsort_lomuto_standart(&mut slice[0 ..(first - 1)]);
    qsort_lomuto_standart(&mut slice[first..len]);

}

fn qsort_hoare(slice: &mut [i32]) -> () {
    let len = slice.len();

    if len < 2 {return;}

    if slice.first() > slice.last() {
        slice.swap(0, len - 1);
    }

    if len == 2 {return;}

    let pivot = slice[0];

    let pivot_pos =  {

        let mut left: usize = 1;
        let mut right: usize = len - 2;

        'outer: loop {
            while slice[right] >= pivot {
                right -= 1;
                if right == 0 {
                    break 'outer 0;
                }
            }

            while slice[left] < pivot {
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
    qsort_hoare(&mut slice[(pivot_pos + 1)..len]);

}


fn qsort_lomuto_branchless(slice: &mut [i32]) {
    let len = slice.len();

    if len < 2 {return;}

    if slice.first() > slice.last() {
        slice.swap(0, len - 1);
    }

    if len == 2 {return;}

    let pivot = slice[0];

    let mut first = 1;

    while slice[first] < pivot {
        first += 1;

        if first >= len - 1 {
            slice.swap(0, len - 2);
            qsort_lomuto_branchless(&mut slice[0..len - 2]);
            return;
        }
    }

    for read in first..(len - 1) {
        let x = slice[read];

        let smaller = -((slice[read] < pivot) as isize);
        let delta = (smaller as usize) & (read - first);

        slice[first + delta] = slice[first];
        slice[read - delta] = x;

        first += (-smaller) as usize;
    }
    slice.swap(0, first - 1);
    qsort_lomuto_branchless(&mut slice[0..(first - 1)]);
    qsort_lomuto_branchless(&mut slice[first..len]);

}


fn main() {
    println!("Hello, World");
}
