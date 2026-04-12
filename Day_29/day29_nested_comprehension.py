# Day 29: Nested List Comprehension 🛡️
# Mission: Flattening a Matrix (2D to 1D)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Traditional way (for reference):
# flattened = []
# for row in matrix:
#     for num in row:
#         flattened.append(num)

# Pro way: Nested List Comprehension
flattened = [num for row in matrix for num in row]

print(f"Original Matrix: {matrix}")
print(f"Flattened List: {flattened}")

# Advanced: Filtering inside nested comprehension
# Only even numbers from the matrix
evens = [num for row in matrix for num in row if num % 2 == 0]
print(f"Even numbers from matrix: {evens}")

input("\nPress enter to exit...")
