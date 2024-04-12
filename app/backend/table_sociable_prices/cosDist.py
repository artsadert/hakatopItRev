import numpy as np
import scipy.spatial.distance as ds
#define arrays
def cosDist(a: str, b: str):
    if len(a) < len(b):
        while len(a) < len(b):
            a += " "
    else: 
        while len(b) < len(a):
            b += " "

    a_vec = np.array(list(map(ord, list(a))))
    b_vec = np.array(list(map(ord, list(b))))
    return ds.cosine(a_vec, b_vec)

if __name__ == "__main__":
    a = input()
    b = input()
    print(cosDist(a, b))
