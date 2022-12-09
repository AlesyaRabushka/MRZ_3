from functions import *
import functools


# def hopfild_neural_network(input_sequence, weight_matrix):
#     X = transform_into_matrix(input_sequence)
#     X_ = matrix_transposition(X)
#
#
#     if not weight_matrix:
#         #weight_matrix = get_weight_matrix(X)
#         weight_matrix = matrix_multiplication(X, X_)
#         weight_matrix = zero_main_diagonal(weight_matrix)
#
#     training(X, weight_matrix)


# def training(X, weight_matrix):
#     previous_state = X
#     current_state = []
#     relax = False
#
#     iteration = 0
#     while(iteration <= 1000):
#         state_matrix = transform_into_matrix(previous_state)
#
#         current_state = activation_function(matrix_multiplication(weight_matrix, previous_state), previous_state)
#         if functools.reduce(lambda x, y: x and y, map(lambda a, b: a == b, previous_state, current_state), True):
#             relax = True
#             print('Состояние релаксации достигнуто!')
#             write_matrix_into_file(weight_matrix)
#             break
#         iteration += 1
#         previous_state = current_state
#     if not relax:
#         print('Состояние релаксации не достигнуто!')






def recognize(X, weight_matrix):
    previous_state = matrix_transposition(X)
    curent_state = []
    relax = False
    iteration = 0

    while relax is not True:
        if iteration >= 1000:
            print('Невозможно распознать образ!')
            exit()

        m = matrix_multiplication(weight_matrix, previous_state)

        current_state = activation_function(m)

        if functools.reduce(lambda x, y: x and y, map(lambda a, b: a == b, previous_state, current_state), True):
        # if (previous_state == current_state).all():
            print('Образ распознан!')
           # show_model(matrix_transposition(previous_state))
            show_model(matrix_transposition(current_state))
            relax = True

        previous_state = current_state
        iteration += 1
