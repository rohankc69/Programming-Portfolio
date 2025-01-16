import sys
import statistics
from collections import defaultdict
from tabulate import tabulate
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk


class RaceAnalyzer:
    def __init__(self, drivers_path, lap_times_path):
        self.drivers_path = drivers_path
        self.lap_times_path = lap_times_path
        self.driver_info = {}
        self.lap_data = defaultdict(list)
        self.race_location = ""

    def read_drivers(self):
        try:
            with open(self.drivers_path, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        car_num, code, name, team = parts
                        self.driver_info[code] = {
                            'car_num': car_num,
                            'name': name,
                            'team': team
                        }
        except FileNotFoundError:
            print(f"Error: {self.drivers_path} not found.")
            sys.exit(1)

    def read_lap_times(self):
        try:
            with open(self.lap_times_path, 'r') as file:
                lines = file.readlines()
                self.race_location = lines[0].strip()

                for line in lines[1:]:
                    code = line[:3]
                    try:
                        lap_time = float(line[3:])
                        self.lap_data[code].append(lap_time)
                    except ValueError:
                        print(f"Invalid lap time in line: {line.strip()}")
        except FileNotFoundError:
            print(f"Error: {self.lap_times_path} not found.")
            sys.exit(1)

    def generate_report(self):
        report = f"Race: {self.race_location}\n"

        best_driver = None
        best_time = float('inf')

        for code, times in self.lap_data.items():
            fastest = min(times)
            if fastest < best_time:
                best_driver = code
                best_time = fastest

        if best_driver:
            info = self.driver_info.get(best_driver, {})
            name = info.get('name', best_driver)
            report += f"Best Lap: {best_time:.3f} by {name} ({best_driver})\n\n"

        report += "Best Lap Per Driver:\n"
        lap_table = []
        for idx, (code, times) in enumerate(self.lap_data.items(), 1):
            info = self.driver_info.get(code, {})
            name = info.get('name', code)
            team = info.get('team', 'Unknown')
            fastest = min(times)
            lap_table.append([idx, name, code, team, f"{fastest:.3f}"])

        report += tabulate(lap_table, headers=["SN", "Driver", "Code", "Team", "Fastest Lap"], tablefmt="grid")
        report += "\n\nAverage Lap Times:\n"

        all_times = [time for times in self.lap_data.values() for time in times]
        overall_avg = statistics.mean(all_times)
        report += f"Overall Average: {overall_avg:.3f}\n"

        avg_table = []
        for idx, (code, times) in enumerate(self.lap_data.items(), 1):
            info = self.driver_info.get(code, {})
            name = info.get('name', code)
            avg_time = statistics.mean(times)
            avg_table.append([idx, name, code, f"{avg_time:.3f}"])

        report += tabulate(avg_table, headers=["SN", "Driver", "Code", "Average Lap"], tablefmt="grid")

        report += "\n\nBest Laps in Descending Order:\n"
        sorted_times = sorted([(code, min(times)) for code, times in self.lap_data.items()], key=lambda x: x[1])

        sorted_table = []
        for idx, (code, time) in enumerate(sorted_times, 1):
            info = self.driver_info.get(code, {})
            name = info.get('name', code)
            sorted_table.append([idx, name, code, f"{time:.3f}"])

        report += tabulate(sorted_table, headers=["SN", "Driver", "Code", "Best Lap"], tablefmt="grid")

        return report


class RaceApp(tk.Tk):
    def __init__(self, analyzer):
        super().__init__()
        self.analyzer = analyzer
        self.title("Race Timing Analyzer")
        self.geometry("800x600")

        self.result_area = tk.Text(self, wrap=tk.WORD, height=30, width=100)
        self.result_area.pack(padx=10, pady=10)

        self.load_button = tk.Button(self, text="Select Lap Times", command=self.select_lap_file)
        self.load_button.pack(pady=10)

        self.analyze_button = tk.Button(self, text="Analyze", command=self.show_results, state=tk.DISABLED)
        self.analyze_button.pack(pady=10)

    def select_lap_file(self):
        lap_path = filedialog.askopenfilename(title="Choose Lap Times File", filetypes=[("Text Files", "*.txt")])
        if lap_path:
            self.analyzer.lap_times_path = lap_path
            self.analyze_button.config(state=tk.NORMAL)

    def show_results(self):
        try:
            self.analyzer.read_drivers()
            self.analyzer.read_lap_times()
            report = self.analyzer.generate_report()
            self.result_area.delete(1.0, tk.END)
            self.result_area.insert(tk.END, report)
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {str(e)}")


def main():
    drivers_path = filedialog.askopenfilename(title="Choose Drivers File", filetypes=[("Text Files", "*.txt")])
    if not drivers_path:
        print("Drivers file not selected. Exiting.")
        sys.exit(1)

    analyzer = RaceAnalyzer(drivers_path, "")
    app = RaceApp(analyzer)
    app.mainloop()


if __name__ == "__main__":
    main()
