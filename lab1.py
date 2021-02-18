# Getting the matrix from user
def get_matrix():
    new_matrix = []
    print('Welcome to the Gauss calculator!')
    print('Please, tell me, where is your matrix?')
    print('Write 1 if you want to write it by yourself')
    print('Write 0 if you want to get matrix from file')
    answer = int(input())
    if answer == 1:
        print('Great! So, how many rows do you have?')
        rows = int(input())
        print('Good job! Let\'s move forward')
        if rows != 1:
            for i in range(rows):
                a = []
                for j in range(rows + 1):
                    print('Write elem: row', i + 1, ', column:', j + 1)
                    a.append(float(input()))
                new_matrix.append(a)
            print('Thank you! Your matrix is here...')
            print(new_matrix)
            return new_matrix
        else:
            print('Oh, matrix should be 2x2, 3x3 or bigger! Please, try again!')
            return get_matrix()
    elif answer == 0:
        print('It\'s so great! Please, write the name of your file!')
        return get_matrix_from_file(input())
    else:
        print('Oh, your answer is broken! Please, try again!')
        return get_matrix()


# Getting matrix from the file by filename
def get_matrix_from_file(filename):
    with open(filename) as f:
        matrix_from_file = [list(map(float, row.split())) for row in f.readlines()]
    print('Matrix:')
    print_matrix(matrix_from_file, 5)
    return matrix_from_file


# Realising a Gauss's Method
def do_gauss_method(input_matrix):
    check_square_matrix(input_matrix)
    print('Let\'s do Gauss method')
    length_of_matrix = len(input_matrix)
    do_triangle_matrix(input_matrix)
    is_singular(input_matrix)
    input_answer_matrix = [0 for i in range(length_of_matrix)]
    for k in range(length_of_matrix - 1, -1, -1):
        input_answer_matrix[k] = (input_matrix[k][-1] - sum(
            [input_matrix[k][j] * input_answer_matrix[j] for j in range(k + 1, length_of_matrix)])) / input_matrix[k][k]
    print('FINALLY!')
    print('ヽ(⌐■_■)ノ♪♬')
    print('ANSWERS!')
    for i in range(len(input_answer_matrix)):
        print('x[', i + 1, '] =', "%5.3f" % input_answer_matrix[i])
    return input_answer_matrix


# Checking the matrix
def check_square_matrix(input_matrix):
    print('Check if matrix is square (and extended) AND has solutions')
    for i in range(len(input_matrix)):
        if len(input_matrix) + 1 != len(input_matrix[i]):
            raise Exception('ERROR: The size of matrix isn\'t correct')
        count = 0
        for j in range(len(input_matrix[i])-1):
            if input_matrix[i][j] == 0:
                count += 1
        if count == len(input_matrix[i])-1:
            raise Exception('ERROR: The matrix has no solutions')
    print('All is okay!')


def do_triangle_matrix(input_matrix):
    print('Let\'s create a Triangle Matrix')
    length_of_matrix = len(input_matrix)  # = number of rows
    for k in range(length_of_matrix - 1):
        print('Iteration №', k + 1)
        print('Matrix was...')
        print_matrix(input_matrix, 5)
        get_max_element_in_column(input_matrix, k)
        print('Matrix become...')
        print_matrix(input_matrix, 5)
        print('Do some math magic...')
        print('╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ *wibbly wobbly timey wimey*')
        print('**TA DA**')
        for i in range(k + 1, length_of_matrix):
            div = input_matrix[i][k] / input_matrix[k][k]
            input_matrix[i][-1] -= div * input_matrix[k][-1]
            for j in range(k, length_of_matrix):
                input_matrix[i][j] -= div * input_matrix[k][j]
        print_matrix(input_matrix, 5)
    return length_of_matrix


# Checking if matrix is singular (вырожденная)
def is_singular(input_matrix):
    print('Check if matrix is singular (вырожденная)')
    if count_determinant_for_square_matrix(input_matrix) == 0:
        raise Exception('ERROR: Your matrix is singular (det ~ 0)')
    else:
        print('OKAY, It isn\'t')


# Searching for the main element in the column
def get_max_element_in_column(input_matrix, number_of_column):
    max_element = input_matrix[number_of_column][number_of_column]
    max_row = number_of_column
    for j in range(number_of_column + 1, len(input_matrix)):
        if abs(input_matrix[j][number_of_column]) > abs(max_element):
            max_element = input_matrix[j][number_of_column]
            max_row = j
    if max_row != number_of_column:
        input_matrix[number_of_column], input_matrix[max_row] = input_matrix[max_row], input_matrix[number_of_column]
    print('The max element between not fixed rows is', "%.4f" % max_element, 'in row', max_row + 1)
    return input_matrix


# Printing matrix in the comfortable view
def print_matrix(input_matrix, decimals):
    for i in range(len(input_matrix)):
        for j in range(len(input_matrix[i])):
            print('|', "%10.4f" % (input_matrix[i][j]), end=' ')
        print()


# Create residual vector (вектор невязок)
def do_residual_vector(input_matrix, input_answer_matrix):
    big_matrix = []
    little_matrix = []
    for i in range(len(input_matrix)):
        big_matrix.append(input_matrix[i][0:len(input_matrix)])
        little_matrix.append(input_matrix[i][len(input_matrix):])
    x_matrix = input_answer_matrix
    temp = [0 for i in range(len(input_matrix))]
    residual_vector = [0 for i in range(len(input_matrix))]
    print('Good job! But...')
    print('Let\'s find residual vector!')
    print('Residual vector:')
    for i in range(len(big_matrix)):
        temp[i] = 0
        for j in range(len(big_matrix)):
            temp[i] += x_matrix[j] * big_matrix[i][j]
        residual_vector[i] = temp[i] - little_matrix[i][0]
        print('r[', i + 1, '] =', residual_vector[i], end='\n')


# Counting the determinant of the out matrix
def count_determinant_for_square_matrix(input_matrix):
    determinant = 1
    for i in range(len(input_matrix)):
        determinant *= input_matrix[i][i]
    print('Determinant of matrix =', round(determinant, 5))
    return round(determinant, 5)


# TODO: MAIN PROGRAM
# TODO: 2) CHECK NUMBER OF ANSWERS (NONE, NOPE or INF)
# TODO: 4) OTCHET

try:
    main_matrix = get_matrix()
    answer_matrix = do_gauss_method(main_matrix)
    do_residual_vector(main_matrix, answer_matrix)
except Exception as ex:
    template = "Oh, you've got an exception! What a pity! So, the problem is...\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)