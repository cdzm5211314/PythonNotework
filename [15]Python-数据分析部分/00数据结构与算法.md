### Python中基本数据结构:
- **列表list:** 有序,元素可重复且是可变的,有索引,可以是任意对象如:字符串,整数,列表,元组,字典,...
- **元组tuple:** 有序,元素可重复且是不可变的,有索引
- **字典dict:** 无序,键值对类型(key不可重复且不可变,value可重复且是任意对象)
- **集合set:** 无序,元素不重复且不可变


### 数据的排序与搜索(查找):
- **冒泡排序:**
    - 比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
    - 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
    - 针对所有的元素重复以上的步骤，除了最后一个。
    - 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
```python
def bubble_sort(alist):
    # 外循环控制序列的遍历次数: 序列的长度 - 1
    for j in range(len(alist)-1,0,-1):
        # 内循环控制每次遍历需要比较的次数j,是逐渐减小的
        for i in range(j):
            #if alist[i] > alist[i+1]:  # 比较两个数值大小,从小到大排序,大值往后移位
            if alist[i] < alist[i+1]:  # 比较两个数值大小,从大到小排序,小值往后移位
                alist[i], alist[i+1] = alist[i+1], alist[i]
li = [54,26,93,17,77,31,44,55,20]
bubble_sort(li)
print(li)

```
- **选择排序:**
    - 工作原理:首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
```python
def selection_sort(alist):
    n = len(alist)
    # 外循环控制序列的选择次数: 序列的长度 - 1
    for i in range(len(alist)-1):
        min_index = i  # 假设最小值位置索引
        # max_index = i  # 假设最小值位置索引
        # 内循环控制每次遍历需要比较的次数j,是逐渐减小的
        for j in range(i+1, len(alist)):
            # if alist[j] < alist[min_index]:  # 比较两个数值大小,从大到小排序,小值往后移位
            # 当假设的最小值实际不是序列中的最小值,就把当前最小的索引赋值给假设的最小值索引变量min_index 
            # 从 i+1 位置到末尾选择出最小数据
            if alist[j] < alist[min_index]:  # 比较两个数值大小,从小到大排序,大值往后移位
                min_index = j
        # 如果选择出的数据不在正确的索引位置，进行交换索引的值
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]
alist = [54,226,93,17,77,31,44,55,20]
selection_sort(alist)
print(alist)

```
- **插入排序:**
    - 工作原理:通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。插入排序在实现上，在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
```python
def insert_sort(alist):
    # 从第二个位置，即下标为1的元素开始向前插入
    for i in range(1, len(alist)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            # if alist[j] > alist[j-1]:  # 从大到小
            if alist[j] < alist[j-1]:  # 从小到大
                alist[j], alist[j-1] = alist[j-1], alist[j]
alist = [54,26,93,17,77,31,44,55,20]
insert_sort(alist)
print(alist)

```
- **快速排序:**
    - 工作原理:通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
```python
def quick_sort(alist, start, end):
    # 递归的退出条件
    if start >= end:
        return
    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]
    # low为序列左边的由左向右移动的游标
    low = start
    # high为序列右边的由右向左移动的游标
    high = end
    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]
        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]
    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid
    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low-1)
    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low+1, end)
alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist,0,len(alist)-1)
print(alist)

```
- **希尔排序:**

- **归并排序:**

- **二分法查找(折半查找):**
    - 优点是比较次数少，查找速度快，平均性能好；缺点是要求待查表为有序表，且插入删除困难。因此，折半查找方法适用于不经常变动而查找频繁的有序列表。首先，假设表中元素是按升序排列，将表中间位置记录的关键字与查找关键字比较，如果两者相等，则查找成功；否则利用中间位置记录将表分成前、后两个子表，如果中间位置记录的关键字大于查找关键字，则进一步查找前一子表，否则进一步查找后一子表。重复以上过程，直到找到满足条件的记录，使查找成功，或直到子表不存在为止，此时查找不成功。
```python
### 非递归实现:
def binary_search(alist, item):
    first = 0
    last = len(alist)-1
    while first<=last:
        midpoint = (first + last)/2
        if alist[midpoint] == item:
            return True
        elif item < alist[midpoint]:
            last = midpoint-1
        else:
            first = midpoint+1
    return False
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))

### 递归实现:
def binary_search(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
          return True
        else:
          if item<alist[midpoint]:
            return binary_search(alist[:midpoint],item)
          else:
            return binary_search(alist[midpoint+1:],item)
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))

```
- **二叉树排序(中序遍历):**
```python
class BTree:  # 二叉树节点
	def __init__(self, value):  # 初始化函数
		self.left = None  # 左儿子
		self.data = value  # 节点值
		self.right = None  # 右儿子
	def insertLeft(self, value):  # 向左子树插入节点
		self.left = BTree(value)
		return self.left
	def insertRight(self, value):  # 向右子树插入节点
		self.right = BTree(value)
		return self.right
	def show(self):  # 输出节点数据
		print(self.data)
def inorder(node):  # 中序遍历
	if node.data:
		if node.left:
			inorder(node.left)
		node.show()
		if node.right:
			inorder(node.right)
def rinorder(node):  # 中序遍历,先遍历右子树
	if node.data:
		if node.right:
			rinorder(node.right)
		node.show()
		if node.left:
			rinorder(node.left)
def insert(node, value):
	if value > node.data:
		if node.right:
			insert(node.right, value)
		else:
			node.insertRight(value)
	else:
		if node.left:
			insert(node.left, value)
		else:
			node.insertLeft(value)
if __name__ == '__main__':
	l = [3, 5 , 7, 20, 43, 2, 15, 30]
	Root = BTree(l[0])  # 根节点
	node = Root
	for i in range(1, len(l)):
		insert(Root, l[i])
	print('*****************************')
	print('        从小到大')
	print('*****************************')
	inorder(Root)
	print('*****************************')
	print('        从大到小')
	print('*****************************')
	rinorder(Root)
	
```


