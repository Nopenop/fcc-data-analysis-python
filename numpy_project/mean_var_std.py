import numpy as np

def calculate(list):
    if len(list) != 9:
        # expects list of length 9
        raise ValueError('List must contain nine numbers.')
    
    # Create 1 dimensional array
    straight_list = np.array(list)
    # Create 2 dimensional matrix
    square_matrix = np.reshape(list, [3,3])
    transposed_square_matrix = square_matrix.transpose()
    # print(square_matrix)
    # print(square_matrix)
    statistics = {}

    statistics['mean'] = [[transposed_square_matrix[0].mean(),transposed_square_matrix[1].mean(),transposed_square_matrix[2].mean()],[square_matrix[0].mean(),square_matrix[1].mean(),square_matrix[2].mean()],straight_list.mean()]
    statistics['variance'] = [[transposed_square_matrix[0].var(),transposed_square_matrix[1].var(),transposed_square_matrix[2].var()],[square_matrix[0].var(),square_matrix[1].var(),square_matrix[2].var()],straight_list.var()]
    statistics['standard deviation'] = [[transposed_square_matrix[0].std(),transposed_square_matrix[1].std(),transposed_square_matrix[2].std()],[square_matrix[0].std(),square_matrix[1].std(),square_matrix[2].std()],straight_list.std()]
    statistics['max'] = [[transposed_square_matrix[0].max(),transposed_square_matrix[1].max(),transposed_square_matrix[2].max()],[square_matrix[0].max(),square_matrix[1].max(),square_matrix[2].max()],straight_list.max()]
    statistics['min'] = [[transposed_square_matrix[0].min(),transposed_square_matrix[1].min(),transposed_square_matrix[2].min()],[square_matrix[0].min(),square_matrix[1].min(),square_matrix[2].min()],straight_list.min()]
    statistics['sum'] = [[transposed_square_matrix[0].sum(),transposed_square_matrix[1].sum(),transposed_square_matrix[2].sum()],[square_matrix[0].sum(),square_matrix[1].sum(),square_matrix[2].sum()],straight_list.sum()]
    
    return statistics
    # return calculations
