import sys

sys.path.extend(['../../src'])

from find_project import *

root_dir = init_project(Path().resolve().parent)
indexing(root_dir)

