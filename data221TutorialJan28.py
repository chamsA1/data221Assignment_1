#Practice Problems - Week 3 Ex 1:
# def filterAndSquare(nums):
#     x = []
#     for num in nums:
#         if num % 2 == 0:
#             num **= 2
#             x.append(num)
#     return x
# # nums =  [1, 2, 3, 4, 5, 6]
# nums = [-4, -3, 0, 7, 8]
# print(filterAndSquare(nums))


#Practice Problems - Week 3 Ex 2:
def uniqueInOrder(items):
    x = []
    for item in items:
        if item not in  item:
            x.append(item)
    return x
list = ["a", "b", "a", "c", "b"]
print(uniqueInOrder(list))
