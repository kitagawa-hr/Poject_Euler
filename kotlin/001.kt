fun main() {
    val N: Int = 1000
    var ans: Int = 0
    for (i in 1..N) {
        if (i % 3 == 0) {
            ans += i
        } else if (i % 5 == 0) {
            ans += i
        }
    }
    println(ans)
}

