from utils import nth_order_coefficients
import numpy as np


result = nth_order_coefficients(2)


# print result 
for i in range(len(result)):
    key = str(i+1)
    temp = str(result[i])
    new = temp.replace('**','^')
    print(f'coefficients for chi_{key}:')
    print(new)
        