import matplotlib.pyplot as plt
import pandas as pd

months = {
    1: "JAN.",
    2: "FEB.",
    3: "MAR.",
    4: "APR.",
    5: "MAY",
    6: "JUN.",
    7: "JUL.",
    8: "AUG.",
    9: "SEPT.",
    10: "OCT.",
    11: "NOV.",
    12: "DEC."
}

class Traffic:
    def __init__(self, NP, spot, total_count):
        self.park = NP
        self.traffic_spot = spot
        self.traffic_count = total_count
        self.counter = {}

    def add_to_map(self, month, count):
        self.counter[months[month]] = count

    def print_counter(self):
        for i in self.counter:
            print(i, self.counter[i])


    def interpolate(self):
        df = pd.DataFrame({"month": self.counter.keys(), "value": self.counter.values()})


        print(df)


    def plot_data(self):
        plt.plot(self.counter.keys(), self.counter.values())
        plt.title(f'Traffic Chart for {self.traffic_spot} at {self.park}')
        plt.xlabel("Month")
        plt.ylabel("Visitation Count")
        plt.show()
    
