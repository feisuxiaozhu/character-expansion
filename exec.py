from utils import nth_order_c 
import sympy as sym
import numpy as np
import itertools

def beta(i):
    string = 'beta_'+str(i)
    if i == 1:
        return sym.Symbol(string)-1
    else:
        return sym.Symbol(string)
    
nb_character = 17
target_order  = 2

result = []

# base result
for i in range(17):
    result.append(beta(i+1))
result = np.array(result)

print(result)

for i in range(1,target_order):
    order = i+1
    c_tensor = nth_order_c(order)
    for idx in itertools.product(*[range(s) for s in (nb_character, ) * order]):
        b = 1/order* (-1)**(order+1)
        for i in idx:
            b *= beta(i+1)
        result += b* c_tensor[idx]

# print result 
for i in range(len(result)):
    key = str(i+1)
    coefficient = sym.simplify(sym.expand(result[i]))
    print(key)
    print(coefficient)
        