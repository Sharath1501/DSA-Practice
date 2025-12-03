import re
def find_area_codes(filename):
    pattern = re.compile(r'^(\w+)\s(\d{3}-\d{8})$')

    names = []
    with open(filename,'r') as file:
        for line in file:
            match = pattern.match(line.strip())
            if match:
                name,phone_number=match.groups()
                area_code = phone_number.split('-')[0]
                if len(area_code)==3:
                    names.append(name)
    return names
filename = 'm.txt'
names = find_area_codes(filename)
print(names)

