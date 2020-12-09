from itertools import permutations, combinations_with_replacement

final_sequence_city = None
final_max_temp = None
city_with_temp = {
    "Lake Havasu City": [71, 65, 63, 66, 68],
    "Sedona": [62, 47, 45, 51, 56],
    "Flagstaff": [46, 35, 33, 40, 44],
    "Casa Grande": [76, 69, 60, 64, 69],
    "chandler": [77, 68, 61, 65, 67],
}
length_of_day = None
for city_name, list_temprature in city_with_temp.items():
    length_of_day = len(list_temprature)

if length_of_day:
    city_list = list(city_with_temp.keys())

    permutations_of_hotel_name = permutations(city_list)

    temp_list_for_max_temprature = list()
    for variation in list(permutations_of_hotel_name):
        variation_list = list(variation)

        list_according_day_temprature = [city_with_temp[x][index] for index, x in enumerate(variation_list)]
        avarage_temp_with_variation = sum(list_according_day_temprature) / length_of_day

        temp_list_for_max_temprature.append(avarage_temp_with_variation)
        if len(temp_list_for_max_temprature) != 1:
            max_temp = max(temp_list_for_max_temprature)
            if max_temp == avarage_temp_with_variation:
                final_max_temp = avarage_temp_with_variation
                final_sequence_city = variation_list
                temp_list_for_max_temprature = temp_list_for_max_temprature[1:]

            else:
                temp_list_for_max_temprature = temp_list_for_max_temprature[:-1]

print(final_sequence_city)
print(final_max_temp)
