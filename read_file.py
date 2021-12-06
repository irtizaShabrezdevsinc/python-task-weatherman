import os

# dict to store the with keys in the form of lists
data = {'date': [], 'max_temperatureC': [], 'mean_temperatureC': [], 'min_temperatureC': [], 'dew_pointC': [],
        'mean_dew_pointC': [], 'min_dew_pointC': [], 'max_humidity': [], 'mean_humidity': [], 'min_humidity': [],
        'max_sea_level_pressurePa': [], 'mean_sea_level_pressurePa': [], 'min_sea_level_pressurePa': [],
        'max_visibilityKm': [], 'mean_visibilityKm': [], 'min_visibilitykm': [], 'max_wind_speedKm/h': [],
        'mean_wind_speedKm/h': [], 'max_gust speedKm/h': [], 'precipitation': [],
        'cloud_cover': [], 'events': [], 'wind_dir_degrees': []}


def add_in_dict(var):
    temp = 0
    for i in data.keys():
        data[i].append(var[temp])
        temp = temp + 1


# Read text File
def read_text_file_lahore(path_file):
    file = open(path_file)
    lines = file.readlines()
    for line in lines[2:-1]:
        var = line.split(",")
        add_in_dict(var)


def read_text_file_other(path_file):
    file = open(path_file)
    lines = file.readlines()
    for line in lines[1:]:
        var = line.split(",")
        add_in_dict(var)


def number_to_month(num):
    if num == "1" or num == "01":
        return "Jan"
    elif num == "2" or num == "02":
        return "Feb"
    elif num == "3" or num == "03":
        return "Mar"
    elif num == "4" or num == "04":
        return "Apr"
    elif num == "5" or num == "05":
        return "May"
    elif num == "6" or num == "06":
        return "Jun"
    elif num == "7" or num == "07":
        return "Jul"
    elif num == "8" or num == "08":
        return "Aug"
    elif num == "9" or num == "09":
        return "Sep"
    elif num == "10" or num == "10":
        return "Oct"
    elif num == "11" or num == "11":
        return "Nov"
    elif num == "12" or num == "12":
        return "Dec"
    else:
        print("Months input value is wrong")
        exit()


def path(name, year, task_type):
    no_file = 0
    path_with_dot = "." + name
    if task_type == 1:
        if 'lahore' in path_with_dot:
            for file in os.listdir(path_with_dot):
                if file.endswith(".txt"):
                    file_path = f"{path_with_dot}/{file}"
                    if year in file_path:
                        no_file = 1
                        read_text_file_lahore(file_path)
        else:
            for file in os.listdir(path_with_dot):
                if file.endswith(".txt"):
                    file_path = f"{path_with_dot}/{file}"
                    if year in file_path:
                        no_file = 1
                        read_text_file_other(file_path)
    else:
        year_month = year.split("/")
        year_month[1] = number_to_month(year_month[1])
        if 'lahore' in path_with_dot:
            for file in os.listdir(path_with_dot):
                if file.endswith(".txt"):
                    file_path = f"{path_with_dot}/{file}"
                    if year_month[0] in file_path:
                        if year_month[1] in file_path:
                            no_file = 1
                            read_text_file_lahore(file_path)
        else:
            for file in os.listdir(path_with_dot):
                if file.endswith(".txt"):
                    file_path = f"{path_with_dot}/{file}"
                    if year_month[0] in file_path:
                        if year_month[1] in file_path:
                            no_file = 1
                            read_text_file_other(file_path)
    if no_file == 0:
        print("There is no such file with that name\nEnter the the correct file name")
        exit()  # exiting the program due
    return data
