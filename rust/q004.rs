
fn palindrome(number: u64) -> u64 {
    let mut n = number;
    let mut reversed = 0;
    while n > 0 {
        let digit = n % 10;
        reversed = reversed * 10 + digit;
        n /= 10;
    }
    reversed
}

fn main(){
    let mut ans = 0;
    for i in 100..1000{
        for j in 100..1000{
            let product = i*j;
            let pal = palindrome(product);
            if product == pal && pal > ans{
                ans = pal;
            }
        }
    }
    println!("{}", ans)
}