fn is_prime(n: u32) ->bool{
    let lim = (n as f32).sqrt() as u32;
    if n==2{
        return true;
    }
    if n%2==0{
        return false;
    }
    for i in 3..lim+1{
        if n%i==0{
            return false;
        }
    }
    return true;
}

fn main(){
    let mut count=0;
    let mut num=2;
    while count<10001{
        if is_prime(num){
            count+=1;
        }
        num+=1;
    }
    println!("{}", num-1)
}