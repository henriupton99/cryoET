import pandas as pd
from cryoet.preprocessing import Particle, Experiment

particle_path = 'tests/data/TS_5_4/apo-ferritin.json'
experiment_path = 'tests/data/TS_5_4'

def test_particle():
  particle = Particle(path=particle_path, experiment='TS_5_4')
  assert hasattr(particle, 'name')
  assert particle.name == 'apo-ferritin'
  
  assert hasattr(particle, 'points')
  assert isinstance(particle.points, list)
  assert len(particle.points) == 2
  assert particle.points[0] == {"x": 468.514, "y": 5915.906, "z": 604.167}

def test_experiment():
  experiment = Experiment(path=experiment_path)
  assert experiment.name == 'TS_5_4'
  assert len(experiment.particles_files) == 2
  
  assert isinstance(experiment.picks, pd.DataFrame)
  assert len(experiment.picks) == 4
