# #1st Method
# count=0
# with open(r"Exersice2.txt", "r") as f:
#     data=f.read()
#     num=""
#     for i in range(len(data)):
#         if(data[i]==","):
#             if(int(num)%2==0):
#                 count+=1
#                 num=""
#         else:
#             num+=data[i]
# print(count)

#2nd method
count=0
with open(r"Exersice2.txt", "r") as f:
    data=f.read()
    nums=data.split(",")
    print(nums)
    for val in nums:
        if(int(val)%2==0):
            count+=1
print(count)