# coding: utf8

import random
import json


data = [random.randint(1, 1000) for elem in range(0, 50)]

print(json.dumps(data))
