def merge(nums1,m,nums2,n):
    m -=1
    n -=1
    index = len(nums1) -1
    while n >= 0:
        if m >=0 and nums1[m] > nums2[n]:
            nums1[index] = nums1[m]
            m-=1
        else:
            nums1[index] = nums2[n]
            n-=1
        index-=1
    print(nums1)

n1 = [1,2,3,0,0,0]
m = 3
n2 = [2,5,6]
n = 3
print(merge(n1,m,n2,n))
