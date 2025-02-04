# Dataset: Car Dataset
data = [
    {'Color': 'Black', 'Brand': 'Ford', 'Gasoline': 'Diesel', 'Status': 'Old'},
    {'Color': 'White', 'Brand': 'BMW', 'Gasoline': 'Regular', 'Status': 'New'},
    {'Color': 'Black', 'Brand': 'BMW', 'Gasoline': 'Regular', 'Status': 'Old'},
    {'Color': 'White', 'Brand': 'Ford', 'Gasoline': 'Diesel', 'Status': 'New'},
    {'Color': 'Black', 'Brand': 'BMW', 'Gasoline': 'Diesel', 'Status': 'Old'},
    {'Color': 'White', 'Brand': 'Ford', 'Gasoline': 'Regular', 'Status': 'New'},
    {'Color': 'Black', 'Brand': 'Ford', 'Gasoline': 'Regular', 'Status': 'Old'},
    {'Color': 'White', 'Brand': 'BMW', 'Gasoline': 'Regular', 'Status': 'New'},
    {'Color': 'Black', 'Brand': 'Ford', 'Gasoline': 'Regular', 'Status': 'Old'},
    {'Color': 'White', 'Brand': 'BMW', 'Gasoline': 'Diesel', 'Status': 'New'}
]

# Step 1: Count occurrences of each class (Prior Probability P(y))
total_samples = len(data)
count_old = sum(1 for item in data if item['Status'] == 'Old')
count_new = sum(1 for item in data if item['Status'] == 'New')

prior_old = count_old / total_samples
prior_new = count_new / total_samples

# Step 2: Compute Likelihood P(x_i | y)
def calculate_likelihood(feature, value, status):
    count_feature_given_status = sum(1 for item in data if item['Status'] == status and item[feature] == value)
    count_status = count_old if status == 'Old' else count_new
    
    # Avoid zero probability issue
    unique_values = set(item[feature] for item in data) 
    smoothed_probability = (count_feature_given_status + 1) / (count_status + len(unique_values))  
    return smoothed_probability

# Step 3: Compute Probability using Naïve Bayes Formula
def naive_bayes_predict(query):
    probability_old = prior_old
    probability_new = prior_new

    for feature, value in query.items():
        likelihood_old = calculate_likelihood(feature, value, 'Old')
        likelihood_new = calculate_likelihood(feature, value, 'New')
        
        probability_old *= likelihood_old
        probability_new *= likelihood_new

    return 'Old' if probability_old > probability_new else 'New'

while True:
    print("\n PREDICTION IF THE CAR IS OLD OR NEW ")
    print("Enter the car's details:\n")

    # User Input
    color = input("Color (Black/White): ").strip()
    brand = input("Brand (Ford/BMW): ").strip()
    gasoline = input("Gasoline (Diesel/Regular): ").strip()

    result = {
        'Color': color,
        'Brand': brand,
        'Gasoline': gasoline
    }

    # Make a prediction
    prediction = naive_bayes_predict(result)
    print(f"\nPrediction: The car is {prediction}.")

    # Ask user if they want to run another prediction
    terminate = input("\nWould you like to predict again? (yes/no): ").strip().lower()
    if terminate != "yes":
        print("Thank you for using this program!")
        break
