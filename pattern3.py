# Check if the array is sorted in increasing order.
# class Sorted:
#     def inc_order(self, arr):
#         for i in range(len(arr)-1):
#             if arr[i] > arr[i+1]:
#                 return False
#         return True 

# obj = Sorted()
# print(obj.inc_order([1,2,3,4,5]))

# Check if the array is sorted in decreasing order
# class Sorted:
#     def desc_sorted(self,arr):
#         for i in range(len(arr)-1):
#             if arr[i] < arr[i+1]:
#                 return False
#             return True 
        
# obj = Sorted()
# print(obj.desc_sorted([1,2,3,4,5]))

# Count how many increasing pairs exist (arr[i] < arr[i+1])
# class Pair:
#     def inc_pair(self,arr):
#         count = 0
#         for i in range(len(arr)-1):
#             if arr[i] < arr[i+1]:
#                 count = count + 1
#         return count

# obj = Pair()
# print(obj.inc_pair([1,2,3,4,5,5,4,3,2,1]))

# Count how many decreasing pairs exist (arr[i] > arr[i+1])
# class Pair:
#     def desc_pair(self,arr):
#         count = 0
#         for i in range(len(arr)-1):
#             if arr[i] > arr[i+1]:
#                 count = count + 1
#         return count
    
# obj = Pair()
# print(obj.desc_pair([1,2,3,4,5,5,4,3,2,1]))

# Print the difference between consecutive elements 
class Difference:
    def conse_element(self,arr):
        difference = 0
        for i in range(len(arr)-1):
            difference = arr[i+1] - arr[i]
            print(difference)

obj = Difference()
obj.conse_element([541,944,956,797,491])