from fake_math import divide as err_div
from true_math import divide as inf_div

print(err_div(69, 3))
print(err_div(3, 0))
print(inf_div(49, 7))
print(inf_div(15, 0))
