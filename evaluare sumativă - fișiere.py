with open('Desktop/input.txt', 'r') as f:
    linii = f.readlines()
print('Nr.	Numele	Prenumele	Nota1	Nota2	Nota3')
print(*linii)
with open('Desktop/rezerva.txt', 'w') as f:
    for i in linii:
        f.write(i)
for j in linii:
    linie_brut = j.split()
    media = str(round((float(linie_brut[3]) + float(linie_brut[4]) + float(linie_brut[5]))/3, 2))
    linie = linie_brut[0] + ' ' + linie_brut[1] + ' ' + linie_brut[2] + ' ' + media + '\n'
    with open('Desktop/output.txt', 'a') as f:
        f.write(linie)
with open('Desktop/output.txt', 'r') as f:
    linii_output = f.readlines()
print('Nr.	Numele	Prenumele	Media')
print(*linii_output)