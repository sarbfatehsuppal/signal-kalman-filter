import csv
import random
import math

random.seed(42)

NUM_SAMPLES = 100
TRUE_START = 50.0
NOISE_STD_DEV = 3.0

rows = []

for i in range(NUM_SAMPLES):
    true_value = TRUE_START + 15 * math.sin(i / 15.0)
    noisy_reading = true_value + random.gauss(0, NOISE_STD_DEV)
    rows.append([i, round(true_value, 3), round(noisy_reading, 3)])

with open("sample_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["sample", "true_value", "distance_cm"])
    writer.writerows(rows)

print(f"Wrote {NUM_SAMPLES} fake noisy readings to sample_data.csv")
