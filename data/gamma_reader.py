import numpy as np
order = 4
filename = f'gamma_order_{order}'
gamma_coef_dict= read_dictionary = np.load(
    './'+filename, allow_pickle='TRUE').item()
print(gamma_coef_dict['coefficients for chi_17:'])
