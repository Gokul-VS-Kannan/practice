def roman_number(num):
    val = [
        1,4,5,9,
        10,40,50,90,
        100,400,500,900,1000
    ]
    sym = [
        "I", "IV", "V", "IX",
        "X", "XL", "L", "XC",
        "C", "CD", "D", "CM","M"
    ]

    rom_num = ""
    i = len(val)-1

    while num > 0:
        for k in range(num//val[i]):
            rom_num += sym[i]
            num -= val[i]

        i -= 1

    return rom_num

number = int(input("Enter the number :"))

print("The roman number for",number, "is",roman_number(number))