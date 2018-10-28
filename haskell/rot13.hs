import Data.Char

rot13' s
    | 'A' <= s && s <= 'M'
    || 'a' <= s && s <= 'm' = chr (ord (s) + 13)
    | 'N' <= s && s <= 'Z'
    || 'n' <= s && s <= 'z' = chr (ord (s) - 13)
    | otherwise = s

rot13 ""     = ""
rot13 (x:xs) = rot13' (x) : rot13 xs

main = do
    let hello13 = "Hello, World!!"
    print $ rot13 hello13
