height = input(55)
weight = input(55)

weight_as_int = int(weight)
height_as_float = float(height)
bmi = weight_as_int / height_as_float ** 2
bmi_as = int(bmi)
print(bmi_as)