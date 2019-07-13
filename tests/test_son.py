"""creates a file test.son and reads back in"""

import son
from pathlib import Path

fname = "test.son"

# Metadata
m = {"purpose": "store biography data", "version": 0.1}

# data points
d1 = {"first name": "Hildegard", "second name": "Kneef", "age": 93}
d2 = {"first name": "Wiglaf", "second name": "Droste", "age": 57}


def test_write(fname=fname, metadata=m, data=[d1, d2], clean_first=True):
    """test son.dump"""

    if Path(fname).exists() and clean_first:
        Path(fname).unlink()

    # dump metadata to file
    son.dump(m, fname, is_metadata=True, indent=2)

    # dump data points to file
    for obj in data:
        son.dump(obj, fname, indent=2)


def test_read(fname=fname):
    """test son.load"""
    metadata, data = son.load(fname)

    assert metadata == m
    assert data == [d1, d2]


def test_write_again(fname=fname):
    """test if writing again throws error"""

    try:
        test_write(clean_first=False)
        raise RuntimeError("FIXME")
    except FileExistsError:
        pass

def test_read_verbose(fname=fname):
    """test son.load"""
    metadata, data = son.load(fname, verbose=True)

    assert metadata == m
    assert data == [d1, d2]

