fn max_factor(n: i64){
    let mut lim = sqrt(n);
    let mut i: i32 = 2;
    while (i <= lim){
        if (n%i==0){
            return max_factor(int(n/i));
        }
        i++;
    }
    n
}
fn main(){
    let N = 600851475143;
    println!("{}", max_factor(N));
}