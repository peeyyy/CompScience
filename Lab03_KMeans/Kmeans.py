# the user will input number of points
n = int(input("Enter the number of data points: "))
data = []

# Get user-defined data points
for i in range(n):
    x, y = map(float, input(f"Enter x, y for point {i+1}: ").split())
    data.append([x, y])

#function to calculate distance using the given formula
def distance(p, q):
    return ((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2) ** 0.5  # Using sqrt(q1 - p1)^2 + (q2 - p2)^2

#to initialize the first k points as centroids
def initialize_centroids(data, k):
    return data[:k]  # this take the first k data points

# to assign each point to the closest centroid
def assign_clusters(data, centroids):
    clusters = [[] for _ in range(len(centroids))]  #it creates empty cluster lists
    assignments = []  #stores the cluster index for each data point
    
    for point in data:
        distances = [distance(point, centroid) for centroid in centroids]
        closest_index = distances.index(min(distances))  #this finds the nearest centroid
        clusters[closest_index].append(point)  #assign point to that cluster
        assignments.append(closest_index)
    
    return clusters, assignments

# compute new centroids
def compute_centroids(clusters):
    new_centroids = []
    
    for cluster in clusters:
        if cluster: 
            centroid = [sum(dimension) / len(cluster) for dimension in zip(*cluster)]  # Compute mean
            new_centroids.append(centroid)
    
    return new_centroids

# to display clustering information in a table
def display_iteration_table(data, centroids, old_assignments, new_assignments, iteration):
    print(f"\nIteration {iteration} Table:")
    print("=" * (40 + len(centroids) * 12))
    print(" Data Point | " + " | ".join([f"Dist to C{i+1}" for i in range(len(centroids))]) + " | Current Cluster | New Cluster ")
    print("-" * (40 + len(centroids) * 12))
    
    for i, point in enumerate(data):
        distances = [distance(point, centroid) for centroid in centroids]
        distance_str = " | ".join([f"{dist:.2f}" for dist in distances])
        print(f" ({point[0]:.1f},{point[1]:.1f})  | {distance_str} | {old_assignments[i]} | {new_assignments[i]} ")
    
    print("=" * (40 + len(centroids) * 12))

# k-Means clustering algorithm 
def k_means(data, k, max_iterations=100):
    centroids = initialize_centroids(data, k)  #1st: Initialize centroids
    old_assignments = [-1] * len(data)  #this track previous cluster assignments
    
    for iteration in range(1, max_iterations + 1):
        clusters, new_assignments = assign_clusters(data, centroids)  # 2nd: Assign points to clusters
        display_iteration_table(data, centroids, old_assignments, new_assignments, iteration)
        new_centroids = compute_centroids(clusters)  #3rd: Compute new centroids
        
        if new_centroids == centroids:  #Stop if centroids don't change
            break
        
        centroids = new_centroids  # this update the centroids
        old_assignments = new_assignments[:]  #will update the old assignments
    
    return clusters, centroids

# Plotting clusters in ASCII format
def plot_graph(data, clusters, centroids):
    width, height = 20, 20  # Grid size
    grid = [['.' for _ in range(width)] for _ in range(height)]
    
    # Scale points to fit grid
    def scale_point(point):
        return (int(point[0] * (width - 1) / 10), int(point[1] * (height - 1) / 10))

    # Assign symbols for different clusters
    cluster_symbols = ["O", "X", "~", "#", "&", "%", "@", "$", "+", "="]
    
    # Plot data points
    for i, cluster in enumerate(clusters):
        symbol = cluster_symbols[i % len(cluster_symbols)]
        for point in cluster:
            x, y = scale_point(point)
            grid[height - y - 1][x] = symbol  # Flip y-axis for correct display

    # Plot centroids
    for centroid in centroids:
        x, y = scale_point(centroid)
        grid[height - y - 1][x] = '*'  # Use * for centroids
    
    # Print the grid
    print("\nCluster Visualization (ASCII Graph):\nREMEMBER: This graph is a visual representation of the clusters and centroids. It is not to scale.")
    for row in grid:
        print(" ".join(row))
    
    # Print legend
    print("\nLegend:")
    for i, cluster in enumerate(clusters):
        print(f"{cluster_symbols[i % len(cluster_symbols)]} = Cluster {i+1}")
    print("* = Centroid")

# Get user-defined k value
k = int(input("Enter the number of clusters (k): "))

# Run k-Means algorithm
clusters, centroids = k_means(data, k)

# Display results
print("\nFinal Clusters:")
for i, cluster in enumerate(clusters):
    print(f"Cluster {i+1}: {cluster}")

print("\nFinal Centroids:")
for i, centroid in enumerate(centroids):
    print(f"Centroid {i+1}: {centroid}")

# Plot ASCII graph
plot_graph(data, clusters, centroids)
