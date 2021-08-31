from utils import nth_order_coefficients
import numpy as np

order = 4
result = nth_order_coefficients(order)

result_dict = {}
# print result 
for i in range(len(result)):
    key = str(i+1)
    temp = str(result[i])
    new = temp.replace('**','^')
    print(f'coefficients for chi_{key}:')
    print(new)
    result_dict[f'coefficients for chi_{key}:'] = new

with open(f'./data/gamma_order_{order}','wb') as f:
    np.save(f, result_dict)
