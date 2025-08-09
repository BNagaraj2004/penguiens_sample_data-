# 🐧 Penguin Data Interactive Dashboard

This project is an **interactive data exploration tool** built using **Python, Plotly, Seaborn, and ipywidgets**, focused on the [Palmer Penguins dataset](https://allisonhorst.github.io/palmerpenguins/).  
It allows filtering, visualization, and exporting of penguin data with dynamic charts and summary statistics.

---

## 📌 Features
- **Interactive Filtering**: Filter penguins by *Island*, *Species*, and *Sex* using dropdown menus.
- **Dynamic Visualizations**:
  - Pie chart: Species distribution
  - Bar chart: Average body mass by species
  - Box plot: Flipper length comparison
  - Histogram: Bill length distribution
  - Scatter plot: Bill length vs. bill depth
- **Summary Statistics**: Automatically updated counts, averages, and gender breakdown.
- **Export Functionality**: Save filtered data to CSV with one click.

---

## 📂 Dataset
We use the **Palmer Penguins** dataset, which contains measurements for penguins from three species: *Adelie*, *Chinstrap*, and *Gentoo*.  
Attributes include:
- Island
- Bill length & depth
- Flipper length
- Body mass
- Sex

---

## 🚀 How to Run

1. **Install Dependencies**
```bash
pip install pandas seaborn plotly ipywidgets
