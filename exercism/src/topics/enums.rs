
// Sublist

use std::fmt::Debug;

pub enum Comparison {
    Equal,
    Sublist,
    Superlist,
    Unequal,
}



pub fn sublist<T: PartialEq>(_first_list: &[T], _second_list: &[T]) -> Comparison {
    if(_first_list.len() == _second_list.len()){
        print!("We are equal");
        for val in [1,2]{
            
        }
    }
    return Comparison::Equal;
}