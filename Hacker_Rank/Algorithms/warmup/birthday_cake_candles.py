'''
/*
 * @Author: Rajat  
 * @Date: 2020-12-22 15:13:46 
 * @Last Modified by: Rajat
 * @Last Modified time: 2020-12-22 15:25:10
 */
'''

def birthdayCakeCandles(candles):
    # Write your code here
    tallest_candle = max(candles)
    return candles.count(tallest_candle)


if __name__ == '__main__':

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(result)