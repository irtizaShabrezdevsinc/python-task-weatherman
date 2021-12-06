import colors
import datetime


def process(data, year, task_type):
    if task_type == 1:
        highest_temperature(data)
        lowest_temperature(data)
        most_humid(data)
    elif task_type == 2:
        count_avg_high_temp_low_temp_humid(data)
    else:
        high_low_day(data, year)


def highest_temperature(data):
    max_temp_index_save = 0
    index = 0
    # check condition if first values are ''
    first_index = check_first_non_empty(data['max_temperatureC'])
    value = int(data['max_temperatureC'][first_index])
    for j in data['max_temperatureC']:
        if j == "":
            index = 1 + index
            continue
        check = int(j)
        if value < check:
            value = check
            max_temp_index_save = index
        index = 1 + index
    month_day = data['date'][max_temp_index_save].split("-")
    month_day = datetime.datetime(1, int(month_day[1]), int(month_day[2]))
    month_day = month_day.strftime("%B %d")
    print(f"Highest: {value}C on {month_day}")


def check_first_non_empty(list_data):
    index = 0
    for i in list_data:
        if i != '':
            return index
        index = index + 1
    return index


def lowest_temperature(data):
    low_temp_index_save = 0
    index = 0
    # check condition if first values are ''
    first_index = check_first_non_empty(data['min_temperatureC'])
    value = int(data['min_temperatureC'][first_index])
    for j in data['min_temperatureC']:
        if j == "":
            index = 1 + index
            continue
        check = int(j)
        if value > check:
            value = check
            low_temp_index_save = index
        index = 1 + index
    month_day = data['date'][low_temp_index_save].split("-")
    month_day = datetime.datetime(1, int(month_day[1]), int(month_day[2]))
    month_day = month_day.strftime("%B %d")
    print(f"Lowest: {value}C on {month_day}")


def most_humid(data):
    max_humid_index_save = 0
    index = 0
    # check condition if first values are ''
    first_index = check_first_non_empty(data['max_humidity'])
    value = int(data['max_humidity'][first_index])
    for j in data['max_humidity']:
        if j == "":
            index = 1 + index
            continue
        check = int(j)
        if value < check:
            value = check
            max_humid_index_save = index
        index = 1 + index
    month_day = data['date'][max_humid_index_save].split("-")
    month_day = datetime.datetime(1, int(month_day[1]), int(month_day[2]))
    month_day = month_day.strftime("%B %d")
    print(f"Humid: {value}% on {month_day}")


def count_avg_high_temp_low_temp_humid(data):
    number_of_record = 0
    highest_sum = 0
    lowest_sum = 0
    humidity_sum = 0
    index = 0
    for i in data['max_temperatureC']:
        if data['max_temperatureC'][index] != '':
            highest_sum = highest_sum + int(data['max_temperatureC'][index])
        if data['min_temperatureC'][index] != '':
            lowest_sum = lowest_sum + int(data['min_temperatureC'][index])
        if data['max_humidity'][index] != '':
            humidity_sum = humidity_sum + int(data['max_humidity'][index])
        number_of_record = number_of_record + 1
        index = index + 1
    print(f"Highest Average: {round(highest_sum / number_of_record)}C")
    print(f"Lowest Average: {round(lowest_sum / number_of_record)}C")
    print(f"Average Humidity: {round(humidity_sum / number_of_record)}%")


def high_low_day(data, year):
    year_month = year.split("/")
    convert_year = datetime.datetime(int(year_month[0]), int(year_month[1]), 1)
    print(convert_year.strftime("%B %Y"))
    for i in range(len(data['date'])):
        day = data['date'][i]
        day = day.split("-")
        print(day[2], end=" ")
        if data['max_temperatureC'][i] != '':
            temp = int(data['max_temperatureC'][i])
            for j in range(temp):
                print(f"{colors.bcolors.RED}+{colors.bcolors.ENDC}", end="")
            print(f" {temp}C")
        else:
            print("No Data")
        print(day[2], end=" ")
        if data['min_temperatureC'][i] != '':
            temp = int(data['min_temperatureC'][i])
            for j in range(temp):
                print(f"{colors.bcolors.OKBLUE}+{colors.bcolors.ENDC}", end="")
            print(f" {temp}C")
        else:
            print("No data")