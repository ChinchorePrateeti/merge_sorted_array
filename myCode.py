#merge sorted array

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

#merging the array to get [1,2,3,2,5,6]
k = 0
for index in range(len(nums1)):
    if nums1[index] == 0:
        nums1[index] = nums2[k]
        k += 1
    if k >= n:
        break
# print(nums1)

#arranging the elements in nums1 in ascending order
nums1.sort()
print(nums1)



