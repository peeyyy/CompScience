import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

def perform_regression():
    try:
        # Get user inputs and convert them into NumPy arrays
        X = np.array(list(map(float, entry_sizes.get().split())))
        Y = np.array(list(map(float, entry_prices.get().split())))

        # Ensure both inputs have the same length
        if len(X) != len(Y):
            messagebox.showerror("Error", "Number of sizes and prices must be equal!")
            return

        n = len(X)  # Number of data points

        # Compute summations needed for slope and intercept
        sum_x = np.sum(X)
        sum_y = np.sum(Y)
        sum_xy = np.sum(X * Y)
        sum_x2 = np.sum(X ** 2)

        # Compute slope (b) using the formula
        b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
        
        # Compute intercept (a)
        a = (sum_y - b * sum_x) / n

        # Predict Y values using the regression equation y = a + bx
        Y_pred = a + b * X

        # Compute Mean Squared Error (MSE)
        mse = np.sum((Y - Y_pred) ** 2) / n

        # Compute R² (Coefficient of Determination)
        ss_total = np.sum((Y - np.mean(Y)) ** 2)
        ss_residual = np.sum((Y - Y_pred) ** 2)
        r2 = 1 - (ss_residual / ss_total)

        # Display results in the GUI
        result_text.set(f"Slope (b): {b:.4f}\nIntercept (a): {a:.4f}\nMSE: {mse:.4f}\nR²: {r2:.4f}")

        # Plot Regression Line
        plt.figure(figsize=(10, 5))
        plt.scatter(X, Y, color='blue', label='Actual Prices')
        plt.plot(X, Y_pred, color='red', label='Regression Line')
        plt.xlabel('House Size (sq ft)')
        plt.ylabel('House Price ($1000)')
        plt.title('Linear Regression: House Price Prediction')
        plt.legend()
        plt.show()

        # Residual Plot
        residuals = Y - Y_pred
        plt.figure(figsize=(10, 5))
        plt.scatter(X, residuals, color='purple', label='Residuals')
        plt.axhline(y=0, color='black', linestyle='dashed')
        plt.xlabel('House Size (sq ft)')
        plt.ylabel('Residuals')
        plt.title('Residual Plot')
        plt.legend()
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Invalid input! Enter numeric values separated by spaces.")

# GUI frame
frame = tk.Tk()
frame.title("Linear Regression: House Price Predictor")
frame.geometry("400x300")

# Labels and entry fields
tk.Label(frame, text="Enter house sizes (sq ft):").pack()
entry_sizes = tk.Entry(frame, width=50)
entry_sizes.pack()

tk.Label(frame, text="Enter house prices ($1000):").pack()
entry_prices = tk.Entry(frame, width=50)
entry_prices.pack()

# Result display
result_text = tk.StringVar()
tk.Label(frame, textvariable=result_text, fg="blue").pack()

# Compute Button
tk.Button(frame, text="Compute Regression", command=perform_regression).pack()

# Tkinter loop
frame.mainloop()