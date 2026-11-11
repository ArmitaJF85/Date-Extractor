#https://github.com/ArmitaJF85/Date-Extractor
import re

text = input()

pattern = r'(?<!\d)(?:(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])|(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/(\d{4}))(?!\d)'

matches = re.finditer(pattern, text)

results = []

for match in matches:
    if match.group(1):
        year, month, day = match.group(1, 2, 3)
    else:
        day, month, year = match.group(4, 5, 6)

    results.append(f"{year}-{month}-{day}")

print("\n".join(results) if results else "None")
