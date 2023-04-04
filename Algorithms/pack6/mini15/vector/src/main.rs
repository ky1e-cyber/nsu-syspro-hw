use std::ptr::NonNull;

struct Vector<T> {
    ptr: NonNull<T>,
    cap: usize,
    len: usize
}

impl<T> Vector<T> {
    fn new() -> Self {
        Vector {
            ptr: NonNull::dangling(),
            cap: 0,
            len: 0
        }
    }

    fn append(elem: T) {
        
    }
}

fn main() {
    println!("Hello, world!");
}
