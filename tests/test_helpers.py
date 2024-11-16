import pytest
from cryoet import helpers

valid_json_path = './tests/data/valid_json.json'

not_json_path = './tests/data/invalid_json.csv'
invalid_path = 'not/valid/path'

def test_load_invalid_path():
  with pytest.raises(FileNotFoundError):
    helpers.load_json(invalid_path)
  
def test_load_not_json():
  with pytest.raises(ImportError):
    helpers.load_json(not_json_path)

def test_load_valid_json():
  json_file = helpers.load_json(valid_json_path)
  assert 'var1' in json_file
  assert json_file['var1'] == "a"
  assert 'var2' in json_file
  assert json_file['var2'] == [1,2,3]
