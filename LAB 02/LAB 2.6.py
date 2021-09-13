#1201200654
#Kong Zi Yin

import math

radius = float(input("Enter value of radius : "))

volume = 4/3 * math.pi * pow(radius,3)
sa = 4 * math.pi * pow(radius,2)

print("\nRadius of sphere is {:.2f} cm, \nVolume is {:.2f} cm^3 \nand surface are is {:.2f} cm^3" .format(radius,volume,sa))