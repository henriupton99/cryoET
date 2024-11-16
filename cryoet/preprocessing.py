import os
import json
import dataclasses
import pandas as pd

class Picks:
  path: str
  
  def __post_init__(self):
    self.json_files = os.listdir(self.path)
    if any(not filename.endswith('.json') for filename in self.json_files):
      raise TypeError(f'Please check that all files in picks folder ({self.path}) are all .json files')
    
    

for filename in os.listdir(json_directory):
    if filename.endswith(".json"):
        class_name = filename.split(".")[0]
        
        with open(os.path.join(json_directory, filename), 'r') as f:
            data = json.load(f)
        
        for point in data.get("points", []):
            location = point.get("location", {})
            transformation = point.get("transformation_", [])
            instance_id = point.get("instance_id")
            
            point_data = {
                "class_name": class_name,
                "pickable_object_name": data.get("pickable_object_name"),
                "user_id": data.get("user_id"),
                "session_id": data.get("session_id"),
                "run_name": data.get("run_name"),
                "voxel_spacing": data.get("voxel_spacing"),
                "unit": data.get("unit"),
                "x": location.get("x"),
                "y": location.get("y"),
                "z": location.get("z"),
                "instance_id": instance_id,
                "transformation": transformation
            }
            all_data.append(point_data)

elements_df = pd.DataFrame(all_data)
print(elements_df)
