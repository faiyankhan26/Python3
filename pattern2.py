# INDEX BASED PATTERN QUESTIONS OF ARRAYS 

# Find the index of a given element in the array
# class Index:
#     def index_element(self,arr, target):
#         for i in range(len(arr)):
#             if arr[i] == target:
#                 return i
#         return -1

# obj1 = Index()
# print(obj1.index_element([1,2,3,4,5],5)) 

# Print all elements with their index 
# class Element:
#     def print_index(self, arr):
#         for i in range(len(arr)):
#             index = i
#             element = arr[i]
#             print(element,"index is",index)

# obj2 = Element()
# obj2.print_index([1,2,3,4,5])

# Print the index of all even numbers
# class Even:
#     def num_index(self, arr):
#         for i in range(len(arr)):
#             if arr[i] % 2 == 0:
#                 index = i
#                 print(index)

# obj3 = Even()
# obj3.num_index([1,2,3,4,5,6])

# Replace every element with its square
# class Square:
#     def num_square(self,arr):
#         for i in range(len(arr)):
#             arr[i] = arr[i] * arr[i]
#         return arr

# obj4 = Square()
# print(obj4.num_square([1,2,3,4,5]))

# Print elements at even indexes
# class Index:
#     def even_index(self, arr):
#         for i in range(len(arr)):
#             if i % 2 == 0:
#                 print(arr[i])
            
# obj5 = Index()
# obj5.even_index([1,2,3,4,5])