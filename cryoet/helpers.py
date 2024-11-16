import os
import yaml
import json

def load_json(path: str):
  if not os.path.exists(path):
    raise FileNotFoundError(f'Input path "{path}" does not exist')
  try:
    with open(path) as file:
      json_file = json.load(file)
  except:
    raise ImportError(f'Error when try to load json file "{path}"')
  return json_file

def load_yaml(path: str):
  if not os.path.exists(path):
    raise FileNotFoundError(f'Input path "{path}" does not exist')
  try:
    with open(path) as file:
      yaml_file = yaml.safe_load(file)
  except:
    raise ImportError(f'Error when try to load yaml file "{path}"')
  return yaml_file
