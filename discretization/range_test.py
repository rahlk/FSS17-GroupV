import sys
sys.path.append('../utils/')
import range_1 as RANGE
from sample_random import Random as R


def f(z):
    return z[0]


def range_test():
    cohen = 0.5
    m = 0.7
    RANDOM = R()
    RANDOM.rseed(1)
    tmp = []
    for i in range(1, 1001):
        tmp.append((RANDOM.r()**2, len(tmp)+1))
    print("ranges: ")
    print("%5s\t%5s\t%5s\t%5s\n" % ("#", "n", "lo", "hi"))
    print("%5s\t%5s\t%5s\t%5s\n" % ("-----", "-----", "-----", "-----"))
    ranges = RANGE.unsup_discret(tmp, f, 0, cohen, m)
    for i, k in enumerate(ranges):
        print("%5s\t%5s\t%5.3f\t%5.3f\n" % (i, k['n'], k['lo'], k['hi']))


if __name__ == "__main__":
    range_test()
