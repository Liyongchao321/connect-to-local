def maxProfit(prices):
    if len(prices) in (0,1):
        return 0
    i = len(prices)-1
    profit = 0
    while i>0:       
        temp = prices[i]
        # print('neighbor values: ', temp, prices[i-1])
        if prices[i-1] > temp:
            i = i-1
        else:
            profit = profit + prices[i] - prices[i-1]
            # print('profit: ',profit)
            i = i-1
    return profit


if __name__ == '__main__':
    input_1 = [7,1,5,3,6,4]
    input_2 = [1,2,3,4,5]
    input_3 = [7,6,4,3,1]
    print(maxProfit(input_1))
    print(maxProfit(input_2))
    print(maxProfit(input_3))
