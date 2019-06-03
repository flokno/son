import son

fname = "test.son"


def dump(obj, file, **kwargs):
    return son.dump(obj, file, **kwargs)


# Metadata
m = {"purpose": "store biography data", "version": 0.1}

# data points
d1 = {"first name": "Hildegard", "second name": "Kneef", "age": 93}
d2 = {"first name": "Wiglaf", "second name": "Droste", "age": 57}

# dump metadata to file
dump(m, fname, metadata=1, indent=2)

# dump data points to file
for obj in (d1, d2):
    dump(obj, fname, indent=2)

# load back
metadata, data = son.load(fname)

# check equality
print("\nEqual after parsing?")
print("Metadata:", metadata == m)
print("Data:    ", data == [d1, d2])
