# The Stock Span Algorithm is used to find the number of consecutive days before the
# current day for which the stock price was less than or equal to today's price. 
# It helps analyze stock trends and investor confidence.

# Explanation

# Imagine we have stock prices for n days.

# For each day, we want to know: 
# How many days in a row (including today) the price was not lower than today's price.

# Naive approach for each day. look backwards until we find a higher price -> (O(n ** 2)).

# Optimized approach (using stack):
# Use a stack to keep track of indices of days:

# Traverse prices one by one

# While (stack is not empty) and (current price >= price at top of stack) -> pop.
# If stack becomes empty -> span is i + 1
# Otherwise, span is i - [top of stack]

# Push current index onto the stack 
# This reduces time to (O(n)).


def stock_span(prices: list[int]):
    n = len(prices)
    span = [0] * n
    st = []
    
    span[0] = 1
    st.append(0)
    
    for i in range(1, n):
        while st and prices[i] >= prices[st[-1]]:
            st.pop()
            
        if not st:
            span[i] = i + 1
        else:
            span[i] = i - st[-1]
        
        st.append(i)
        
    return span


# Example Usage

prices = [100, 80, 60, 70, 60, 75, 85]

print(f"Stock Span for {prices}, is : {stock_span(prices)}")