import pdb
import numpy as np
import tools

a = np.matrix(
    [
        [1, 6],
        [2, 8],
        [3, 11],
        [3, 10],
        [1, 7]
    ]
)
print('Initial matrix')
print(a)
tools.print_separator()

# Задание 1
mean_a = a.mean(0)

# Не разобрался как вывести result в виде одномерного массива
# т.к. метод mean() возвращает двумерный массив [[*, *, *, *, *]]
# ничего лучше чем result.tolist[0] не придумал
# напишите пожалуйста в коменте как по нормальному можно вывести результат
print('Task 1')
print(f'Mean value for each observation: {mean_a.tolist()[0]}')
tools.print_separator()

# Задание 2

a_centered = a - mean_a

print('Task 2')
print(a_centered)
tools.print_separator()

# Задание 3

transposed_array = np.squeeze(np.asarray(a_centered)).transpose()
a_centered_sp = np.dot(*transposed_array)

unbiased_covariance_estimate = a_centered_sp / (transposed_array.shape[1] - 1)

print('Task 3')
print(f"Unbiased covariance estimate: {unbiased_covariance_estimate}")
tools.print_separator()

# Задание 4

unbiased_covariance_estimate_check = np.cov(a.transpose())[0][1]

print('Task 4')
print(f'unbiased covariance estimate check: {unbiased_covariance_estimate_check}')
