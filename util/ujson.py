import json

def Read(filename):
  with open(filename) as f:
    r = json.load(f) # try and/or check correct json format
  return r

def Write(struc, filename):
  dumps = json.dumps(struc, sort_keys=True, indent=2) 
  with open(filename, 'w') as f:
    f.write(dumps)
