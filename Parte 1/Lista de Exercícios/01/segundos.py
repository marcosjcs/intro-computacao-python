segundos_str = input("Digite o número de segundos: ")
total_seg = int(segundos_str)

horas = total_seg // 3600
dias = horas // 24
horas = horas % 24
segs = total_seg % 3600
minutos = segs // 60
segs = segs % 60

print(dias, "dias,", horas,"horas,", minutos, "minutos e", segs,"segundos.")
