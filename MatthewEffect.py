import random
import matplotlib.pyplot as plt

def assign_colors(n):
    # Create a list of numbers from 1 to n
    numbers = list(range(1, n + 1))

    # Create a list of colors with equal numbers of red and blue
    colors = ['red'] * (n // 2) + ['blue'] * (n // 2)

    # If n is odd, add one random color (red or blue)
    if n % 2 != 0:
        colors.append(random.choice(['red', 'blue']))

    # Shuffle the colors randomly
    random.shuffle(colors)

    # Assign colors to numbers
    colored_numbers = list(zip(numbers, colors))

    return colored_numbers

def plot_colored_circles(box, title):
    # Create a plot
    fig, ax = plt.subplots(figsize=(10, 1))

    # Plot each item in the box as a colored circle
    for i, (item, color) in enumerate(box):
        circle = plt.Circle((i + 0.5, 0.5), 0.4, color=color, alpha=0.7)
        ax.add_patch(circle)
        plt.text(i + 0.5, 0.5, str(item), ha='center', va='center', fontsize=8, color='white')

    # Set plot limits and remove axes
    ax.set_xlim(0, len(box))
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    # Set the title of the plot
    plt.title(title)

    # Show the plot
    plt.show()

def calculate_percentages(box):
    # Calculate the percentage of red and blue balls in the box
    total_balls = len(box)
    red_count = sum(1 for _, color in box if color == 'red')
    blue_count = total_balls - red_count

    red_percentage = (red_count / total_balls) * 100
    blue_percentage = (blue_count / total_balls) * 100

    return red_percentage, blue_percentage

# Number of numbers
n = 1000  # You can change this to any number

# Assign colors to numbers
colored_numbers = assign_colors(n)

# Number of iterations
num_iterations = 10  # You can change this to any number

# Initialize the second box with one red and one blue ball
second_box = [('A', 'red'), ('B', 'blue')]


red_percentages = []
blue_percentages = []

# Loop for the specified number of iterations
for iteration in range(num_iterations):
    print(f"\nIteration {iteration + 1}:")

    # Randomly select one ball from the second box
    selected_ball = random.choice(second_box)
    selected_color = selected_ball[1]

    # Print the selected ball
    print("Selected ball color:", selected_color)

    # Add a new ball of the same color from the first box to the second box
    # Find a ball with the selected color in the first box
    new_ball = None
    for ball in colored_numbers:
        if ball[1] == selected_color:
            new_ball = ball
            break

    if new_ball:
        second_box.append(new_ball)
        print("Added ball color:", selected_color)
    else:
        print("No more balls of this color in the first box!")

    # Calculate and print the percentages of red and blue balls in the second box
    red_percentage, blue_percentage = calculate_percentages(second_box)
    print(f"Red balls: {red_percentage:.2f}%, Blue balls: {blue_percentage:.2f}%")

    # Plot the second box after adding the new ball
    plot_colored_circles(second_box, f"Second Box after iteration {iteration + 1}")
    # Store the percentages after each iteration
    red_percentages.append(red_percentage)
    blue_percentages.append(blue_percentage)




# Plot the previously stored results
plt.figure(figsize=(10, 5))
plt.plot(range(1, num_iterations + 1), red_percentages, label='Red Percentage', color='red', marker='o')
plt.plot(range(1, num_iterations + 1), blue_percentages, label='Blue Percentage', color='blue', marker='s')

plt.xlabel('Iterations')
plt.ylabel('Percentage')
plt.title('Red and Blue Percentage Evolution')
plt.legend()
plt.grid(True)
plt.show()