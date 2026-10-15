
# Social Network using Adjacency Matrix

n = int(input("Enter number of users: "))

names = []

for i in range(n):
    name = input(f"Enter user {i + 1} name: ")
    names.append(name)

# Create an adjacency matrix
matrix = [[0] * n for _ in range(n)]

# Add friendship connections
print("\nEnter friendship connections (1 = Yes, 0 = No):")

for i in range(n):
    for j in range(i + 1, n):
        choice = int(input(
            f"Are {names[i]} and {names[j]} friends? "
        ))

        if choice == 1:
            matrix[i][j] = 1
            matrix[j][i] = 1

# Display adjacency matrix
print("\nAdjacency Matrix:")
print("     ", end="")

for name in names:
    print(f"{name:<10}", end="")

print()

for i in range(n):
    print(f"{names[i]:<5}", end=" ")
    for j in range(n):
        print(f"{matrix[i][j]:<10}", end="")
    print()

# Display friends
print("\nFriendship Connections:")

for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] == 1:
            print(f"{names[i]} - {names[j]}")
