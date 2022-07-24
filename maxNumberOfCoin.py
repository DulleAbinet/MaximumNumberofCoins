class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total = 0
        idx = len(piles)//3
        
        while idx < len(piles):
            total += piles[idx]
            idx += 2
            
        return total
