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

horas = int(segundos_totais/3600)
minutos = int(segundos_totais/60) - (horas * 60)
segundos = segundos_totais - (horas *3600) - (minutos *60)

print(horas,"h",minutos,"m",segundos,"s")