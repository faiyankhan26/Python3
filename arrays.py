# from numpy import * 

# # Find the largest element in an array
# class Largest:
#     def largest_name(self,arr):
#         largest = arr[0]
#         for num in arr:
#             if num > largest:
#                 largest = num
#         return largest

# obj = Largest()
# print(obj.largest_name([1,2,3,4,5,6]))


# # Find the smallest element in an array
# class Smallest:
#     def smallest_name(self, arr):
#         smallest = arr[0]
#         for num in arr:
#             if num < smallest:
#                 smallest = num
#         return smallest

# obj2 = Smallest()
# print(obj2.smallest_name([1,2,3,4,5,6]))

# # Find the sum of all elements in an array
# class Element:
#     def sum_element(self,arr):
#         total = 0
#         for num in arr:
#             total += num
#         return total

# obj3 = Element()
# print(obj3.sum_element([1,2,3,4,5,6]))

# # Find the average of array elements
# class Avg:
#     def avg_number(self, arr):
#         total = 0
#         for num in arr:
#             total += num
#             average = total / len(arr)
#         return average

# obj4 = Avg()
# print(obj4.avg_number([1,2,3,4,5]))

# # Count even numbers in the array
# class Even:
#     def even_number(self, arr):
#         count = 0
#         for num in arr:
#             if num % 2 == 0:
#                 count += 1
#         return count
    
# obj5 = Even()
# print(obj5.even_number([1,2,3,4,5,6]))

# # Count odd numbers in the array
# class Odd:
#     def odd_number(self, arr):
#         count = 0
#         for num in arr:
#             if num % 2 != 0:
#                 count += 1
#         return count

# obj6 = Odd()
# print(obj6.odd_number([1,2,3,4,5,6]))

# # Print array in reverse order
# class Reverse:
#     def reverse_array(self, arr):
#         array = []
#         for i in range(len(arr)-1,-1,-1):
#             array.append(arr[i])
#         return array

# obj7 = Reverse()
# print(obj7.reverse_array([1,2,3,4,5]))

# # Find the second largest element
# class Top:
#     def second_highest(self, arr):
#         largest = arr[0]
#         second_largest = arr[0]
#         for num in arr:
#             if num > largest:
#                 second_largest = largest
#                 largest = num
#             elif num > second_largest and num != largest:
#                 second_largest = num
#         return second_largest

# obj8 = Top()
# print(obj8.second_highest([1,2,3,4,5,6]))

# Check if a number exists in the array
# class Exist:
#     def num_exist(self, arr, target_num):

#         for num in arr:
#             if num == target_num :
#                 return True
            
#         return False
    
# obj9 = Exist()
# print(obj9.num_exist([1,2,3,4,5], 7))

# Find the index of a given element
# class Index:
#     def find_index(self, arr, target):
#         for i in range(len(arr)):
#             if arr[i] == target:
#                 return i
            
#         return -1
    
# obj10 = Index()
# print(obj10.find_index([1,2,3,4,5,6], 11));

# Count how many times an element appears
# class Count:
#     def count_number(self, arr, target):
#         count = 0
#         for num in arr:
#             if num == target:
#                 count += 1
#         return count

# obj11 = Count()
# print(obj11.count_number([1,2,3,2,5,6,2,8], 2));

# Find the maximum difference between two elements 
