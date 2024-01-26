# Print a downward Half-Pyramid Pattern of Star (asterisk)

# Pseudocode

# Set rows to 5
rows = 5
# Create for loop
for i in range(rows, 0, -1):
     # Outer loop to iterate through each row from top to bottom
    for j in range(1, i + 1):
    # Inner loop to print stars in each row
        print("*", end= " ")
    # Move to the next line after printing stars in the current row
    print()
