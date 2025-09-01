from typing import List


def buy_and_sell(arr: List[int]) -> int:
    """i will add this later"""
    profit = 0
    smallest = arr[0]
    largest = arr[0]

    for i in arr:
        if i < smallest:
            smallest = i

        elif i > largest:
            largest = i
        profit = max(largest - smallest, profit)

    return profit


def buy_and_sell_2(prices: List[int]) -> int:
    profit = 0
    smallest = prices[0]

    for idx, price in enumerate(prices):
        smallest = min(smallest, price)
        largest = max(prices[idx:])
        profit = max(largest - smallest, profit)
    return profit


def main():
    prices = [1, 7, 1, 5, 3, 6, 4]
    prices_2 = [8, 7, 6, 4, 3, 1]
    print(buy_and_sell_2(prices))

    print(buy_and_sell_2(prices_2))


if __name__ == "__main__":
    main()
