"""
用python实现对链表的操作
"""


class Node(object):
    """定义链表节点"""

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DlinkList(object):
    """定义双向链表类"""

    def __init__(self):  # 链表的头元素
        self._head = None

    def is_empty(self):
        """判断是否为空"""
        return self._head == None  # 判断首元素存不存在，不存在则说明链表为空

    def lenght(self):
        """返回链表的长度"""
        cur = self._head
        count = 0
        while cur != None:  # 链表不为空，则用count来计算；链表的长度
            cur = cur.next  # cur的下一个元素就成为新的cur
            count += 1
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur != None:
            print(cur.item, end='  ')
            cur = cur.next

    def add(self, item):
        """在链表头部添加元素"""
        node = Node(item)
        if self._head == None:  # 首先判断是否为空
            self._head = node
        else:
            node.next = self._head  # 新元素的后驱为原首元素
            self._head.prev = node  # 原首元素的前继为新元素
            self._head = node  # 新元素就成为新的首元素

    def append(self, item):
        """在链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():  # 判断链表是否为空
            self._head = node
        else:
            cur = self._head
            while cur.next != None:  # 找到链表的最后一个元素
                cur = cur.next
            cur.next = node  # cur 的next 指向 node
            node.prev = cur  # node 的prev 指向 cur

    def search(self, item):
        """查找元素是否存在"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                # 如果当前元素为要查找的元素 返回True，如果不是，继续往后查找，直至找到或找完
                return True
            cur = cur.next
        return False

    def insert(self, pos, item):
        """在链表中指定位置插入元素"""
        node = Node(item)
        if pos <= 0:
            # 如果指定的位置小于或等于0，就插到第一个位置
            self.add(item)
        elif pos > self.lenght() - 1:
            # 如果指定位置大于或等于链表长度，就插到最后一个位置
            self.append(item)
        else:
            cur = self._head
            count = 0
            while count < pos - 1:  # 利用count将cur移动到指定位置pos的前面
                cur = cur.next
                count += 1
                # 将node插入cur 和 cur.next之间
            node.next = cur.next  # 新元素的后继指向cur的后继
            node.prev = cur  # 新元素的前驱为cur
            cur.next.prev = node  # cur的后继的前驱指向新元素node
            cur.next = node  # 将cur的后继指向新元素node

    def remove(self, item):
        """删除元素"""
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.item == item:  # 如果要删除的元素是第一个元素的时候
                if cur.next == None:  # 如果这个链表只有一个元素的时候
                    self._head = None
                else:  # 如果有多个元素的时候，将第二个元素设为头元素
                    cur.next.prev = None
                    self._head = cur.next
                return
            while cur != None:
                if cur.item == item:  # 完成对满足条件的item的的删除
                    #  将cur的前继的后驱指向cur的后驱
                    cur.next.prev = cur.prev
                    #  将cur的后驱的前继指向cur的前继
                    cur.prev.next = cur.next
                    break
                cur = cur.next


if __name__ == "__main__":
    my_link = DlinkList()
    my_link.append(1)
    my_link.append(2)
    my_link.append(3)
    my_link.add(4)
    my_link.travel()
    print()
    my_link.insert(1, 5)
    my_link.travel()
    my_link.remove(2)
    print()
    my_link.travel()
