length' []     = 0
length' (_:xs) = 1 + length' xs

sum' []     = 0
sum' (x:xs) = x + sum' xs

take' n _      | n < 1 = []
take' _ []     = []
take' n (x:xs) = x : take' (n-1)  xs

product' []     = 1
product' (x:xs) = x * product xs


drop' n xs     | n < 1 = xs
drop' _ []     = []
drop' n (x:xs) = drop' (n-1)  xs

reverse' []     = []
reverse' (x:xs) =  reverse' (xs) ++ [x]

fact 0 = 1
fact n = n * fact (n-1)

fact' 0 = 1
fact' n = product [1..n]

perpPoint (p,q) (a,b,c) = (x, y)
    where
        x = (a*b + b*d) / (a*a + b*b)
        y = (b*c - a*d) / (a*a+b*b)
        d = b*p-a*q

main = do
    print $ length [1,2,3,4,5]
    print $ length' [1,2,3,4,5]
    print $ sum [1,2,3,4,5]
    print $ sum' [1,2,3,4,5]
    print $ take 3 [1,2,3,4,5]
    print $ take' 3 [1,2,3,4,5]
    print $ product [1,2,3,4,5]
    print $ product' [1,2,3,4,5]
    print $ drop 3 [1,2,3,4,5]
    print $ drop' 3 [1,2,3,4,5]
    print $ reverse [1,2,3,4,5]
    print $ reverse' [1,2,3,4,5]
    print $ fact 5
    print $ fact' 5
