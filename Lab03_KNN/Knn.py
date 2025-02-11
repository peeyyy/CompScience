#the user will input how many classes there will be
num_classes = int(input("Enter the number of classes: "))
class_labels = {}

#store user-defined class labels
for i in range(num_classes):
    label_name = input(f"Enter name for Class {i}: ")
    class_labels[label_name] = i #this will assign a number to each class

# The user will input a dataset
X_point = []
Y_point = []
n = int(input("Enter number of points: "))

for i in range(n):
    x, y, label = input(f"Enter x, y, and class ({'/'.join(class_labels.keys())}) for point {i+1}: ").split()
    if label not in class_labels:
        print(f"Invalid class name! Please enter one of: {', '.join(class_labels.keys())}")
        exit()
    X_point.append([int(x), int(y)])
    Y_point.append(class_labels[label]) 

# Ask for new point
x, y = input("Enter x and y for new point: ").split()
new_point = [int(x), int(y)]

# Ask for distance metric
metric = input("Enter distance metric (euclidean or manhattan): ").strip().lower()

# Function to calculate Euclidean distance
def euclidean_distance(point_x, point_y):
    distance = 0
    for i in range(len(point_x)):
        distance += (point_y[i] - point_x[i]) ** 2
    return distance ** 0.5  #to solve the square root

# Function to calculate Manhattan distance
def manhattan_distance(point_x, point_y):
    distance = 0
    for i in range(len(point_x)):
        distance += abs(point_x[i] - point_y[i])  # to solve the absolute value
    return distance

# k-NN classifier implementation
def k_nearest_neighbors(X_point, Y_point, X_test, k=3, metric="euclidean"):
    distances = []
    
    # Choose a distance metric
    distance_function = euclidean_distance if metric == "euclidean" else manhattan_distance
    
    # Calculate distances from the test point to all points
    for i in range(len(X_point)):
        dist = distance_function(X_test, X_point[i])
        distances.append((dist, Y_point[i], X_point[i]))  #will store distance with labels
    
    # will sort the distance in an ascending order
    distances.sort(key=lambda x: x[0])

    # Print ranked distances with classes
    print("\nRanked distances from new point:")
    print("Rank | Distance | Point (x, y) | Class")
    print("--------------------------------------")
    for rank, (dist, label, point) in enumerate(distances, start=1):
        class_name = [key for key, value in class_labels.items() if value == label][0]
        print(f"{rank:4} | {dist:.2f}   | ({point[0]},{point[1]})  | {class_name}")
    
    # Get the top k nearest labels
    k_nearest = [label for _, label, _ in distances[:k]]
    
    # Majority vote (find the most common label)
    label_counts = {}
    for label in k_nearest:
        label_counts[label] = label_counts.get(label, 0) + 1
    
    # Get the label with the highest count
    predicted_label = max(label_counts, key=label_counts.get)
    
    return predicted_label

# This function will plot the graph without using any packages
# REMEMBER: This function is only for visualization purposes and may not work well for large datasets
def plot_graph(X_point, Y_point, new_point, predicted_class):
    width = 20  # Graph size
    height = 20
    grid = [['.' for _ in range(width)] for _ in range(height)]
    
    # Get class symbols dynamically
    symbols = ["O", "X", "*", "#", "&", "%", "@", "$", "+", "="]  # Extend if more classes
    class_symbols = {i: symbols[i % len(symbols)] for i in range(len(class_labels))}
    
    # Place training points on the grid
    for i in range(len(X_point)):
        x, y = X_point[i]
        if 0 <= x < width and 0 <= y < height:
            grid[height - y - 1][x] = class_symbols[Y_point[i]]  # this will assign symbol to each class
    
    # Place new point on the grid
    x, y = new_point
    if 0 <= x < width and 0 <= y < height:
        grid[height - y - 1][x] = class_symbols[predicted_class]  # this will mark the predicted class
    
    # it will print the graph
    print("\nGraph (Class symbols):\nREMEMBER: This is only for visualization purposes and may not work well for large datasets")
    for row in grid:
        print(" ".join(row))

    print("\nLegend:")
    for label, index in class_labels.items():
        print(f"{class_symbols[index]} = {label}")

# Predict class
k = int(input("Enter value of k: "))
predicted_class = k_nearest_neighbors(X_point, Y_point, new_point, k, metric)

# Get predicted class label
predicted_label = [key for key, value in class_labels.items() if value == predicted_class][0]

# Print results
print(f"\nPredicted class for point {new_point} using {metric} distance: {predicted_label}")

# Draw graph
plot_graph(X_point, Y_point, new_point, predicted_class)
