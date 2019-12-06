print("Salam!!")
vorodi=input()
bozorg=vorodi.upper()
kochack=vorodi.lower()
u=0
l=0
for i in range(0, len(vorodi)):
    if vorodi[i]==bozorg[i]:
        u=u+1
    if vorodi[i]==kochack[i]:
        l=l+1
if u>l:
    print(vorodi.upper())
else:
    print(vorodi.lower())