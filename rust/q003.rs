fn max_factor(n: i64) ->i64{
    let lim = (n as f64).sqrt() as i64;
    let mut i: i64 = 3; 
    while i <= lim{
        if n % i == 0{
            let m = n/i as i64;
            return max_factor(m);
        }
        i += 2;
    }
    return n;
}
fn main(){
    let num = 600851475143;
    let ans = max_factor(num);
    println!("{}", ans);
}