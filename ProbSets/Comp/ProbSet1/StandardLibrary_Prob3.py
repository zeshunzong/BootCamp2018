import calculator

def get_hypotenuse(a, b):
    a_sq = calculator.get_product(a,a)
    b_sq = calculator.get_product(b,b)
    h_sq = calculator.get_sum(a_sq, b_sq)
    return calculator.sqrt(h_sq)

print(get_hypotenuse(3,4))
