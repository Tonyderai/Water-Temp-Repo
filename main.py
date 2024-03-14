# Ask the user to input the water temperature
temperature = float(input("Enter the temperature of water: "))

# Create print statements if water temperature is below 0
if temperature <= 0:
    print("The state of the water is: Ice")
elif temperature <= 100:
    print("The state of the water is: Liquid Water")
else:
    print("The state of the water is: Water vapour")