import sys
import statistics
from collections import defaultdict
from tabulate import tabulate
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk


class F1TimingAnalyzer:
    def __init__(self, drivers_file, lap_times_file):
        self.drivers_file = drivers_file
        self.lap_times_file = lap_times_file
        self.drivers_data = {}
        self.lap_times_data = defaultdict(list)
        self.grand_prix_location = ""

    def load_drivers_data(self):
        """Load driver details from the drivers file."""
        try:
            with open(self.drivers_file, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        car_number, code, name, team = parts
                        self.drivers_data[code] = {
                            'car_number': car_number,
                            'name': name,
                            'team': team
                        }
        except FileNotFoundError:
            print(f"Error: The file {self.drivers_file} does not exist.")
            sys.exit(1)
            
 def load_lap_times_data(self):
        """Load lap times from the lap times file."""
        try:
            with open(self.lap_times_file, 'r') as file:
                lines = file.readlines()
                self.grand_prix_location = lines[0].strip()

                for line in lines[1:]:
                    code = line[:3]
                    try:
                        lap_time = float(line[3:])
                        self.lap_times_data[code].append(lap_time)
                    except ValueError:
                        print(f"Warning: Invalid lap time format in line: {line.strip()}")

        except FileNotFoundError:
            print(f"Error: The file {self.lap_times_file} does not exist.")
            sys.exit(1)

    def display_results(self):
        """Generate the analysis results as a string (for the frontend to display)."""
        result = f"Grand Prix: {self.grand_prix_location}\n"

        # Find the fastest lap overall
        fastest_driver = None
        fastest_time = float('inf')

        for code, times in self.lap_times_data.items():
            driver_fastest_time = min(times)
            if driver_fastest_time < fastest_time:
                fastest_driver = code
                fastest_time = driver_fastest_time

        if fastest_driver:
            driver_info = self.drivers_data.get(fastest_driver, {})
            driver_name = driver_info.get('name', fastest_driver)
            result += f"Fastest Lap: {fastest_time:.3f} by {driver_name} ({fastest_driver})\n\n"

   