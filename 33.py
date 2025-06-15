import matplotlib.pyplot as plt
import numpy as np

# Parameter tetap
S = 50000  # biaya pesan per kali
H = 2000   # biaya simpan per unit per tahun

# Variasi permintaan tahunan
D_values = np.arange(1000, 20000, 1000)
EOQ_values = np.sqrt((2 * D_values * S) / H)

# Buat grafik
plt.figure(figsize=(10, 6))
plt.plot(D_values, EOQ_val
