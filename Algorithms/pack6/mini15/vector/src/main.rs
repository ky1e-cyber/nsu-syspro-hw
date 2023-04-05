use std::ops::Index;
use std::ptr::{self, NonNull};
use std::alloc::{self, Layout};

struct Vector<T> {
    ptr: NonNull<T>,
    cap: usize,
    len: usize
}

impl<T> Vector<T> {
    pub fn new() -> Self {
        Vector {
            ptr: NonNull::dangling(),
            cap: 0,
            len: 0
        }
    }

    fn realloc(&mut self, new_cap: usize) {
        let new_layout = 
            Layout::array::<T>(new_cap)
                .unwrap();

        assert!(new_layout.size() <= isize::MAX as usize, "Allocation too large");

        let new_ptr = unsafe {
            alloc::realloc(
                self.ptr.as_ptr() as *mut u8, 
                Layout::array::<T>(self.cap).unwrap(), 
                new_layout.size()
            )
        };

        self.ptr = match NonNull::new(new_ptr as *mut T) {
            Some(p) => p,
            None => alloc::handle_alloc_error(new_layout),
        };

        self.cap = new_cap;

    }

    fn grow(&mut self) {

        if self.cap == 0 {
            let layout = Layout::array::<T>(1).unwrap();
            let new_ptr = unsafe {alloc::alloc(layout)};

            self.ptr = match NonNull::new(new_ptr as *mut T) {
                Some(p) => p,
                None => alloc::handle_alloc_error(layout),
            };

            self.cap = 1;
        } else {
            self.realloc(self.cap * 2);
        }
    }

    pub fn append(&mut self, elem: T) {
        if self.len >= self.cap {self.grow();}

        unsafe {
            ptr::write(self.ptr.as_ptr().add(self.len), elem);
        }

        self.len += 1;
    }

    fn raw_pop(&mut self) -> Option<T> {
        if self.len <= 0 {None} else {
            self.len -= 1;

            unsafe {
                Some(ptr::read(self.ptr.as_ptr().add(self.len)))
            }
        }
    }

    pub fn pop(&mut self) -> Option<T> {
        let e = self.raw_pop();
        match e {
            Some(_) => {
                if self.len <= (self.cap / 4) {
                    self.realloc(self.cap / 2);
                };
                e
            },
            None => None
        }
    }

    pub fn get(&self, index: usize) -> Option<&T> {
        if index >= self.len {None} else {
            unsafe {
                self.ptr
                    .as_ptr()
                    .add(index)
                    .as_ref()
            }
        }
    }

}

impl<T> Drop for Vector<T> {
    fn drop(&mut self) {
        if self.cap != 0 {
            while let Some(_) = self.raw_pop() { }
            let layout = Layout::array::<T>(self.cap).unwrap();
            unsafe {
                alloc::dealloc(self.ptr.as_ptr() as *mut u8, layout);
            }
        }
    }
}

// Just an unwrap
impl<T> Index<usize> for Vector<T> {
    type Output = T;
    fn index(&self, index: usize) -> &Self::Output {
        self.get(index)
            .unwrap()
    }
}


fn main() {
    let mut v: Vector<i32> = Vector::new();

    for i in 0..10000 {
        v.append(i);
    }
    
    println!("v[0] = {}; v[10] = {}, v[5000] = {}, v[9999] = {}", v[0], v[10], v[5000], v[9999]);
    println!("v.len = {}; v.cap = {}", v.len, v.cap);

    for _ in 0..9000 {
        v.pop();
    }

    println!("v.len = {}; v.cap = {}", v.len, v.cap);
}
