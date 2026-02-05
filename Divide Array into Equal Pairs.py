class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # create dict having count of each number in the array
        number_count={}
        
        for i in nums:
        
            if i not in number_count:
                number_count[i]=1
            else:
                number_count[i]+=1
        
        for i in number_count:
        
            if(number_count[i]%2!=0):
                return  
             
        
        return True
            



            