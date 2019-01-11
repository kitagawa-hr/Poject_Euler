// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.

fn main() {
    for a in 334..1000 {
        for b in 1..a {
            for c in 1..b {
                if (i32::pow(a, 2) == i32::pow(b, 2) + i32::pow(c, 2)) && (a + b + c == 1000) {
                    println!("{}", a * b * c);
                }
            }
        }
    }
}
