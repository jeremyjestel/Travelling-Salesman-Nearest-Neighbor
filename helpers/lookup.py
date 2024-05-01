from helpers.mph import to_str, to_minutes


def lookup(table, id):
    obj = table.search(id)
    return obj
def at_time(table, time, path):
    time = to_minutes(time) / 60
    status = []
    for pack in path:
        if pack[0] == "HUB":
            continue
        deliv_time = pack[2]
        if deliv_time < time:
            status.append([pack[0], "Delivered", to_str(pack[2])])
            loaded = pack[3]
        elif pack[0] in loaded:
            status.append([pack[0], "En Route", to_str(pack[2])])
        else:
            status.append([pack[0], "At The Hub", to_str(pack[2])])




    return status