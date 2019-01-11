fn fibo(x: i32) -> i32 {
    if x == 1 || x == 2 {
        x
    } else {
        fibo(x - 1) + fibo(x - 2)
    }
}

fn main() {
    let mut x: i32 = 1;
    let mut ans: i32 = 0;
    let mut f: i32 = 0;
    while f <= 4000000 {
        f = fibo(x);
        x += 1;
        if f % 2 == 0 {
            ans += f;
        }
    }

    println!("{}", ans)
}
