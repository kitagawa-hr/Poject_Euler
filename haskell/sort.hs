insert x [] = [x]
insert y (x:xs)
    | y<x = y:x:xs
    | otherwise = x: insert y xs

isort [] = []
isort (x:xs) = insert x (isort xs)

bubble [] = []
bubble [x,y]
    | x < y = [x,y]
    | otherwise = [y,x]
bubble (x:y:xs)
    | x > y = y: bubble (x:xs)
    | otherwise = x: bubble (y:xs)

bsort [] = []
bsort (x:xs) = bubble(x:xs)

main = do 
    let lis = [4, 6, 9, 8, 3, 5, 1, 7, 2]
    print $ isort lis
    print $ bubble lis
    print $ bsort lis
