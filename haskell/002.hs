fibo n 
    | n <= 2 = n
    | otherwise = fibo (n-1) + fibo (n-2)

main = do
    print $ fibo 10    
