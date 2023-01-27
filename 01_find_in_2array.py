"""
    在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
    请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


def find_in_2array(array2, num):
    if not array2:
        return False
    for row in array2:
        for element in row:
            if num == element:
                return True
    return False


# *************************************
array2 = [[2, 4, 5, 6], [8, 9, 10, 11]]
array = []
print(find_in_2array(array, 1))
