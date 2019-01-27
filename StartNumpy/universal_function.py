# -*- coding: utf-8 -*-
import numpy as np
import traceback
from timeit import timeit, repeat
np.random.seed(0)


def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output


# try:
#     values = np.random.randint(1, 10, size=1000)
#     print(111+"sda")
#     # print(compute_reciprocals(values))
#     # print(timeit('compute_reciprocals(values)',
#     #              "from __main__ import compute_reciprocals;import numpy as np;"
#     #              "np.random.seed(0);values = np.random.randint(1, 10, size=10)", number=1000))
#     # print(timeit('1.0/values', 'import numpy as np;np.random.seed(0);values = np.random.randint(1, 10, size=1000)',
#     #              number=1000))
#     # print(repeat('compute_reciprocals(values)', 'from __main__ import compute_reciprocals;'
#     #                                             'import numpy as np;np.random.seed(0);'
#     #                                             'values = np.random.randint(1, 10, size=1000)', number=1000, repeat=5))
# except Exception:
#     pass
#     # traceback.print_exc()
