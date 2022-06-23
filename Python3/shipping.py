weight = 1.5

# Ground ground_shipping
ground_shipping = 0

if weight <= 2:
  ground_shipping += 20.00 + weight * 1.50
elif weight <= 6:
  ground_shipping += 20.00 + weight * 3.00
elif weight <= 10:
  ground_shipping += 20.00 + weight * 4.00
else:
  ground_shipping += 20.00 + weight * 4.75

print('Ground Shipping: $', ground_shipping)
ground_premium_shipping = 125
print('Ground Premium Shipping: $', ground_premium_shipping)

# Drone Shipping
drone_shipping = 0

if weight <= 2:
  drone_shipping = weight * 4.5
elif weight <= 6:
  drone_shipping = weight * 9.00
elif weight <= 10:
  drone_shipping = weight * 12.00
else:
  drone_shipping = weight * 14.25

print('Drone Shipping: $', drone_shipping)