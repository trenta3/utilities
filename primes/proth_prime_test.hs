{- Copyright Dario Balboni 2017
 - The code is provided 'as is' without any warranty and it is under the public domain.
 -
 - DESCRIPTION:
 - For reference see https://arxiv.org/pdf/0812.2596.pdf
 -}

import Data.Bits

modExp :: Integer -> Integer -> Integer -> Integer
modExp b 0 m = 1
modExp b e m = t * modExp ((b * b) `mod` m) (shiftR e 1) m `mod` m
  where t = if testBit e 0 then b `mod` m else 1

-- e and t pairs with 3 \nmid t
nextProth :: (Integer, Integer) -> (Integer, Integer)
nextProth (e, t) = let nextt = if t `mod` 3 == 1 then t + 4 else t + 2
                   in if nextt >= 2^e then (e + 1, 1) else (e, nextt)

isPrime :: (Integer, Integer) -> Bool
isPrime (e, t) = (modExp 3 exp bign) == (bign - 1)
  where bign = t * 2^e + 1
        exp = (bign - 1) `div` 2

getFirstPrimeAfter :: (Integer, Integer) -> (Integer, Integer)
getFirstPrimeAfter s = let proths s = s : proths (nextProth s)
                       in head $ [ x | x <- proths s, isPrime x ]
  
