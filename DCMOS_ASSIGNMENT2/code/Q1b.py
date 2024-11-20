import matplotlib.pyplot as plt
import pandas as pd
import os

# Read data from CSV file
csv_file_path = "D:\Desktop\DCMOS_ASSIGNMENT2\data\Q1b.csv"  # Replace with your actual CSV file path
data = pd.read_csv(csv_file_path)

# Extract columns for Vin and Vout
Vin = data['V(vin)']       # Replace 'Vin' with the actual column name for Vin
Vout = data['V(vout)']  # Replace 'V(vout)' with the actual column name for Vout

# Create the plot for Vin vs Vout
plt.figure(figsize=(10, 6))
plt.plot(Vin, Vout, label='Vout vs Vin', color='blue', linewidth=2)

# Add title and labels
plt.title('Vout vs Vin for 45nm Technology (High Performance)', fontsize=16, fontweight='bold')
plt.xlabel('Vin (Volts)', fontsize=14)
plt.ylabel('Vout (Volts)', fontsize=14)

# Add grid and legend
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(loc='upper right', fontsize=12)

# Save the plot
output_folder = '../plots'
output_file = 'vin_vs_vout.png'
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, output_file)
plt.savefig(output_path)
plt.show()

print(f"Vin vs Vout plot saved to {output_path}")
