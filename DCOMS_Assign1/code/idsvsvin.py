import matplotlib.pyplot as plt
import pandas as pd
import os

# Read data from CSV file
csv_file_path = 'D:\Desktop\DCOMS\data\dischargingpmos.csv'  # Replace with your actual CSV file path
data = pd.read_csv(csv_file_path)

# Assuming the CSV has columns named 'Voltage' and 'Current'
voltage = data['vin']
current = data['Id(M1)']

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the data
plt.plot(voltage, current, label='Ids vs Vin', color='blue', linewidth=2)

# Reverse the x-axis
plt.gca().invert_xaxis()

# Add title and labels
plt.title('Ids vs Vin for 45nm technology-pmos discharging (high performance)', fontsize=16, fontweight='bold')
plt.xlabel('Vin(V)', fontsize=14)
plt.ylabel('Ids(A)', fontsize=14)

# Add grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add legend
plt.legend(loc='upper right', fontsize=12)

# Save the plot
output_folder = 'plots'
output_file = 'idsvsvindischarging(pmos).png'
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, output_file)

plt.savefig(output_path)

# Show the plot
plt.show()

print(f"Plot saved to {output_path}")
