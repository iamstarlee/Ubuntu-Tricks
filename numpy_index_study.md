# What does -1 mean in numpy reshape?
numpy allow us to give one of new shape parameter as -1 (eg: (2,-1) or (-1,3) but not (-1, -1)). It simply means that it is an unknown dimension and we want numpy to figure it out. And numpy will figure this by looking at the 'length of the array and remaining dimensions' and making sure it satisfies the above mentioned criteria.
Now see the example.
```
z = np.array([[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]])
z.shape
(3, 4)
```
Now trying to reshape with (-1) . Result new shape is (12,) and is compatible with original shape (3,4)
```
z.reshape(-1)
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
```
Now trying to reshape with (-1, 1) . We have provided column as 1 but rows as unknown . So we get result new shape as (12, 1).again compatible with original shape(3,4)
```
z.reshape(-1,1)
array([[ 1],
   [ 2],
   [ 3],
   [ 4],
   [ 5],
   [ 6],
   [ 7],
   [ 8],
   [ 9],
   [10],
   [11],
   [12]])
```
The above is consistent with numpy advice/error message, to use reshape(-1,1) for a single feature; i.e. single column.
New shape as (-1, 2). row unknown, column 2. we get result new shape as (6, 2)
```
z.reshape(-1, 2)
array([[ 1,  2],
   [ 3,  4],
   [ 5,  6],
   [ 7,  8],
   [ 9, 10],
   [11, 12]])
```