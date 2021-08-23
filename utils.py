import sympy as sym
import numpy as np
import itertools

c_i_j_dict = read_dictionary = np.load(
    './data/c_for_i_j_result.npy', allow_pickle='TRUE').item()

base_dim = 3
nb_character = 17
array_dim = (nb_character,) * base_dim
base_tensor = np.zeros(array_dim) # store c_i_j

for i in range(17):
    for j in range(17):
        base_tensor[i][j] = c_i_j_dict[str(i+1) + '_' + str(j+1)]

def nth_order_c(n):
    if n == 2:
        return base_tensor
    elif n>2:
        target_dim = n+1
        previous_tesnor = base_tensor
        for dim in range(3+1, target_dim+1):
            next_array_dim = (nb_character,) * dim
            next_tensor = np.zeros(next_array_dim)
            for idx in itertools.product(*[range(s) for s in (nb_character,) * (dim-1)]):
                index_except_last = idx[:dim-2]
                index_last = idx[-1]
                temp_array = np.zeros(nb_character)
                for counter in range(nb_character):
                    temp_array += previous_tesnor[index_except_last][counter] * base_tensor[counter][index_last]
                next_tensor[idx] = temp_array
            previous_tesnor = next_tensor
        return next_tensor


