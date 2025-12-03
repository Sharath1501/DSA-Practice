def freuency_cal(instr):
    freuency = [0]*10
    for char in instr:
        if char.isdigit():
            freuency[int(char)] +=1
    for digit in range(10):
        if freuency[digit]>0:
            print(f"Digit {digit} : {freuency[digit]}")
instr = input("Enter the multi character value: ")
freuency_cal(instr)