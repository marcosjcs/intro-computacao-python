def MinMax(temps):
    print("A menor temp do mês foi:", mínima(temps),"ºC.")
    print("A maior temp do mês foi:", máxima(temps),"ºC.")

def mínima(temps):
    temps.sort()
    return temps[0]

def máxima(temps):
    temps.sort()
    return temps[len(temps)-1]
