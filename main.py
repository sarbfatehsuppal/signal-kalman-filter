import sys
import csv
import matplotlib.pyplot as plt

from kalman_filter import KalmanFilter1D


PROCESS_VARIANCE = 1e-3
MEASUREMENT_VARIANCE = 4.0
INITIAL_UNCERTAINTY = 1.0


def load_column(csv_path, column_name=None):
    with open(csv_path, "r", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

        if column_name is None:
            column_name = "distance_cm" if "distance_cm" in fieldnames else fieldnames[0]

        if column_name not in fieldnames:
            raise ValueError(
                f"Column '{column_name}' not found. Available columns: {fieldnames}"
            )

        values = []
        for row in reader:
            values.append(float(row[column_name]))

    print(f"Loaded {len(values)} readings from '{csv_path}' (column: '{column_name}')")
    return values


def main():
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "sample_data.csv"
    column_name = sys.argv[2] if len(sys.argv) > 2 else None

    raw_readings = load_column(csv_path, column_name)

    kf = KalmanFilter1D(
        initial_estimate=raw_readings[0],
        initial_uncertainty=INITIAL_UNCERTAINTY,
        process_variance=PROCESS_VARIANCE,
        measurement_variance=MEASUREMENT_VARIANCE,
    )

    filtered_readings = []
    for reading in raw_readings:
        smoothed_value = kf.filter(reading)
        filtered_readings.append(smoothed_value)

    sample_indices = range(len(raw_readings))

    plt.figure(figsize=(10, 5))
    plt.plot(sample_indices, raw_readings, label="Raw (noisy)",
              color="gray", alpha=0.6, marker=".")
    plt.plot(sample_indices, filtered_readings, label="Kalman filtered",
              color="red", linewidth=2)
    plt.xlabel("Sample #")
    plt.ylabel("Value")
    plt.title("1D Kalman Filter: Raw vs Filtered")
    plt.legend()
    plt.tight_layout()

    plt.savefig("output.png")
    print("Saved plot to output.png")

    plt.show()


if __name__ == "__main__":
    main()
