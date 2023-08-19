def pythanum(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

print(pythanum(60, 63, 87))


#for check the numbers ^-^




n = 10
for a in range(1, n):
    for b in range(1, n):
        for c in  range(1, n):
            if pythanum(a,b,c):
                if a < b and b < c:
                    print(f"we found a = {a} ,and b = {b}, and c = {c}")

#fpr find pythagorean numbers in your choise range ^-^        
