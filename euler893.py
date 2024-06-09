# <p>
# Define $M(n)$ to be the minimum number of matchsticks needed to represent the number $n$.</p>

# <p>
# A number can be represented in digit form or as an expression involving addition and/or multiplication. Also order of operations must be followed, that is multiplication binding tighter than addition. Any other symbols or operations, such as brackets, subtraction, division or exponentiation, are not allowed.</p>

# <p>
# The valid digits and symbols are shown below:</p>
# <div style="text-align:center;">
# <img src="resources/images/0893_DigitDiagram.jpg?1714876316" alt="0893_DigitDiagram.jpg" height="433" width="668"></div>

# <p>
# For example, $28$ needs $12$ matchsticks to represent it in digit form but representing it as $4\times 7$ would only need $9$ matchsticks and as there is no way using fewer matchsticks $M(28) = 9$.</p>

# <p>
# Define $\displaystyle T(N) = \sum_{n=1}^N M(n)$. You are given $T(100) = 916$.</p>

# <p>
# Find $T(10^6)$.</p>


# dictionary for what each char requires how many matchsticks
match_stick_vals = {
    '1' = 2, 
    '2' = 5, 
    '3' = 5, 
    '4' = 5, 
    '5' = 5,
    '6' = 6,
    '7' = 4,
    '8' = 7,
    '9' = 6,
    '+' = 2,
    'x' = 2,
}
