import numpy as np

a = np.array([1, 2, 3])

print(a.shape)

b = np.array([[1, 2, 3],

        [4, 5, 6]])

print(b.shape)

c = np.array([[[1, 2],

               [3, 4]]])

print(c.shape)

c = np.array([[[1, 2],[3,4]],

    [[5, 6],[7, 8]]])

print(c.shape)

sales = np.array([

    [100, 120, 90],

    [110, 130, 95],

    [105, 125, 100]

])

print("每天銷售:", sales.sum(axis=1))

print("每商品銷售:", sales.sum(axis=0))

print("總銷售:", sales.sum())

a = np.array([10, 20, 30, 40, 50])

print(a[0])

a = np.array([10, 20, 30, 40, 50])

print(a[0:4:2])

a = np.array([

[10, 20, 30],

[40, 50, 60],

[70, 80, 90]

])

print(a[1])

print(a[:,2])
