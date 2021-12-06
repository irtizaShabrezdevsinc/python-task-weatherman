def verify_path(path):
    if path[1] == '-e':
        year = len(path[2].split("-"))
        if year == 1:
            return 1
        else:
            return -1
    elif path[1] == '-a':
        year = len(path[2].split("/"))
        if year == 2:
            return 2
        else:
            return -1
    elif path[1] == '-c':
        year = len(path[2].split("/"))
        if year == 2:
            return 3
        else:
            return -1
    else:
        return -1
