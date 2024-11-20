import matplotlib.pyplot as plt
import pandas as pd
import os

# Read data from CSV file
csv_file_path = 'D:\Desktop\DCOMS\data\Q2CgsvsVgs.csv'  # Replace with your actual CSV file path
data = pd.read_csv(csv_file_path)

# Assuming the CSV has columns named 'Voltage' and 'Cg'
voltage = data['V(n001)']
Cg = data['Cgs']

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the data
plt.plot(voltage, Cg, label='Cg vs Vgs', color='blue', linewidth=2)

# Add title and labels
plt.title('Cg vs Vgs', fontsize=16, fontweight='bold')
plt.xlabel('Vgs(V)', fontsize=14)
plt.ylabel('Cg(F)', fontsize=14)

# Add grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add legend
plt.legend(loc='upper left', fontsize=12)

# Save the plot
output_folder = 'plots'
output_file = 'CgvsVgs.png'
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, output_file)

plt.savefig(output_path)

# Show the plot
plt.show()

print(f"Plot saved to {output_path}")
