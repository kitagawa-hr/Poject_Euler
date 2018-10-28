fibo1 0 = 0
fibo1 1 = 1
fibo1 x = fibo1 (x-1) + fibo1 (x-2)

fibo2 n
    | n == 0 = 0
    | n == 1 = 1
    | n>0 = fibo2 (n-2) + fibo2 (n-1)

fibo3 n = case n of
    0 -> 0
    1 -> 1
    _ | n > 0 -> fibo3 (n-2) + fibo3 (n-1)

main = do
    print $ fibo1 6
    print $ fibo2 6
    print $ fibo3 6
