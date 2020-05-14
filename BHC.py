#Decimal to Binary and Hexadecimal Converter

print("Welcome to the Binary/Hexadecimal Converter App")

target = int(input("\nCompute Binary and Hexadecimal up to the number:" ))
target_list = list(range(1,target+1))
binary = []
hexadecimal = []
for num in target_list:
    binary.append(bin(num))
    hexadecimal.append(hex(num))

print("\nGenerating lists.......Complete!")
print("\nUsing slicing we will now show you a portion of each list")

slice_start = int(input("What number would you like to start at? "))
slice_end = int(input("What number would you like to end at? "))

print("\nDecimal values from " + str(slice_start) + " to " + str(slice_end) + ".")
for num in target_list[slice_start-1:slice_end]:
    print(num)
print("\nBinary values from " + str(slice_start) + " to " + str(slice_end) + ".")
for num in binary[slice_start-1:slice_end]:
    print(num)
print("\nHexadecimal values from " + str(slice_start) + " to " + str(slice_end) + ".")
for num in hexadecimal[slice_start-1:slice_end]:
    print(num)

input("Press ENTER to see all values from 1 to " + str(target))
print("Decimal---Binary---Hexadecimal\n------------------------------")
for d,b,h in zip(target_list,binary,hexadecimal):
    print(str(d) + "--------" + str(b) + "--------" + str(h))
