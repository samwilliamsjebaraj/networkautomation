class Solution(object):
    def twosum(self,nums,target):
        print len(nums)
        if len(nums)!=0 or len(nums)!=1:
            for x in range(0,len(nums)):
                for y in range(1,len(nums)):
                    if nums[x]+nums[y]==target:
                        return [x,y]
        elif len(nums)==0:
            if nums[0]==target:
                return [0]
        elif len(nums)==1:
            if nums[0]+nums[1]==target:
                return [0,1]

if __name__=="__main__":
    s=Solution()
    t=0
    n=[0,0]
    print (s.twosum(n,t))
