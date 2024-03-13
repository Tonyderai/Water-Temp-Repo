temperature = float(input("Enter the temperature of water: "))

if temperature <= 0:
    print("The state of the water is: Ice")
elif temperature <= 100:
    print("The state of the water is: Liquid Water")
else:
    print("The state of the water is: Water vapour")