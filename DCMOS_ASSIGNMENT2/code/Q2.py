import matplotlib.pyplot as plt
import pandas as pd
import os

csv_file_path = "D:\Desktop\DCMOS_ASSIGNMENT2\data\Q2.csv" 
data = pd.read_csv(csv_file_path)

time = data['time']
Vin = data['V(vy)']
Vout = data['V(vout)']  

plt.figure(figsize=(12, 6))
plt.plot(time, Vin, label='Vin vs Time', color='green', linewidth=2)
plt.plot(time, Vout, label='Vout vs Time', color='blue', linestyle='--', linewidth=2)

plt.title('Vin and Vout vs Time for 45nm Technology (High Performance)', fontsize=16, fontweight='bold')
plt.xlabel('Time (s)', fontsize=14)
plt.ylabel('Voltage (Volts)', fontsize=14)

plt.grid(True, which='both', linewidth=0.5)
plt.legend(loc='upper right', fontsize=12)

output_folder = '../plots'
output_file_combined = 'vin_vout_vs_time.png'
os.makedirs(output_folder, exist_ok=True)
output_path_combined = os.path.join(output_folder, output_file_combined)
plt.savefig(output_path_combined)
plt.show()