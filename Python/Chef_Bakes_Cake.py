

import math


N, X, Y = map(int, input().split())

cakes_per_vehicle = Y // X

print(math.ceil(N/cakes_per_vehicle))