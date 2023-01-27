"""
    请实现一个函数，将一个字符串中的每个空格替换成“%20”。
    例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


def replace_space(string):
    string_list = string.split(' ')
    return '%20'.join(string_list)

string = 'we are happy'
print(replace_space(string))
