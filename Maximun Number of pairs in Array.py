class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:

        n=len(nums)
        
        if(n==0):
            return [0,1]
        
        pair=0
        odd = set()
        
        for num in nums:
            
            if num in odd:
                odd.remove(num)
                pair=pair+1
            else:
                odd.add(num)

        no=len(odd)
        Ans=[pair,no]
      
      
        return Ans
        