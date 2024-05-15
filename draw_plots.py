import pandas as pd
import matplotlib.pyplot as plt
import os

class PlotDrawer:
    def __init__(self):
        # Initialize plot folder
        self.plot_folder = "plots"
        if not os.path.exists(self.plot_folder):
            os.makedirs(self.plot_folder)

    def draw_plots(self, json_file):
        # Read data from JSON file into DataFrame
        df = pd.read_json(json_file)

        # Drop 'name' column if exists
        if 'name' in df.columns:
            df = df.drop(columns=['name'])

        # Create plot folder if it doesn't exist
        if not os.path.exists(self.plot_folder):
            os.makedirs(self.plot_folder)

        # List to store paths of saved plots
        plot_paths = []

        # Iterate over each column in DataFrame
        for column in df.columns:
            # Create a new figure
            plt.figure()
            # Plot data from column
            plt.plot(df[column])
            # Set title, xlabel, and ylabel
            plt.title(column)
            plt.xlabel("Index")
            plt.ylabel("Value")
            # Save plot as an image
            plot_path = os.path.join(self.plot_folder, f"{column}_plot.png")
            plt.savefig(plot_path)
            # Append path to the list
            plot_paths.append(plot_path)
            # Close the plot to release memory
            plt.close()
        
        return plot_paths

# Create an instance of PlotDrawer
plot_drawer = PlotDrawer()
# JSON file containing data for plotting
json_file = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"
# Generate plots and get paths
plot_paths = plot_drawer.draw_plots(json_file)
# Print paths of saved plots
print("Plots saved at:")
for path in plot_paths:
    print(path)