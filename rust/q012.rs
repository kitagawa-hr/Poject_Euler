fn main() {
    let mut i = 1;
    loop {
        let tri: i32 = i * (i + 1) / 2 as i32;
        if divisor_count(tri) > 50 {
            println!("{}", tri);
            break;
        }
        i += 1;
    }
}

fn divisor_count(num: i32) -> i32 {
    let mut count = 0;
    for n in 1..num + 1 {
        if num % n== 0 {
            count += 1;
        }
        if n > num / 2 {
            break;
        }
    }
    count + 1
}

