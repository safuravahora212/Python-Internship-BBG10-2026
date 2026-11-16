height_cm="175"
weight_cm="68.5"
height_cm=int(height_cm)
weight_cm=float(weight_cm)

height_m=height_cm/100
bmi=weight_cm/(height_m*height_m)
print("BMI",bmi)