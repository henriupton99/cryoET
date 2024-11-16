import os
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

from preprocessing import Experiment

class PicksVisualizations:
  """Generic class for generate graphs about picks visualizations in 3D space for a given experiment:
  - plot_experiment_picks: colored 3D scatterplot of the picks locations for the different particles classes
  """
  
  def __init__(self, experiment_path: str, figures_path: str):
    self.figures_paths = figures_path
    self.experiment = Experiment(path=experiment_path)
    print(self.experiment)
  
  def plot_experiment_picks(self, save: bool= True):
    particle_labels = self.experiment.picks['particle'].unique()
    colors = plt.cm.jet(np.linspace(0, 1, len(particle_labels)))
    color_map = {label: color for label, color in zip(particle_labels, colors)}

    fig = go.Figure()
    for label in particle_labels:
        particle_elements = self.experiment.picks[self.experiment.picks['particle'] == label]
        x, y, z = particle_elements['x'], particle_elements['y'], particle_elements['z']
        
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(size=4, color=[color_map[label]]*len(x)),
            name=label,
            legendgroup=label,
            showlegend=True
        ))
    
    if save:
      plot_path = os.path.join(self.figures_paths,f'{self.experiment.name}.png')
      print('Saving the plot...')
      fig.write_image(plot_path, format='png', scale=2)
      print(f'saved completed, can find the plot at the location : {plot_path}')
