fn swap_slice(arr: &mut [i32], ind1: usize, ind2: usize) -> () {
    (arr[ind1], arr[ind2]) = (arr[ind2], arr[ind1]);
}

fn qsort_lomuto_standart(slice: &mut [i32]) -> () {

    let len = slice.len();

    if len < 2 {
        return;
    }

    if slice.first() > slice.last() {
        swap_slice(slice, 0, len - 1);
    }

    let pivot = slice[0];

    let mut first_pos = 1;
    while (first_pos < len) & (slice[first_pos] <= pivot) {
        first_pos += 1;
    }

    for read in (first_pos + 1)..len {
        if slice[read] <= pivot {
            swap_slice(slice, first_pos, read);
            first_pos += 1;
        }
    }

    swap_slice(slice, 0, first_pos - 1);
    qsort_lomuto_standart(&mut slice[0..(first_pos - 1)]);
    qsort_lomuto_standart(&mut slice[first_pos..len]);
    return; 
}

fn main() {
    let mut a = [10, 6, 7, 22, 3, 2, 1];
    qsort_lomuto_standart(&mut a);

    println!("{:?}", a);
}
