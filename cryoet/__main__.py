import os
import argparse
from visualizations import PicksVisualizations
from helpers import load_yaml

if __name__ == '__main__':
  parser = argparse.ArgumentParser('Main script for CryoET')
  parser.add_argument('--c', required=False, default='config.yml', help='Path to config yaml file', type=str)
  args = parser.parse_args()
  config_path = args.c
  if not os.path.exists(config_path):
    raise FileNotFoundError(f'Invalid path for config : "{config_path}"')
  
  config = load_yaml(config_path)
  PicksVisualizations(
    experiment_path=config['paths']['picks'], 
    figures_path=config['paths']['figures']
    ).plot_experiment_picks()
