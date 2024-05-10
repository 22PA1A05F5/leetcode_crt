class Solution:
    def twoSum(self,num,target):
        n=len(num)
        for i in range(n):
            for j in range(i+1,n):
                if num[i] + num[j] ==target:
                    return[i,j]
        return None
        