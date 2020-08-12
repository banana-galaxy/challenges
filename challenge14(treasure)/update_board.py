import json

def get(dbname):
    with open(dbname, 'r') as f:
        return json.load(f)

def _write(dbname, data):
    with open(dbname, 'w') as f:
        json.dump(data, f)

def lost(dbname, user, challengeid):
    data = get(dbname)
    if user not in data.keys():
        data[user] = {challengeid: 0}
    else:
        data[user][challengeid] = 0
    _write(dbname, data)

def won(dbname, user, challengeid):
    data = get(dbname)
    if user not in data.keys():
        data[user] = {challengeid: 1}
    else:
        data[user][challengeid] = 1
    _write(dbname, data)