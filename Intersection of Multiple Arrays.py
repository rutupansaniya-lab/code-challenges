class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        max_length_row=[]
        l=len(nums)

        for i in nums:
            a=len(i)
            max_length_row.append(a)
        
        ref=max(max_lenght_row)
        index_of_max=max_length_row.index(ref)
        list2=[]

        for i in range(len(nums(index_of_max))):
            flag=0

            for j in nums:
                if nums[i] not in j:
                    flag=1

            if flag==0:
                list2.append(nus[i])
                
        return list2
    