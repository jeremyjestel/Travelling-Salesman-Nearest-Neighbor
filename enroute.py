def enroute(table, packs):
    for pack in packs:
        obj = table.search(pack)
        obj.status = "En Route"