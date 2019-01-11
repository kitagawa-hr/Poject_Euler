fun fibo(n: Int): Int {
    if (n in 1..2) {
        return n
    } else {
        return fibo(n - 1) + fibo(n - 2)
    }
}

fun main() {
    var ans: Long = 0;
    var i = 1;
    while (fibo(i) < 4000000) {
        if (fibo(i) % 2 == 0) {
            ans += i
        }
        i++
    }
    println("${ans}")
}
