# Function to generate the window column panes spaced out multiples of 4
def generate_window_panes(num_panes, spacing):
    return [x * spacing for x in range(num_panes)]

# Function to generate the array of strings spaced out in base 2
def generate_base2_strings(start, end):
    base2_strings = []
    current_value = start
    while current_value <= end:
        base2_strings.append(bin(current_value)[2:])  # Convert to binary and remove '0b' prefix
        current_value *= 2
    return base2_strings

# Create the structure array
window_panes = generate_window_panes(6, 4)
base2_strings = generate_base2_strings(25, 1600)

# Print the structure array
print("Window Panes (x dimension):", window_panes)
print("Base2 Strings:", base2_strings)