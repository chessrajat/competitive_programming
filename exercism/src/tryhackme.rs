use std::{io::Bytes, ops::Not};
use base64::{decode};
use std::str::from_utf8;

pub fn rust_chal(string: &str) -> String {
    println!("{}", string);
    let mut decrypted = rot13_decrypt(string);
    let b64_decoded = decode(decrypted).unwrap();
    decrypted = rot13_decrypt(from_utf8(&b64_decoded).unwrap());
    return decrypted;
}

fn rot13_decrypt(string: &str) -> String {
    // rot13 decrypt
    let mut output:Vec<char> = Vec::new();
    for char_val in string.chars() {
        if char_val.is_alphabetic() != true{
            output.push(char_val);
            continue;
        }

        let a = if char_val.is_ascii_uppercase() {
            b'A'
        } else {
            b'a'
        };

        let alphabet_pos = char_val as u8 - a;
        let shifted_pos = 
            if alphabet_pos < 13 {
                26 - (13 - alphabet_pos)
            }else{
                alphabet_pos - 13
            };

        let new_pos = shifted_pos + a;

        output.push(new_pos as char);
        
    }
    return output.into_iter().collect();
}
