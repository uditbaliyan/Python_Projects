from typing import List


def buy_and_sell(prices: List[int]) -> int:
    """
    Calculate the maximum profit from a single buy and sell operation.
    This approach updates both the smallest and largest values seen so far,
    and computes profit at each step.

    Args:
        prices (List[int]): List of stock prices.

    Returns:
        int: Maximum profit possible.
    """
    if not prices:
        return 0

    profit = 0
    smallest = prices[0]
    largest = prices[0]

    for price in prices:
        if price < smallest:
            smallest = price
            largest = price  # Reset largest when new smallest is found
        elif price > largest:
            largest = price
        profit = max(profit, largest - smallest)

    return profit


def buy_and_sell_2(prices: List[int]) -> int:
    """
    Brute-force inspired approach that checks the max future price at each index.
    Less efficient due to repeated slicing and max calculations.

    Args:
        prices (List[int]): List of stock prices.

    Returns:
        int: Maximum profit possible.
    """
    if not prices:
        return 0

    profit = 0
    smallest = prices[0]

    for i in range(len(prices)):
        smallest = min(smallest, prices[i])
        future_max = max(
            prices[i:], default=prices[i]
        )  # Avoids ValueError on empty slices
        profit = max(profit, future_max - smallest)

    return profit


def buy_and_sell_3(prices: List[int]) -> int:
    """
    Optimized single-pass approach.
    Tracks the minimum price so far and calculates profit at each step.

    Args:
        prices (List[int]): List of stock prices.

    Returns:
        int: Maximum profit possible.
    """
    if not prices:
        return 0

    profit = 0
    min_price = prices[0]

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


def main() -> None:
    """
    Test different stock price scenarios using all implementations.
    """
    prices_1 = [7, 1, 5, 3, 6, 4]
    prices_2 = [7, 6, 4, 3, 1]

    print("Testing buy_and_sell_3:")
    print(f"Prices: {prices_1} -> Max Profit: {buy_and_sell_3(prices_1)}")
    print(f"Prices: {prices_2} -> Max Profit: {buy_and_sell_3(prices_2)}")

    print("\nTesting buy_and_sell:")
    print(f"Prices: {prices_1} -> Max Profit: {buy_and_sell(prices_1)}")
    print(f"Prices: {prices_2} -> Max Profit: {buy_and_sell(prices_2)}")

    print("\nTesting buy_and_sell_2:")
    print(f"Prices: {prices_1} -> Max Profit: {buy_and_sell_2(prices_1)}")
    print(f"Prices: {prices_2} -> Max Profit: {buy_and_sell_2(prices_2)}")


if __name__ == "__main__":
    main()
