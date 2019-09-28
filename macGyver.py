#V0.1.2
#import modules
import json


labyrinth=[['*' for i in range(15)],['*'] + ['v'] * 13 + ['*']];
for i in range(13):
    labyrinth.append(['*'] + ['v'] * 13 + ['*']);
labyrinth.append(['*' for i in range(15)]);
