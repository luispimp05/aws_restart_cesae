#programa calcula a duração hh:mm:s de um album músical com 5 songs.

#duração das canções é lida em minutos e segundos


musica_1_minutos = int(input(" -Introduza minutos da música 1: "))
musica_1_segundos =int(input(" -Introduza segundos da música 1: "))

musica_2_minutos = int(input(" -Introduza minutos da música 2: "))
musica_2_segundos = int(input(" -Introduza segundos da música 2: "))

musica_3_minutos = int(input(" -Introduza minutos da música 3: "))
musica_3_segundos = int(input(" -Introduza segundos da música 3: "))

musica_4_minutos = int(input(" -Introduza minutos da música 4: "))
musica_4_segundos = int(input(" -Introduza segundos da música 4: "))

musica_5_minutos = int(input(" -Introduza minutos da música 5: "))
musica_5_segundos = int(input(" -Introduza segundos da música 5: "))

segundos_totais = 60 * (musica_1_minutos + musica_2_minutos + musica_3_minutos + musica_4_minutos + musica_5_minutos) + (musica_1_segundos + musica_2_segundos + musica_3_segundos +musica_4_segundos + musica_5_segundos)
minutos_totais = segundos_totais / 60
horas_totais = minutos_totais / 60

print(f"{horas_totais}h {minutos_totais}m {segundos_totais}s")
