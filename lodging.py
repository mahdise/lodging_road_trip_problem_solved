from itertools import permutations, combinations_with_replacement

best_route_hotel_list = None
best_max_budget = None
budget = 850
hotel_with_price = {
    "Motel 6": 89,
    "Best Western": 109,
    "Holiday Inn Express": 115,
    "Courtyard by Marriott": 229,
    "Residence Inn": 199,
    "Hampton Inn": 209,
}
hotel_list = list(hotel_with_price.keys())

temp_save = list()
temp_save.append(30)
permutations_of_hotel_name = permutations(hotel_list)
for combination_hotel in list(permutations_of_hotel_name):
    temp_list_hotel = list(combination_hotel)
    temp_list_hotel = temp_list_hotel[:-1]

    extract_price = [hotel_with_price[y] for y in temp_list_hotel]
    total_count = sum(extract_price)
    deference_price = budget - total_count
    if deference_price < 0:
        continue

    temp_save.append(deference_price)

    calculate_minimum = min(temp_save)

    if calculate_minimum == deference_price:
        lowest_price = deference_price
        temp_save = temp_save[1:]
        best_max_budget = total_count
        best_route_hotel_list = temp_list_hotel



    else:
        temp_save = temp_save[:-1]

print(best_route_hotel_list)
print(best_max_budget)
