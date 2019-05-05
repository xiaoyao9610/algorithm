"""
用python完成对队列的实现
队列：先进先出
"""


class MyQueue:
    def __init__(self):
        self.my_queue = []

    def in_queue(self, args):
        # 入队一个元素
        self.my_queue.append(args)

    # def many_inqueue(self, *args):
    #     # 入队多个元素
    #     self.queue.extend(args)

    def out_queue(self):
        # 出队
        if not self.my_queue == []:
            self.my_queue.pop(0)
        else:
            return None

    def show(self):
        # 显示队列
        # for i in self.my_queue:
        print(self.my_queue)

    def head(self):
        # 队列的头部
        if not self.my_queue == []:
            return self.my_queue[0]
        else:
            return None

    def tail(self):
        # 队列的尾部
        if not self.my_queue == []:
            return self.my_queue[-1]
        else:
            return None

    def is_empty(self):
        # 队列是否为空
        return self.my_queue == []

    def lenght(self):
        # 队列的长度
        return len(self.my_queue)


q = MyQueue()
q.in_queue('1')
q.in_queue('2')
q.in_queue('3')
q.show()
print(q.lenght())
q.out_queue()
q.show()