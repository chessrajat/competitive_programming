#![allow(unused)]

use core::num;

pub fn hello() {
    println!("Hello, World!")
}

// Assembly Line

pub fn production_rate_per_hour(speed: u8) -> f64 {
    let unit_speed:f64= 221.0;
    let mut current_speed:f64;
    if ((1..5).contains(&speed)){
        current_speed = speed as f64 * unit_speed;
    }else if ((5..9).contains(&speed)) {
        current_speed = speed as f64 * (unit_speed * 0.9);
    }else{
        current_speed = speed as f64 * (unit_speed * 0.77);
    }
    return current_speed;
    
}

pub fn working_items_per_minute(speed: u8) -> u32 {
    let total_cars = production_rate_per_hour(speed);
    let cars_per_minute = total_cars/60.0;
    return cars_per_minute as u32;
}

// Cooking

pub fn expected_minutes_in_oven() -> i32 {
    return 40;
}

pub fn remaining_minutes_in_oven(actual_minutes_in_oven: i32) -> i32 {
    let remaining_time = expected_minutes_in_oven() - actual_minutes_in_oven;
    return remaining_time;
}

pub fn preparation_time_in_minutes(number_of_layers: i32) -> i32 {
    let preparation_time = number_of_layers * 2;
    return preparation_time;
}

pub fn elapsed_time_in_minutes(number_of_layers: i32, actual_minutes_in_oven: i32) -> i32 {
    let total_time = (number_of_layers * 2) + actual_minutes_in_oven;
    return total_time;
}
