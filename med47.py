# given a collection of numbers, nums, that might contain duplicates,
# return all possible unique permutations in any order

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        results = []
        
        def backtrack(curCombo, counter):
            
            # if we're done, add to results
            if len(curCombo) == len(nums):
                results.append(list(curCombo))
                return
            
            # otherwise find the next digit to add to curCombo
            for num in counter:
                
                if counter[num] > 0:
                    
                    # add valid candidate num
                    curCombo.append(num)
                    counter[num] -= 1
                    
                    # countinue building curCombo
                    backtrack(curCombo, counter)
                    
                    # backtrack one step
                    curCombo.pop()
                    counter[num] += 1
            
        backtrack([], Counter(nums))
            
        return results