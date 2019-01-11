fn main() {
    let mut ans: i64 = 2;
    for n in 3..2000000 {
        if is_prime(n) {
            ans += n as i64;
        }
    }
    println!("{}", ans);
}

fn is_prime(num: i32) -> bool {
    if num % 2 == 0 {
        return false;
    }
    let mut i = 3;
    while i32::pow(i, 2) < num + 1 {
        if num % i == 0 {
            return false;
        } else {
            i += 2;
        }
    }
    true
}
