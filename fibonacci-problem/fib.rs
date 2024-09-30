

fn fib(n: i32) -> i32{
    if n <= 1 {
        return 1;
    }

    fib(n - 2) + fib(n - 1)
}


fn main(){

    let n: i32 = 41;

    println!("{}", fib(n));
}