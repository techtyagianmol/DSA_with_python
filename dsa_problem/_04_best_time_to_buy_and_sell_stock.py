# best time to buy and sell stock

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf') 
         # start with infinity (so first price will always be smaller)
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price 
                 # update min price if we find smaller
            elif price - min_price > max_profit:
                max_profit = price - min_price 
                 # update max profit

        return max_profit

        # t.c -> O(n)
        # s.c -> O(1)