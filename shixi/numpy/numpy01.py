'''
numpy 提供了数据分析的运算的基础，操作高维数据（矩阵）
numpy 提供了一种数组类型
'''
import numpy as np
#查看 numpy的版本
#print(np.__version__)
#numpy 被设计的初衷是 运算的，对数据进行统一的优化
# ** numpy 默认的 ndarray的所有的元素类型都是相同的
# 数组类型有一个优先级  str>folat>int
#numpy的数组
#将列表转化为 numpy.ndarray 类型，被转化的列表里有字符串，由于优先级的原因，所有的值都变成字符串
array = np.array([1,2,3,7.5,'hello'])
#numpy 将二维的列表转化为 数组类型
array2 = np.array([[1,2,3],[4,5,6]])
#print(type(array2))
#numpy可以产生一个  二维的5行5列的数组
# shape = (m,n) m行 n列 二维数组
# shape = (m) m个元素的一维数组
# shape = (m,1) m行 1列的二维数组float
# dtype 是设置元素的类型
#print(np.ones(shape=(5,5),dtype=np.int8))float

#print(np.ones(shape=(5,5),dtype=np.float))
#用0去填充矩阵
#print(np.zeros(shape=(5,6)))

#print(np.zeros(shape=(5),dtype=int))
#输出一个3维的矩阵
#print(np.zeros(shape=(2,5,6)))
# 由6来填充 2行3列的矩阵
#print(np.full(shape=(2,3),fill_value=6))

#对角线为1，其他位置为0矩阵 (3行3列的矩阵)
#print(np.eye(N=3,dtype=int))

# 多加一个M的参数，会减少列数
#print(np.eye(N=5,M=4,dtype=int))

# 加 k 的参数矩阵对角线上下移动
#print(np.eye(N=5,k=-1,dtype=int))
# 生成一个等差数列
# 参数1 开始的数，参数2 等差数列结束的数，参数3:等差数列的数量 参数4：是否以最后一个数结尾
#print(np.linspace(0,40,10,endpoint=True,dtype=float))

# 另外一种等差数列的写法
# 参数1 等差数列 开始的数值，参数2:等差数列结束的数值，参数3 等差数列的差值
#print(np.arange(0,10,step=3))

# 生成一个矩阵，都是随机数进行填充
# size等同于 shape
#print(np.random.randint(0,100,size=(5,5)))

# 输出标准的正太分布
#print(np.random.randn(3,5))

#输出一个普通的正太分布
#loc 是标准差 期望，scale
#print(np.random.normal(loc=170,scale=5,size=(5,3)))

#生成随机索引,索引的范围是 从0开始 到最大值-1
#print(np.random.permutation(10))


#生成一个 从0到1随机数矩阵 5行5列
# 这个 print(np.random.randint(0,100,size=(5,5))) 0-100 的随机数
#print(np.random.random(size=(5,5)))

# numpy ndarray 的属性
# 4需要记住的参数  ndim:维度  shape:形状 size:总长度 dtype:元素类型
arr = np.random.randint(0,100,size=(2,5,5))
#输出数组的维度
# print(arr.ndim)
# #输出数组的形状
# print(arr.shape)
# #输出数组的总长度
# print(arr.size)
# #输出元素类型
# print(arr.dtype)

#ndarray 其他的操作  索引 切片 变形 级联，切分 副本
data = [[1,2,3],[4,5,6]]
#print(data[0][0])

arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
#访问和列表访问差不多
#print(arr1[0][0])
#numpy 特有的 可以采用对方维度索引进行访问
#print(arr1[1,0])
# numpy 高级用法
#print(arr1[[0,1,0,1,1,2]])
# 效果如下
# [[1 2 3]
#  [4 5 6]
#  [1 2 3]
#  [4 5 6]
#  [4 5 6]
#  [7 8 9]]

# 采用布尔类型,来决定ndarray 数组的值是否显示
bool_list = [True,False,True]
#print(arr1[bool_list])
arr2 = np.array([1,2,3,4,5])
bool_list1 = [True,False,True,False,True]
#print(arr2[bool_list1 ])
#找到 arr2 数组中数值大于2的数
#print(arr2[arr2>2])
#arr3 = np.random.randint(0,10,size=(5,4,3))
#print(arr3)

#print("*****************************")
# 输出三维数组 每一行的值
#print(arr3[2,0])
#arr2 = np.array([1,2,3,4,5])
#数组中的切片
#对 arr2进行切片,左闭后开的规则
#print(arr2[0:3])
# 创建  0 -100 5行6列的2维数组
#arr3 = np.random.randint(0,100,size=(5,6))
#print(arr3)
#print("*****************************")
#行切片
#print(arr3[0:2])

#列切片
#print(arr3[:,0:2])

#创建一个3维的二维数组
arr4 = np.random.randint(0,10,size=(3,4,5))

# print(arr4)
# #切 前两个数组
# print("*******************")
# print(arr4[0:2])
# #切割每一个二维数组的前两项
# print("*******************")
# print(arr4[:,:,0:2])

# 数据的反转 [1,2,3] ----->[3,2,1]
#arr5 = np.array([1,2,3,4,5])
#1维数组反转
#print(arr5[::-1])
#二维的数组
# arr6 = np.random.randint(0,100,size=(5,6))
# print(arr6)
# print("*******************")
# #二维数组反转 行反转
# #print(arr6[::-1])
# #列反转
# print(arr6[:,::-1])
# #行和列都反转
# print(arr6[::-1,::-1])

#变形
#0 -10 一个1维数组
#arr7 = np.random.randint(0,10,size=(20))
#print(arr7)
# 把它变形为4行5列的矩阵
# reshape 是一个元组 tuple
#print(arr7.reshape((4,5)))
#一下不可以，会出错
#print(arr7.reshape((3,7)))

#级联
# 1 .np.concatenate,需要注意，级联的参数是列表，一定要加中括号，维度必须相同
#2形状必须相符
#3 级联默认的方向 shape 这个tuple 第一个值代表的维度方向
# 通过 axis改变级联方向

#arr1 = np.random.randint(0,10,size=(3,3))
#arr2 = np.random.randint(0,20,size=(3,3))
#print(arr1)
#print(arr2)
#print("*******************")
#把  arr1 和arr2级联在一起
# axios 是列和列的级联
# axios 是行和行的级联，也是默认的级联
#print(np.concatenate((arr1,arr2),axis=1))

# 可以利用函数 hstack 还有  vstack 进行级联
#print(np.hstack((arr1,arr2)))
#print(np.vstack((arr1,arr2)))

# 切分
# np.split np.vsplit np.hsplit
#arr=np.random.randint(0,100,size=(3,7))
#print(arr)
#开始切分,indices_or_sections 切成几部分,通过axis 控制切分的方向
# axis=1 按照列进行切分   axis=0 按照行进行切分
#part1,part2,part3 = np.split(arr,indices_or_sections=3,axis=0)
#利用函数进行切分
#行级切分
#part1,part2,part3 = np.hsplit(arr,indices_or_sections=3)
#列级切分
# 0:2 列  2：5列  5：最后
# part1,part2 ,part3= np.split(arr,indices_or_sections=[2,5],axis=1)
# print(part1)
# print("********")
#
# print(part2)
# print("********")
# print(part3)



#副本内容
#arr = np.random.randint(0,100,size=(6,6))
#通过copy函数创建副本,改变副本不会对原来的对象有影响，赋值不可以的，会有影响
# brr =  arr.copy()
# print(arr)
# brr[0,0] = 99
# print(arr)
# arr = np.random.randint(0,10,size=(10))
# print(arr)
# #输出和
# print(arr.sum())
# #输出平均值
# print(arr.mean())
# print(arr.max(),arr.min())
# #输出最大值的索引
# print('最大值的索引是:',arr.argmax())
# print("标准差",arr.std())
# #可以输出方差
# print("方差:",arr.var())
# #可以输出中位数
# print("中位数",np.median(arr))

#矩阵的运算
# 矩阵的乘积
# a = np.array([[1,2],[3,4]])
# b = np.array([[1,1],[2,2]])
#
# print(a)
# print(b)
#
# print("********")
# # 单纯的位置 相乘
# print(a*b)
# # 输出中的矩阵运算
# print(np.dot(a,b))


#广播机制
# arr = np.random.randint(0,10,size=(10))
# print(arr)
# data = 3
# #所有的数在原来的基础上都加3了
# print(arr + 3)

# 广播的机制有两个特性
# 可以为缺失是的维度补1
#  假定缺失的元素用已有的值填充

# m = np.ones((2,3))
# print(m)
#
# a = np.arange(3)
# # [[0,1,2],[0,1,2]]  和  m进行相加的时候,会自动补全（用已有的元素），在和m进行相加
# print(a)
# print("*****8")
# print(m + a)
# print(m+1)
#

# 三行一列的二维数组
a = np.arange(0,3,step=1).reshape(3,1)
# print(a)
# b = np.arange(3)
# print(b)
# print("*******")
# a  和  b  分别扩充如下格式
'''0 0 0
   1 1 1
   2 2 2   
   
   0  1  2
   0  1  2
   0  1  2

'''
# print(a + b)
# 得出的结果是如下的值
'''
[[0 1 2]'''

'''
import numpy as np
#查看 numpy的版本
#print(np.__version__)
#numpy 被设计的初衷是 运算的，对数据进行统一的优化
# ** numpy 默认的 ndarray的所有的元素类型都是相同的
# 数组类型有一个优先级  str>folat>int
#numpy的数组
#将列表转化为 numpy.ndarray 类型，被转化的列表里有字符串，由于优先级的原因，所有的值都变成字符串
array = np.array([1,2,3,7.5,'hello'])
#numpy 将二维的列表转化为 数组类型
array2 = np.array([[1,2,3],[4,5,6]])
#print(type(array2))
#numpy可以产生一个  二维的5行5列的数组
# shape = (m,n) m行 n列 二维数组
# shape = (m) m个元素的一维数组
# shape = (m,1) m行 1列的二维数组float
# dtype 是设置元素的类型
#print(np.ones(shape=(5,5),dtype=np.int8))float

#print(np.ones(shape=(5,5),dtype=np.float))
#用0去填充矩阵
#print(np.zeros(shape=(5,6)))

#print(np.zeros(shape=(5),dtype=int))
#输出一个3维的矩阵
#print(np.zeros(shape=(2,5,6)))
# 由6来填充 2行3列的矩阵
#print(np.full(shape=(2,3),fill_value=6))

#对角线为1，其他位置为0矩阵 (3行3列的矩阵)
#print(np.eye(N=3,dtype=int))

# 多加一个M的参数，会减少列数
#print(np.eye(N=5,M=4,dtype=int))

# 加 k 的参数矩阵对角线上下移动
#print(np.eye(N=5,k=-1,dtype=int))
# 生成一个等差数列
# 参数1 开始的数，参数2 等差数列结束的数，参数3:等差数列的数量 参数4：是否以最后一个数结尾
#print(np.linspace(0,40,10,endpoint=True,dtype=float))

# 另外一种等差数列的写法
# 参数1 等差数列 开始的数值，参数2:等差数列结束的数值，参数3 等差数列的差值
#print(np.arange(0,10,step=3))

# 生成一个矩阵，都是随机数进行填充
# size等同于 shape
#print(np.random.randint(0,100,size=(5,5)))

# 输出标准的正太分布
#print(np.random.randn(3,5))

#输出一个普通的正太分布
#loc 是标准差 期望，scale
#print(np.random.normal(loc=170,scale=5,size=(5,3)))

#生成随机索引,索引的范围是 从0开始 到最大值-1
#print(np.random.permutation(10))


#生成一个 从0到1随机数矩阵 5行5列
# 这个 print(np.random.randint(0,100,size=(5,5))) 0-100 的随机数
#print(np.random.random(size=(5,5)))

# numpy ndarray 的属性
# 4需要记住的参数  ndim:维度  shape:形状 size:总长度 dtype:元素类型
arr = np.random.randint(0,100,size=(2,5,5))
#输出数组的维度
# print(arr.ndim)
# #输出数组的形状
# print(arr.shape)
# #输出数组的总长度
# print(arr.size)
# #输出元素类型
# print(arr.dtype)

#ndarray 其他的操作  索引 切片 变形 级联，切分 副本
data = [[1,2,3],[4,5,6]]
#print(data[0][0])

arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
#访问和列表访问差不多
#print(arr1[0][0])
#numpy 特有的 可以采用对方维度索引进行访问
#print(arr1[1,0])
# numpy 高级用法
#print(arr1[[0,1,0,1,1,2]])
# 效果如下
# [[1 2 3]
#  [4 5 6]
#  [1 2 3]
#  [4 5 6]
#  [4 5 6]
#  [7 8 9]]

# 采用布尔类型,来决定ndarray 数组的值是否显示
bool_list = [True,False,True]
#print(arr1[bool_list])
arr2 = np.array([1,2,3,4,5])
bool_list1 = [True,False,True,False,True]
#print(arr2[bool_list1 ])
#找到 arr2 数组中数值大于2的数
#print(arr2[arr2>2])
#arr3 = np.random.randint(0,10,size=(5,4,3))
#print(arr3)

#print("*****************************")
# 输出三维数组 每一行的值
#print(arr3[2,0])
#arr2 = np.array([1,2,3,4,5])
#数组中的切片
#对 arr2进行切片,左闭后开的规则
#print(arr2[0:3])
# 创建  0 -100 5行6列的2维数组
#arr3 = np.random.randint(0,100,size=(5,6))
#print(arr3)
#print("*****************************")
#行切片
#print(arr3[0:2])

#列切片
#print(arr3[:,0:2])

#创建一个3维的二维数组
arr4 = np.random.randint(0,10,size=(3,4,5))

# print(arr4)
# #切 前两个数组
# print("*******************")
# print(arr4[0:2])
# #切割每一个二维数组的前两项
# print("*******************")
# print(arr4[:,:,0:2])

# 数据的反转 [1,2,3] ----->[3,2,1]
#arr5 = np.array([1,2,3,4,5])
#1维数组反转
#print(arr5[::-1])
#二维的数组
# arr6 = np.random.randint(0,100,size=(5,6))
# print(arr6)
# print("*******************")
# #二维数组反转 行反转
# #print(arr6[::-1])
# #列反转
# print(arr6[:,::-1])
# #行和列都反转
# print(arr6[::-1,::-1])

#变形
#0 -10 一个1维数组
#arr7 = np.random.randint(0,10,size=(20))
#print(arr7)
# 把它变形为4行5列的矩阵
# reshape 是一个元组 tuple
#print(arr7.reshape((4,5)))
#一下不可以，会出错
#print(arr7.reshape((3,7)))

#级联
# 1 .np.concatenate,需要注意，级联的参数是列表，一定要加中括号，维度必须相同
#2形状必须相符
#3 级联默认的方向 shape 这个tuple 第一个值代表的维度方向
# 通过 axis改变级联方向

#arr1 = np.random.randint(0,10,size=(3,3))
#arr2 = np.random.randint(0,20,size=(3,3))
#print(arr1)
#print(arr2)
#print("*******************")
#把  arr1 和arr2级联在一起
# axios 是列和列的级联
# axios 是行和行的级联，也是默认的级联
#print(np.concatenate((arr1,arr2),axis=1))

# 可以利用函数 hstack 还有  vstack 进行级联
#print(np.hstack((arr1,arr2)))
#print(np.vstack((arr1,arr2)))

# 切分
# np.split np.vsplit np.hsplit
#arr=np.random.randint(0,100,size=(3,7))
#print(arr)
#开始切分,indices_or_sections 切成几部分,通过axis 控制切分的方向
# axis=1 按照列进行切分   axis=0 按照行进行切分
#part1,part2,part3 = np.split(arr,indices_or_sections=3,axis=0)
#利用函数进行切分
#行级切分
#part1,part2,part3 = np.hsplit(arr,indices_or_sections=3)
#列级切分
# 0:2 列  2：5列  5：最后
# part1,part2 ,part3= np.split(arr,indices_or_sections=[2,5],axis=1)
# print(part1)
# print("********")
#
# print(part2)
# print("********")
# print(part3)



#副本内容
#arr = np.random.randint(0,100,size=(6,6))
#通过copy函数创建副本,改变副本不会对原来的对象有影响，赋值不可以的，会有影响
# brr =  arr.copy()
# print(arr)
# brr[0,0] = 99
# print(arr)
# arr = np.random.randint(0,10,size=(10))
# print(arr)
# #输出和
# print(arr.sum())
# #输出平均值
# print(arr.mean())
# print(arr.max(),arr.min())
# #输出最大值的索引
# print('最大值的索引是:',arr.argmax())
# print("标准差",arr.std())
# #可以输出方差
# print("方差:",arr.var())
# #可以输出中位数
# print("中位数",np.median(arr))

#矩阵的运算
# 矩阵的乘积
# a = np.array([[1,2],[3,4]])
# b = np.array([[1,1],[2,2]])
#
# print(a)
# print(b)
#
# print("********")
# # 单纯的位置 相乘
# print(a*b)
# # 输出中的矩阵运算
# print(np.dot(a,b))


#广播机制
# arr = np.random.randint(0,10,size=(10))
# print(arr)
# data = 3
# #所有的数在原来的基础上都加3了
# print(arr + 3)

# 广播的机制有两个特性
# 可以为缺失是的维度补1
#  假定缺失的元素用已有的值填充

# m = np.ones((2,3))
# print(m)
#
# a = np.arange(3)
# # [[0,1,2],[0,1,2]]  和  m进行相加的时候,会自动补全（用已有的元素），在和m进行相加
# print(a)
# print("*****8")
# print(m + a)
# print(m+1)
#

# 三行一列的二维数组
# a = np.arange(0,3,step=1).reshape(3,1)
# print(a)
# b = np.arange(3)
# print(b)
# print("*******")
# # a  和  b  分别扩充如下格式

#    0  1  2
#    0  1  2
#    0  1  2
#
# '''
# print(a + b)
# 得出的结果是如下的值
'''
[[0 1 2]
 [1 2 3]
 [2 3 4]]
'''
# ndarray 的排序
# np.sort ndarray.sort() 都可以，但有区别
# np.sort() 是不改变输入的
# ndarray.sort() 本地处理，不占用空间，但改变输入,指的是自身的排序

# data = np.random.permutation(10)
# print(data)
# print(np.sort(data))
# print(data)
# #ndarray自身的排序，会改变原来的顺序
# data.sort()
# print(data)

# 庞大的一组数， 不是对全部数据感兴趣，只想对其中一小部分排序
data = np.random.permutation(20)
print(data)

#开始部分排序
# partition(data,k),
# 当k正数时候，得到最小的k 个数
#当k为负数的时候，得到最大的k个数
print(np.partition(data,4)[:4])

print(np.partition(data,-4)[-4:])

'''
data =np.random.permutation(100)
print(data)

print(np.partition(data,5)[:5])
'''