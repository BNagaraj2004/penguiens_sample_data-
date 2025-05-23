import pandas as pd
import seaborn as sns
import plotly.express as px
from ipywidgets import interact, widgets, VBox, HBox
from IPython.display import display
from google.colab import files

# Step 2: Load and Preprocess Data
df = sns.load_dataset('penguins')
df = df.dropna()

# Encode categorical variables (optional for modeling, not for display)
df['sex'] = df['sex'].astype('category')
df['species'] = df['species'].astype('category')
df['island'] = df['island'].astype('category')

# Step 3: Create Dropdown Filters
island_dropdown = widgets.Dropdown(options=['All'] + list(df['island'].cat.categories), description='Island:')
species_dropdown = widgets.Dropdown(options=['All'] + list(df['species'].cat.categories), description='Species:')
sex_dropdown = widgets.Dropdown(options=['All'] + list(df['sex'].cat.categories), description='Sex:')

# Step 4 & 5: Visualizations + Summary Statistics
output = widgets.Output()

def update_dashboard(island, species, sex):
    output.clear_output()
    
    filtered = df.copy()
    if island != 'All':
        filtered = filtered[filtered['island'] == island]
    if species != 'All':
        filtered = filtered[filtered['species'] == species]
    if sex != 'All':
        filtered = filtered[filtered['sex'] == sex]
    
    with output:
        display(filtered.head())

        # Visualizations
        fig1 = px.pie(filtered, names='species', title='Species Distribution')
        fig1.show()

        fig2 = px.bar(filtered.groupby('species')['body_mass_g'].mean().reset_index(),
                      x='species', y='body_mass_g', title='Average Body Mass by Species')
        fig2.show()

        fig3 = px.box(filtered, x='species', y='flipper_length_mm', title='Flipper Length by Species')
        fig3.show()

        fig4 = px.histogram(filtered, x='bill_length_mm', nbins=20, title='Bill Length Distribution')
        fig4.show()

        fig5 = px.scatter(filtered, x='bill_length_mm', y='bill_depth_mm', color='species',
                          title='Bill Length vs. Bill Depth')
        fig5.show()

        # Summary Statistics
        print("Summary Statistics:")
        print(f"Total Penguins: {len(filtered)}")
        print(f"Average Body Mass: {filtered['body_mass_g'].mean():.2f} g")
        print(f"Average Flipper Length: {filtered['flipper_length_mm'].mean():.2f} mm")
        print("Gender Count:")
        print(filtered['sex'].value_counts())

        # Save filtered data to a CSV
        def save_csv(_):
            filtered.to_csv('filtered_penguins.csv', index=False)
            files.download('filtered_penguins.csv')
        
        save_button = widgets.Button(description="Export Filtered Data")
        save_button.on_click(save_csv)
        display(save_button)

# Interactive Controls
interact_ui = VBox([HBox([island_dropdown, species_dropdown, sex_dropdown])])
interact(update_dashboard, island=island_dropdown, species=species_dropdown, sex=sex_dropdown)

display(interact_ui, output)
