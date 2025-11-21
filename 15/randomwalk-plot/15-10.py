import pandas as pd
import plotly.express as px

from random_walk import RandomWalk

# Generate the dataset
rw = RandomWalk(1000000)
rw.fill_walk()

# Prepare a DataFrame for plotly
df = pd.DataFrame({
    "x": rw.x_values,
    "y": rw.y_values,
    "point": range(rw.num_points)
})

# Create an interactive scatter plot with a colormap.
# Use WebGL rendering for large point counts (render_mode='webgl').
fig = px.scatter(
    df,
    x="x",
    y="y",
    color="point",
    color_continuous_scale="Reds",
    title="Random Walk (plotly.express)",
    labels={"x": "x", "y": "y"},
    width=1200,
    height=800,
    render_mode="webgl"
)

# Make points small and set equal aspect ratio
fig.update_traces(marker=dict(size=2, opacity=0.8))
fig.update_yaxes(scaleanchor="x", scaleratio=1)

# Show interactive plot (will open in browser or plotly viewer)
fig.show()