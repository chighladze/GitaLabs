def liters_100km_to_miles_gallon(liters):
    one_mile_in_one_km = 1609.344  # metres
    one_gallon_in_liter = 3.785411784  # litres
    return 100_000 / one_mile_in_one_km * one_gallon_in_liter / liters


def miles_gallon_to_liters_100km(miles):
    one_mile_in_one_km = 1609.344  # metres
    one_gallon_in_liter = 3.785411784  # litres
    return 100_000 / one_mile_in_one_km / miles * one_gallon_in_liter


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
