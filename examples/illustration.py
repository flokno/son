"""creates a file test.son and reads back in"""

import son

fname = "test.son"

# Metadata
m = {"purpose": "store biography data", "version": 0.1}

# data points
d1 = {"first name": "Hildegard", "second name": "Kneef", "age": 93}
d2 = {"first name": "Wiglaf", "second name": "Droste", "age": 57}

# dump metadata to file
son.dump(m, fname, is_metadata=True, indent=2)

# dump data points to file
for obj in (d1, d2):
    son.dump(obj, fname, indent=2)

# load back
metadata, data = son.load(fname)

# check equality
print("\nEqual after parsing?")
print("Metadata:", metadata == m)
print("Data:    ", data == [d1, d2])
