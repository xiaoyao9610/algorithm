"""
用python实现对栈的操作
栈：先进后出
"""


class Stack(object):
    def __init__(self):
        # 初始化，即创建一个列表
        self.__list = []

    def push(self, data):  # 进栈操作
        self.__list.append(data)

    def pop(self):  # 出栈操作
        self.__list.pop()

    def peek(self):  # 返回栈中元素
        if self.__list:
            return self.__list
        else:
            return None

    def is_empty(self):  # 判断是否为空
        return not self.__list

    def size(self):  # 计算栈的长度
        return len(self.__list)


if __name__ == "__main__":
    """进行测试"""
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.size())
    print(s.peek())
    s.pop()
    print(s.peek())
    print(s.is_empty())
