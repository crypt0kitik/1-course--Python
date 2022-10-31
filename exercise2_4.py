# ask driven kilometers outside urban area
# ask the kilometers driven in an urban area
km_out = input("Kilometers outside urban area: \n")
km_out = float(km_out)
km_in = input("Kilometers in an urban area: \n")
km_in = float(km_in)

# make calculations: count fuel consumption
# in area - 5.1l/100km, outside - 7.5l/100km
cons_out = km_out * 5.1 / 100
cons_in = km_in * 7.5 / 100
cons_total = cons_out + cons_in
cons_total = round(cons_total, 2)

# show the results
print(f"Consumption: {cons_total} l")