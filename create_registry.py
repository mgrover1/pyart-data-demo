import os
import pathlib

import pooch

__file__ = 'create_registry.py'

if __name__ == '__main__':
    here = pathlib.Path(os.path.dirname(__file__))
    data_dir = here / 'data'

    pooch.make_registry(data_dir, here / 'data/registry.txt')