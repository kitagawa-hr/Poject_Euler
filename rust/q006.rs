fn main() {
    let mut sum1: i32 = 0;
    let mut sum2: i32 = 0;
    for i in 1..101 {
        sum1 += i;
        sum2 += i.pow(2);
    }
    let ans = sum1.pow(2) - sum2;
    println!("{}", ans)
}
