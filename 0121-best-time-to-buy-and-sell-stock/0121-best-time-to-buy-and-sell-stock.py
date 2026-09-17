class Solution(object):
    def maxProfit(self, prices):
        minindex = 0
        profit = 0

        for i in range(1, len(prices)):

            if prices[i] < prices[minindex]:
                minindex = i

            else:
                current_profit = prices[i] - prices[minindex]

                if current_profit > profit:
                    profit = current_profit

        return profit