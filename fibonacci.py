def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage
n = int(input("Enter number of terms: "))
print("🔢 Fibonacci sequence:", fibonacci_sequence(n))
def fibonacci_nth(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Example usage
n = int(input("Enter the position (n): "))
print(f"📍 The {n}th Fibonacci number is: {fibonacci_nth(n)}")
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage
n = int(input("Enter the position (n): "))
print(f"🌀 The {n}th Fibonacci number is: {fibonacci_recursive(n)}")
