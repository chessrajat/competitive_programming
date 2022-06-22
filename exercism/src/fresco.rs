use std::io::{self, Read};

pub fn restructured_array() {
    let mut number_of_elements: String = String::new();
    io::stdin().read_line(&mut number_of_elements);
    let number_of_elements = number_of_elements
        .trim()
        .parse()
        .expect("Input not an integer");

    let mut array = vec![vec![0; 0]; 0];
    let mut first = true;
    let mut width: i32 = 0;
    let mut height: i32 = 0;
    let mut i: usize = 0;
    let mut j: usize = 0;

    for num in (0..number_of_elements) {
        let mut input: String = String::new();
        io::stdin().read_line(&mut input);
        let input: i32 = input.trim().parse().expect("Input not an integer");
        if first == true {
            width = input.clone();
            height = (number_of_elements - 1) / width;
            array = vec![vec![0; width as usize]; height as usize];
            first = false;
            continue;
        }

        if i < width as usize {
            array[j][i] = input;
            i += 1;
        } else {
            i = 0;
            j += 1;
            array[j][i] = input;
            i += 1;
        }
    }
    let mut width: String = String::new();
    io::stdin().read_line(&mut width);
    let width: i32 = width.trim().parse().expect("Input not an integer");
    let mut height: String = String::new();
    io::stdin().read_line(&mut height);
    let height: i32 = height.trim().parse().expect("Input not an integer");
   
    for i in (0..width) {
        let mut input: String = String::new();
        io::stdin().read_line(&mut input);
        let vals = input.split(" ").collect::<Vec<&str>>();
        let val1:i32 = vals[0].trim().parse().expect("Input not an integer");
        let val2:i32 = vals[1].trim().parse().expect("Input not an integer");
        let print_val = array[val1 as usize -1][val2 as usize -1];
        println!("{}", print_val);
    }
    
}


//String manipulation

fn main() {
    let mut m: String = String::new();
    io::stdin().read_line(&mut m);
    let m2: i32 = m.trim().parse().expect("Input not an integer");
    for i in 0..m2 {
        let mut useless: String = String::new();
        let mut values: String = String::new();
        io::stdin().read_line(&mut useless);
        io::stdin().read_line(&mut values);
        let mut total_sum: u128 = 0;
        for val in values.split(" ") {
            let mut mul: u128 = 1;
            for v in val.trim().chars() {
                let ord_val = v as u32;
                let real_val: u128 = (ord_val * ord_val) as u128;
                mul = mul * real_val;
                println!("{}", &mul);
            }

            total_sum += mul;
        }
        println!("{}", total_sum);
    }
}
