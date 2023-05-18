use std::time;
use std::env;
use std::fs;

macro_rules! profile {
    ($($token:tt)+) => { {
        let _now = time::Instant::now();
        $($token)+;
        _now.elapsed().as_micros()
    }

    };
}

macro_rules! elapse_geom_mean {
    ($n: expr, $($token:tt)+) => { {
        let mut _mult = 1;
        for _ in 0..($n) {
            _mult *= $($token)+;
        }
        (_mult as f64).powf(1.0 / ($n as f64))
    }      
    };
}

fn parse_string(s: String) -> Vec<i32> {
    let mut res: Vec<i32> = Vec::new();

    for e in s.split(" ") {
        match e.parse::<i32>() {
            Ok(x) => res.push(x),
            Err(_) => ()
        }
    }

    return res;
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

const EXPECT_MSG: &str = "Was expecting 2 arguments";

fn main() {
    let mut arg_iter = env::args();
    arg_iter.next();

    let input_path =
        arg_iter
            .next()
            .expect(EXPECT_MSG);

    let n_iters: usize =
        arg_iter
            .next()
            .expect(EXPECT_MSG)
            .parse()
            .expect("Was expecting integer");
    
    let to_sort =
        parse_string(
            fs::read_to_string(input_path)
                .unwrap()
        );

    let mut unsorted = to_sort.clone();

    let lomuto_standart_elapsed =
        elapse_geom_mean!(
            n_iters,
            profile!(
                qsort_lomuto_standart(&mut unsorted)
            )
        );

    unsorted = to_sort.clone();

    let lomuto_branchless_eplapsed =
        elapse_geom_mean!(
            n_iters, 
            profile!(
                qsort_lomuto_branchless(&mut unsorted)
            )
        );

    unsorted = to_sort.clone();

    let hoare_eplapsed =
        elapse_geom_mean!(
            n_iters,
            profile!(
                qsort_hoare(&mut unsorted)
            )
        );

    println!(
        "{{\"lomuto_standart\": {0}, \"lomuto_branchless\": {1}, \"hoare\": {2}}}",
        lomuto_standart_elapsed,
        lomuto_branchless_eplapsed,
        hoare_eplapsed
    );
}
