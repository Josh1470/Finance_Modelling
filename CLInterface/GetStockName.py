from CLInterface import DataRepresentation as DR

def split(word):
    return [char for char in word]


def getName(*args):
    stock = DR.graphStockData.currentStock(*args)
    temp = split(stock)
    if temp[0] == 'A':
        if temp[1] == 'M':
            return 'Amazon'
        elif temp[1] == 'A':
            return 'Apple'
    elif temp[0] == 'M':
        return 'Microsoft'
    elif temp[0] == 'G':
        return 'Google'
    elif temp[0] == 'F':
        return 'Facebook'
    elif temp[0] == 'T':
        return 'Telsa'
    elif temp[0] == 'N':
        return 'Nvidia'
    else:
        return stock








