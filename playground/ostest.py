import os

for root, _, filenames in os.walk('~/.ssh'):
    print('{} - {} - {}'.format(root, _, filenames))

