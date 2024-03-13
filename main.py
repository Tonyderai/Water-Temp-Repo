temperature = float(input("Enter the temperature of water: "))

if temperature <= 0:
    print("Ice")
elif temperature <= 100:
    print("Water")
else:
    print("Water vapour")