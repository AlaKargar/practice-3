count=int(input("please enter the count of your numbers: "))
nums=[]
for i in range (count):
    x=int(input("please enter your num: "))
    nums.append(x)

nums2 = nums[:]
nums2.sort()
if nums2 == nums:
  print("it has sorted")
  print(nums)
  print(nums2)
else: 
    print("it hasn't sorted")
    print("unsorted:", nums)
    print("sorted:", nums2)

    