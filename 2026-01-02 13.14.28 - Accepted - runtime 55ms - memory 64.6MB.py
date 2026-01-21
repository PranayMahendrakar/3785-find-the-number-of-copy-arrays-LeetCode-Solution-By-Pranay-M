class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        n = len(original)
        
        # For copy[i] = copy[0] + (original[i] - original[0])
        # We need: bounds[i][0] <= copy[0] + diff[i] <= bounds[i][1]
        # So: bounds[i][0] - diff[i] <= copy[0] <= bounds[i][1] - diff[i]
        
        lo = bounds[0][0]  # lower bound for copy[0]
        hi = bounds[0][1]  # upper bound for copy[0]
        
        for i in range(1, n):
            diff = original[i] - original[0]
            # copy[0] >= bounds[i][0] - diff
            # copy[0] <= bounds[i][1] - diff
            lo = max(lo, bounds[i][0] - diff)
            hi = min(hi, bounds[i][1] - diff)
            
            if lo > hi:
                return 0
        
        return hi - lo + 1