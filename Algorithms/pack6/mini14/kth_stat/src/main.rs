fn partition(nums: &mut [i32]) -> usize {
    let len = nums.len();

    if len < 2 {
        return 0;
    }

    let pivot = nums[0];

    let mut first_pos = 1;
    // (first_pos < len) & (nums[first_pos] > pivot) doesn't work smh??
    while nums[first_pos] > pivot {
        first_pos += 1;
        if first_pos >= len {break;};
    }

    for read in (first_pos + 1)..len {
        let x = nums[read];

        let bigger = (nums[read] > pivot) as usize;
        let delta = bigger * (read - first_pos);

        nums[first_pos + delta] = nums[first_pos];
        nums[read - delta] = x;

        first_pos += bigger;
    }

    nums.swap(0, first_pos - 1);
    first_pos - 1

}

fn _kth_largest(nums: &mut [i32], k: i32) -> i32 {
    let p_point = partition(nums);
    let p = p_point as i32;

    if p > k - 1 {
        return _kth_largest(
            &mut nums[0..p_point], 
            k
        );
    } else if p < k - 1 {
        let len = nums.len();
        return _kth_largest(
            &mut nums[(p_point + 1)..len], 
            k - (p + 1)
        );
    } else {
        return nums[p_point];
    }
}

pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
    let mut copy = nums.clone();
    return _kth_largest(&mut copy, k);
}

fn main() {
    let a = vec![3,2,1,5,6,4];
    println!("{}", find_kth_largest(a, 2));
}