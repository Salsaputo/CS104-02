# CS104
# Sal Saputo
# conditions.py
i = 1
while i <= 5:
    temp = int(input("please enter the current temperature: "))
    if temp > 90:
        print("wear Shorts")
    elif temp > 70:
        print("Short sleeves are fine")
    elif temp > 32:
        print ("Wear a heavy coat")
    else:
        print("Stay Inside")
    i +=1
