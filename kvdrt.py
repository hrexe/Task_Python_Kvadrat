# Inkishaf etdirmek meqsedile her iki variantla yazdim...

import math
import random

random_reqemler = [random.randint(20, 50) for _ in range(5)]
print(f"Random reqemler budur: {random_reqemler}")

cutler = [cut for cut in random_reqemler if cut % 2 == 0]
print(f"Cut ededler budur: {cutler}")

ustu_ikiler = [int(math.pow(kvdrt, 2)) for kvdrt in cutler]
print(f"Cut ededlerin kvadrati budur: {ustu_ikiler}")



# import math
# import random
#
# list = []
# cutler = []
# ustu_ikiler = []
# for i in range(5):
#     random_reqemler = random.randint(20,50)
#     list.append(random_reqemler)
# print(f"Random reqemler budur: {list}")
#
# for cut in list:
#     if cut % 2 == 0:
#         cutler.append(cut)
# print(f"Cut ededler budur: {cutler}")
#
# for kvdrt in cutler:
#     ustu_iki = int(math.pow(kvdrt, 2))
#     ustu_ikiler.append(ustu_iki)
# print(f"Cut ededlerin kvadrati budur: {ustu_ikiler}")




