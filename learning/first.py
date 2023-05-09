# ######################################## if statement and input
# num = int(input("enter any number: "))
# if num <= 10:
#     print("lower numbers")
# elif num == 50:
#     print("middle number")
# else:
#     print("higher numbers")

# ######################################## for loop
# list = ['red', 'blue', 'green', 'yellow', 'white', 'black']
# for index, color in enumerate(list):
#     print(index, color)

# a = 0
# for i in range(10):
#     a += 1
#     print('i=',i,'a=',a)
#     if a==5:
#         break

# for i in range(5):
#     if i == 0 :
#         continue
#     print('num:', i)


# my_list = [1, 4, 20, 50, 100, 2000, 10000, 6]
# result = 1
# for i in my_list:
#     result *= i
# print(result)
# # return result

# ######################################## while loop
# i = 10
# while i <= 10:
#     i -= 1
#     if i == 5:
#         break
#     print(i)

# nums = [1,2,3,4,5,6,7,8,9]
# # while nums:
# #     print(nums.pop())
# # while len(nums) >= 5:
# #     print(nums.pop())

# ######################################## opening files
# f = open('prompts.txt', 'r')
# print(f.read())

# f = open('prompts.txt', 'r')
# for line in f:
#     print(line)

# def read_files(file_name, no_lines):
#     from itertools import islice
#     with open(file_name) as f:
#         for line in islice(f, no_lines):
#             print(line)


# read_files('prompts.txt', 3)
