def get_distances(file, location):
    index = 0
    distances = dict()

    #find index of location
    for row in range(len(file)):
        if location == file[row][0]:
            index = row
            break

#check whole row for not none starting at index 2
    for i in range(2, len(file[index])):
        if file[index][i] != '' and file[index][i] != '0.0':
            distances[file[i-2][0]] = file[index][i]
        else:
            break

    index += 2
#check whole column for not none and not the crossover element
    for i in range(0, len(file)):
        if file[i][index] != '' and file[i][index] != '0.0':
            distances[file[i][0]] = file[i][index]
    return distances