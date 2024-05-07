from helpers.mph import to_str, to_minutes


# return the object instance for the id provided
def lookup(table, key):
    obj = table.search(key)
    return obj


#
def at_time(time, path):
    # convert the time given to minutes
    time = to_minutes(time) / 60
    status = []
    # dont include the hub in the status array
    for pack in path:
        if pack[0] == "HUB":
            continue
        deliv_time = pack[2]
        # add new row to status array including the id status and
        if deliv_time < time:
            status.append([pack[0], "Delivered", to_str(deliv_time)])
            loaded = pack[3]
        elif pack[0] in loaded:
            status.append([pack[0], "En Route", to_str(deliv_time)])
        else:
            status.append([pack[0], "At The Hub", to_str(deliv_time)])
    return status
