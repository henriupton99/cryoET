import os
import dataclasses
import pandas as pd

from helpers import load_json

@dataclasses.dataclass
class Particle:
    """Generic dataclass to load a Particle json file content, and its respective picks.
    Generate the utility attribute .points, a list of dict with attributes x,y,z
    - format of a point: {'x': ..., 'y': ..., 'z': ...}
    """
    path: str
    experiment: str
    
    def __post_init__(self):
        self.content = load_json(self.path)
        self.name = self.content.get('pickable_object_name')

        self.points = []
        for point in self.content.get('points', []):
            location = point.get('location', {})
            self.points.append(location)
    
    def __repr__(self):
        repr = f'Particle name : {self.name}\n'
        repr += f'Experiment name : {self.experiment}\n'
        repr += f'Number of points : {len(self.points)}'
        return repr
          
@dataclasses.dataclass
class Experiment:
    """Generic dataclass to load Experiment folder content, containing several json files of particle picks.
    Generate the utility attribute .picks, a pandas dataframe containing the columns experiment,particle,x,y,z
    - experiment: experiment id (e.g 'TS_5_4')
    - particle: the particle name / class for the picked observation (e.g 'apo-ferritin', 'beta-amylase'...)
    - x,y,z: the 3 dimensionnal coordinate for the pick extracted from the tomography (float)
    """
    path: str
    
    def __post_init__(self):
        self.name = self.path.split('/')[-1]
        self.particles_files = os.listdir(self.path)
        if any(not filename.endswith('.json') for filename in self.particles_files):
            raise TypeError(f'Please check that all files in picks folder ({self.path}) are all .json files')
        
        self.picks = []
        for file in self.particles_files:
            filepath = os.path.join(self.path, file)
            particle = Particle(path=filepath, experiment=self.name)
            for point in particle.points:
                point_data = {
                    'experiment' : self.name,
                    'particle' : particle.name,
                    'x': point.get('x'),
                    'y': point.get('y'),
                    'z': point.get('z')
                }
                self.picks.append(point_data)
        
        self.picks = pd.DataFrame(self.picks)
    
    def __repr__(self):
        repr = f'Experiment name : {self.name}\n'
        repr += f'Number of picks : {len(self.picks)}\n'
        repr += f'Picks : {self.picks.head(5)}'
        return repr
