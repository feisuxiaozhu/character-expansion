from utils import nth_order_coefficients, nth_order_c
import itertools
import sympy as sym

nb_character = 17
gammas = nth_order_coefficients(2)

result = nth_order_coefficients(1) # first order result
print(result)
multiplication_table = nth_order_c(2)

for idx in itertools.product(*[range(s) for s in (nb_character, ) * 2]):
    two_chi_product = multiplication_table[idx]
    result += 1/2* gammas[idx[0]]*gammas[idx[1]]*two_chi_product
print('calclulation done, begin to simplify')
final_result=[]
counter = 1
for unsimplified in result:
    print(f'simplify the coefficient for chi_{counter}' )
    simplified = sym.simplify(sym.expand(unsimplified))
    print(simplified)
    final_result.append(simplified)
    counter += 1




