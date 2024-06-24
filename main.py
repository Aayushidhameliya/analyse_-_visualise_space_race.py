import pandas as pd

# Load the data with 'Datum' column parsed as datetime
try:
    data = pd.read_csv('space_missions.csv', parse_dates=['Datum'], encoding='utf-8')
except FileNotFoundError:
    print("File not found. Please check the file path and ensure the file exists.")
    # Optionally raise the error or handle it as needed
except Exception as e:
    print(f"An error occurred while loading the data: {e}")
    # Handle other specific exceptions if necessary

# Example: Convert 'Datum' column to datetime with error handling
data['Datum'] = pd.to_datetime(data['Datum'], errors='coerce')

print(data.dtypes)

if 'data' in locals():
    # Filter data for missions from 1957 onwards
    data = data[data['Datum'].dt.year >= 1957]

    # Proceed with further analysis and visualization as needed
    # Example: Number of missions per year
    missions_per_year = data['Datum'].dt.year.value_counts().sort_index()

    # Example: Plotting number of missions per year
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    missions_per_year.plot(kind='line', marker='o', color='b')
    plt.title('Number of Space Missions Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Missions')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('missions_per_year.png')
    plt.show()

else:
    print("Data was not loaded successfully. Check previous error messages for details.")
