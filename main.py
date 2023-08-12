class Solution:

    def maxSubArraySum(self,arr,N):
        
        sum=0
        m=0
        if(max(arr)<=0):
            return max(arr)
        for i in range(0,len(arr)):
            if arr[i]<0:
                m=max(sum,m)
            sum+=arr[i]
            if(sum<0):
                sum=0
        return max(sum,m)