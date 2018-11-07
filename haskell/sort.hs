insert x [] = [x]
insert y (x:xs)
    | y<x = y:x:xs
    | otherwise = x: insert y xs
isort = foldr insert []

bswap [x] = [x]
bswap (x:xs)
    | x > y     = y:x:ys
    | otherwise = x:y:ys
    where
        (y:ys) = bswap xs

bsort [x]=[x]
bsort xs = y: bsort ys
    where
         (y:ys) = bswap xs

merge xs [] = xs
merge [] ys = ys
merge (x:xs) (y:ys)
    | x < y     = x : merge xs (y:ys)
    | otherwise = y : merge (x:xs) ys


msort []  = []
msort [x] = [x]
msort xs  = merge (msort (take h xs)) (msort (drop h xs))
    where
        h = length xs `div` 2



main = do
    let lis = [4, 6, 9, 8, 3, 5, 1, 7, 2]
    print $ isort lis
    print $ bsort lis
    print $ msort [4, 6, 9, 8, 3, 5, 1, 7, 2]
