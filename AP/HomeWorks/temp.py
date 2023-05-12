import re

s = "adsfsd1323%adsf"
print(re.findall(r"^(?!.*[^a-z\d]+)[a-z\d]+", s))
