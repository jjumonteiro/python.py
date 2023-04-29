P1 = [8.5, 7.0, 9.5, 6.0, 8.0]
P2 = [9.0, 8.0, 7.5, 6.5, 8.5]

media_p1 = sum(P1) / len(P1)
media_p2 = sum(P2) / len(P2)
#sum: soma len: quantidade


# Imprimindo as médias
print(f'Média da turma na prova 1: {media_p1:.2f}')
print(f'Média da turma na prova 2: {media_p2:.2f}')

# Verificação de qual prova teve a melhor media
if media_p1 > media_p2:
    print('A prova 1 teve a melhor nota.')

elif media_p2 > media_p1:
    print('A prova 2 teve a melhor nota.')

else:
    print('Obteve a mesma média nas duas provas.')
