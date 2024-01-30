def fibonacci_series(n,sequence=[0,1]):
    if len(sequence)<n:
        next_num = sequence[-1]+sequence[-2]
        sequence.append(next_num)
        fibonacci_series(n,sequence)
    return sequence

recursion_fibonacci_series = fibonacci_series(10)
print(recursion_fibonacci_series)
    
