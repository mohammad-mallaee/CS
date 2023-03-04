inputs = []

for i in range(5):
    inputs.append(int(input()))

rain_intensity = inputs[0]
necessity = inputs[1]

tools = 0
has_boots = True if inputs[2] == 1 else False
tools = 1 if has_boots else 0
has_umbrella = True if inputs[3] == 1 else False
tools = 10 if has_umbrella else tools
has_car = True if inputs[4] == 1 else False
tools = 100 if has_car else tools

if rain_intensity == 0:
    print("True")
elif necessity >= rain_intensity:
    print("True")
elif tools >= rain_intensity:
    print("True")
else:
    print("False")
