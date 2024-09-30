

fn grid_traveler(m: i64, n: i64) -> i64 {
    if m == 1 && n == 1 {
        return 1;
    }
    if m == 0 || n == 0 {
        return 0;
    }

    grid_traveler(m - 1, n) + grid_traveler(m, n - 1)
}

fn main(){

    println!("{}", grid_traveler(18, 18))

}