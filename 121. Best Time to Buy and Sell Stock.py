# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# class Solution(object):
#     def maxProfit(self, prices):
#         cur_min = prices[0]
#         cur_max = 0
#         max_profit = 0
#         for i in prices[1:]:
#             if cur_min >= i:
#                 cur_min = i
#                 cur_max = 0
#             elif cur_min < i:
#                 if cur_max < i:
#                     cur_max = i
#             else:
#                 return 0
#             if cur_max > 0:
#                 new_max_profit = cur_max - cur_min
#                 if max_profit < new_max_profit:
#                     max_profit = new_max_profit
#         if max_profit>0:
#             return max_profit
#         else: 
#             return 0
    
class Solution(object):
    def maxProfit(self, prices):
        buying_price = prices[0]
        selling_price = 0
        max_profit = 0
        for i in prices[1:]:
            if buying_price >= i:
                buying_price = i
                selling_price = 0
            elif buying_price < i:
                if selling_price < i:
                    selling_price = i
            else:
                return 0

            if selling_price > 0:
                today_s_profit = selling_price - buying_price
                if max_profit < today_s_profit:
                    max_profit = today_s_profit
        if max_profit>0:
            return max_profit
        else: 
            return 0


prices = [7,1,5,3,6,4] #result 5
# # sample test cases
# 5,2,2,2,4   //2
# 5,1,4,2,7   //6
# 7,6,4,3,1   //0
s = Solution()
print(s.maxProfit(prices))
