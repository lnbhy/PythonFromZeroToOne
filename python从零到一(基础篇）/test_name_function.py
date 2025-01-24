#任何测试文件需要以test_开头
from name_function import get_formatted_name
def  test_first_last_name():
    '''姓名格式化函数的正确性'''
    formatted_name = get_formatted_name('janis','joplin')
    #断言，如果不相等，则报错
    assert formatted_name == 'Janis Joplin'