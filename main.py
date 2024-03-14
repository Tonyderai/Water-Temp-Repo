try:
# Ask the user to input the water temperature
temperature = float(input("Enter the temperature of water: "))

# Ensure the temperature is within a reasonable range
if temperature < -273.15:
    print("Error: Temperature cannot be below absolute zero.")
else:
    # Create print statements based on the water temperature
    if temperature <= 0:
        print("The state of the water is: Ice")
    elif temperature <= 100:
        print("The state of the water is: Liquid Water")
    else:
        print("The state of the water is: Water vapour")