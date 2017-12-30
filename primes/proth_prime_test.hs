{- Copyright Dario Balboni 2017
 - The code is provided 'as is' without any warranty and it is under the public domain.
 -
 - DESCRIPTION:
 - Given e as input we calculate if the number N = 3 * 2 ^ {3 e + 2} + 1 is a prime using
 - a little variant of Proth theorem and Pepin test. We make use that numbers of that form
 - are prime if and only if 7 ^ {3 * 2^{3 e + 2}} == -1 (mod N).
 -
 - Usage: isProthPrime e
 - For reference see https://arxiv.org/pdf/0812.2596.pdf
 -}

import Data.Bits

modExp :: Integer -> Integer -> Integer -> Integer
modExp b 0 m = 1
modExp b e m = t * modExp ((b * b) `mod` m) (shiftR e 1) m `mod` m
  where t = if testBit e 0 then b `mod` m else 1


isProthPrime :: Integer -> Bool
isProthPrime e = (modExp 7 exp bign) == (bign - 1)
  where bign = 3 * 2 ^ (3 * e + 2) + 1
        exp = (bign - 1) `div` 2

