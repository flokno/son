"""based on https://stackoverflow.com/a/34482761/5172579"""

import sys


def progressbar(it, prefix="progress:", size=35, file=sys.stdout):
    """a simple progress bar to decorate an iterator

    Args:
        it (iterator): show progressbar for this iterator
        prefix (str): prefix for the progressbar
        size (int): size of the progress bar
        file (file): file to write to
    """
    count = max(1, len(it))
    n = len(str(count)) + 1

    def show(jj):
        """show the progressbar"""
        x = int(size * jj / count)
        counter = "{:{}d}/{}".format(jj, n, count)
        bar = "{} |{}{}| {}\r".format(prefix, "|" * x, " " * (size - x), counter)
        file.write(bar)
        file.flush()

    show(0)

    ii = 0
    for ii, item in enumerate(it):
        yield item
        if hasattr(file, "isatty") and file.isatty():
            show(ii + 1)

    if hasattr(file, "isatty") and file.isatty():
        file.write("\n")
        file.flush()
    else:
        show(ii + 1)
