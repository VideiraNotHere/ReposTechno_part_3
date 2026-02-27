import math
'''
 def main(z, y):
     term1 = math.atan(82 * y**2 + 1 + y)
     term2 = 98 * (69 * y**2 - 11 * z - 59 * y**3)**4

     numerator = (42 + y**2 / 30 + z) / 97 + (81 * z + z**3 / 94 + z**2)**3
     denominator = 26 * (y + 34)**7 + 6 * (1 - 5 * y**2 - z**3)**2
     term3 = math.sqrt(numerator / denominator)

     return term1 - term2 - term3

 def main(z):
     if z < 152:
         return z**18 - 14 * (11 * z**2 - 61 * z) - 55
     elif z < 183:
         return (z**3 + z**2)**5 + z + 51
     elif z < 227:
         return (15 * z - 7 * z**3 - 1)**4 + z**5
     else:
         part1 = z**7 - math.log2(1 + 8 * z**2 + 25 * z**3)**6
         return part1 - 3 * abs(z)**4

 def main(b, n, m, z):
     result = 0
     for c in range(1, m + 1):
         for j in range(1, n + 1):
             for k in range(1, b + 1):
                 t1 = 10 * (j + 83 * c**2 + k**3)
                 t2 = 68 * c**5 + math.log2(z)**2
                result += t1 + t2
     return result

 def main(n):
     if n == 0:
         return -0.10
     if n == 1:
         return -0.83
     return math.ceil(main(n - 1)**3) - 1 - main(n - 2)**3'''

def main(z, y):
    n = len(z)
    result = 0
    for i in range(1, n + 1):
        y_idx = math.ceil(i / 4) - 1
        z_idx = i - 1
        term = 59 * (98 * y[y_idx] + 3 * z[z_idx]**3)**7
        result += term

    return result