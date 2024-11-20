
# # Vds calculation
# Vds = Vin - Vout
# Vdd = 1

# # NMOS parameters
# Vth_nmos = 0.46893
# wn_by_wl = 2/1
# mun = 540e-4
# toxn = 1.25e-9
# coxn = k * e0 / toxn
# betan = mun * coxn * (wn_by_wl)
# # print(betan)

# # PMOS parameters
# Vth_pmos = -0.49158
# wp_by_wl = 4/1
# mup = 200e-4
# toxp = 1.3e-9
# coxp = k * e0 / toxp
# betap = mup * coxp * (wp_by_wl)
# # print(betap)

# # Functions to check the region of operation
# def isCutoff(Vinp, type_t):
#     if type_t == "n":
#         # NMOS transistor cutoff check
#         return Vinp > Vdd - Vth_nmos
#     elif type_t == "p":
#         # PMOS transistor cutoff check (example)
#         return Vinp < abs(Vth_pmos)

# def isLinear(Vinp, type_t):
#     if type_t == "n":
#         return Vinp <= Vdd - Vth_nmos
#     elif type_t == "p":
#        return Vinp >= abs(Vth_pmos)

# def isSaturation(Vinp, type_t):
#   if type_t == "n":
#         return Vinp > Vdd - Vth_nmos
#   elif type_t == "p":
#        return Vinp < abs(Vth_pmos)
  
# # Calculate Ids for NMOS
# Ids_nmos = np.zeros(n)
# for i in range(n):
#     if isCutoff(Vin[i], "n"):
#         Ids_nmos[i] = 0
#     elif isLinear(Vin[i], "n"):
#         Ids_nmos[i] = betan * ((Vdd - Vout[i] - Vth_nmos) * Vds[i] - (Vds[i]**2) / 2)
#     elif isSaturation(Vin[i], "n"):
#         Ids_nmos[i] = betan / 2 * (Vin[i] - Vth_nmos)**2

# # Calculate Ids for PMOS
# Ids_pmos = np.zeros(n)
# for i in range(n):
#     if isCutoff(Vin[i], "p"):
#         Ids_pmos[i] = 0
#     elif isLinear(Vin[i], "p"):
#         Ids_pmos[i] = betap * ((Vin[i] - abs(Vth_pmos) - Vds[i]) * Vds[i] - (Vds[i])**2 / 2)
#     elif isSaturation(Vin[i], "p"):
#         Ids_pmos[i] = betap / 2 * (Vin[i] - abs(Vth_pmos))**2

# # Plotting Ids vs Vin for NMOS and PMOS
# plt.figure(figsize=(10, 6))

# # NMOS plot
# plt.plot(Vin, Ids_nmos , label='Ids vs Vin (NMOS)', color='blue', linewidth=2)

# # PMOS plot
# plt.plot(Vin, Ids_pmos, label='Ids vs Vin (PMOS)', color='red', linewidth=2)

# # # NMOS + PMOS plot
# # plt.plot(Vin, Ids_nmos+Ids_pmos, label='Ids vs Vin (NMOS)', color='blue', linewidth=2)

# # Add title and labels
# plt.title('Ids vs Vin for NMOS and PMOS Transistors', fontsize=16, fontweight='bold')
# # plt.title('(IdsNmos+IdsPmos) vs Vin for NMOS and PMOS Transistors', fontsize=16, fontweight='bold')
# plt.xlabel('Vin (V)', fontsize=14)
# plt.ylabel('IdsNmos (A)', fontsize=14)
# # plt.ylabel('(IdsNmos+IdsPmos) (A)', fontsize=14)
# # Add grid
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# # Add legend
# plt.legend(loc='upper left', fontsize=12)

# # # Save the plot
# # output_folder = 'plots'
# # output_file = 'ids_vs_vin_nmos_pmos.png'
# # os.makedirs(output_folder, exist_ok=True)
# # output_path = os.path.join(output_folder, output_file)
# # plt.savefig(output_path)

# # Show the plot
# plt.show()

# # print(f"Plot saved to {output_path}")