import matplotlib.pyplot as plt
import numpy as np

# Example data: Replace these with actual data from your model
epochs = np.arange(1, 101)  # Example epochs from 1 to 100
training_accuracies = np.random.uniform(0.7, 0.95, size=100)  # Example training accuracies
validation_accuracies = np.random.uniform(0.65, 0.93, size=100)  # Example validation accuracies

# Create a plot for the learning curve
plt.figure(figsize=(12, 6))

# Plot training accuracy
plt.plot(epochs, training_accuracies, label='Training Accuracy', color='blue')

# Plot validation accuracy
plt.plot(epochs, validation_accuracies, label='Validation Accuracy', color='green')

# Add title and labels
plt.title('Learning Curve')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')

# Add legend
plt.legend()

# Show the plot
plt.ylim(0, 1)  # Set y-axis limit from 0 to 1
plt.show()