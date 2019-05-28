from json import dumps, loads


def dump(obj, indent=2):
    return dumps(obj, indent=2)

def parse(string):
    return [loads(blob) for blob in string.split('---')]


# Metadate
m = {"purpose": "store biography data", "version": 0.1}

# data points
d1 = {"first name": "Hildegard", "second name": "Kneef", "age": 93}

d2 = {"first name": "Wiglaf", "second name": "Droste", "age": 57}

# son representation
s = "\n".join([dump(m), "===", dump(d1), "---", dump(d2)])

print(s)

# load back
raw_metadata, raw_data = s.split('===')

metadata = parse(raw_metadata)
data = parse(raw_data)

# check equality
print('\nEqual after parsing?')
print('Metadata:', metadata == [m])
print('Data:    ', data == [d1, d2])
