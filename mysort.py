# -*- coding:utf-8 -*-
def bubble_sort(arr):
    # 冒泡排序
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insert_sort(arr):
    """
        从第二个数开始，依次与前面的数进行比较，找到大于前面的数并小于后面的数的位置
        注意：
            若这个数大于前一个数，即说明是目前为止最大的数，就是说不需要移动其它数据
            若这个数小于前一个数，那么这个数应该赋值为前一个数字，以此实现数字的移动
                所以，在之前需要将比较的数字保存起来，避免被覆盖
    """
    for i in range(1, len(arr)):
        preindex = i - 1
        current = arr[i]
        while current < arr[preindex] and preindex >= 0:
            arr[preindex + 1] = arr[preindex]
            preindex -= 1
        arr[preindex + 1] = current
    return arr


a = insert_sort([3, 1, 4, 6, 5, 2])
print(a)
