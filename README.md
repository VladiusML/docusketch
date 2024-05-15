# Plot Drawer (DocuSketch Internship task)

This repository contains code for drawing plots from data stored in JSON format and displaying images from a specified folder.

## Setup

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```bash
   cd plot_drawer
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv env
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     .\env\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source env/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Drawing Plots

1. Run the `draw_plots.py` script to generate plots from a JSON file:

   ```bash
   python draw_plots.py
   ```

   This script reads data from a JSON file (specified within the script) and saves plots as PNG images in the `plots` folder.

2. After running `draw_plots.py`, you can use the provided Jupyter Notebook (`Notebook.ipynb`) to visualize the saved plots.

### Displaying Images

- Open the Jupyter Notebook (`Notebook.ipynb`) and execute the code cells to display images stored in a specified folder.
