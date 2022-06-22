#![allow(unused)]
use std::vec;

// A short fibonnaci sequence

pub fn create_empty() -> Vec<u8> {
    vec![]
}

pub fn create_buffer(count: usize) -> Vec<u8> {
    return vec![0;count];
}

pub fn fibonacci() -> Vec<u8> {
    let count = 5;
    let mut my_buffer = create_buffer(count);
    for i in (0..count){
        if i == 0{
            my_buffer[i] = 1;
        }else if i == 1 {
            my_buffer[i] = 1;
        }else{
            my_buffer[i] = my_buffer[i-1] + my_buffer[i-2];
        }
    }
    return my_buffer;
}