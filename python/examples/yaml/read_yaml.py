import yaml

filename = "data.yaml"

with open(filename) as fh:
    data = yaml.safe_load(fh)

print(data)
