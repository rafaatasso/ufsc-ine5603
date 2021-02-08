n1 = 7
n2 = 6
n3 = 5

final = 0

if n1 <= n2:
    if n1 <= n3:
        final = n1        
    else:
        final = n3
elif n2 <= n3:
    final = n2
else:
    final = n3

print(final)
