# ✅↓ Write your code here ↓✅
def sing():
    letra=""
    for i in range(11):
        if i ==4:
            letra=letra+"there will be an answer,\n"
        elif i==10:
            letra=letra+"whisper words of wisdom, let it be"
        else:
            letra=letra+"let it be,\n"
    return letra

print(sing())
