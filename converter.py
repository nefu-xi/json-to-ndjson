# import json
import ndjson

# load from file-like objects
with open('players_team15.json') as f:
    data = ndjson.load(f)

# convert to and from objects
# text = ndjson.dumps(data)
# data = ndjson.loads(text)

# dump to file-like objects
with open('backup.ndjson', 'w') as f:
    ndjson.dump(data, f)