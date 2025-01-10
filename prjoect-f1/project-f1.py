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

   