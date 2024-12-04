def mod_5(x):
    return x % 5

print("Bilangan terbesar adalah?", max(100, 72, 54), sep='\n')
print("Bilangan terbesar dengan modulus 5 adalah?", max(100, 72, 54, key=mod_5), sep='\n')