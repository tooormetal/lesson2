from functools import reduce
my_list = [el for el in range(100, 1001) if el % 2 == 0]
def my_funk(prev_n, n):
    return prev_n * n
print(reduce(my_funk, my_list))