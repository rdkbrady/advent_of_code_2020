import operator


def match_mat(value, array, n=2, op = operator.add):
    shape = np.ones(n).astype(int)
    arrays = []
    for i in range(len(shape)):
        new_shape = shape.copy()
        new_shape[i] = -1
        arrays.append(array.reshape(tuple(new_shape)))
    match_vals = reduce(op, arrays)
    matched = np.where(match_vals == value)
    return(np.array(matched).T)
        
def match_sum(*args):
    return(match_mat(*args, op=operator.add))

def match_prod(*args):
    return(match_mat(*args, op=operator.mul))