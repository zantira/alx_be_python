#program that utilize while loops and nested for loops to draw a simple text-based pattern.

pattern_size = int(input("Enter the size of the pattern: "))

i = 0

while i <= pattern_size:
  
    for i in range(1, pattern_size + 1):
        j = 0
        for j in range(1, pattern_size + 1):
            print("*", end="")

            j += 1
       
        print()
        i += 1


