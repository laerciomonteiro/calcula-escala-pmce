from datetime import datetime, timedelta
import csv

def obter_data_turno(mensagem):
    while True:
        data_str = input(mensagem)
        try:
            data = datetime.strptime(data_str, '%d/%m/%Y')
            return data
        except ValueError:
            print('Data inválida. Tente novamente.')

def imprimir_tabela(turnos):
    print('-' * 45)
    print('| {:^21} | {:^21} |'.format('Turno A', 'Turno B'))
    print('-' * 45)
    for data_a, data_b in turnos:
        print('| {:>11} | {:>11} |'.format(data_a.strftime('%d/%m/%Y'), data_b.strftime('%d/%m/%Y')))
        print('-' * 45)

def exportar_csv(turnos):
    with open('turnos.csv', mode='w', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo, delimiter=';')
        escritor_csv.writerow(['Data do Turno A', 'Data do Turno B'])
        for data_a, data_b in turnos:
            escritor_csv.writerow([data_a.strftime('%d/%m/%Y'), data_b.strftime('%d/%m/%Y')])

# solicita a data do turno A
data_turno_a = obter_data_turno('Digite a data do turno A (formato dd/mm/aaaa): ')

# solicita a data do turno B
data_turno_b = obter_data_turno('Digite a data do turno B (formato dd/mm/aaaa): ')

# calcula as novas datas dos turnos A e B
nova_data_turno_a = data_turno_b + timedelta(days=3)
nova_data_turno_b = nova_data_turno_a + timedelta(days=1)
print('\n')
print("O próximo turno A será em:", nova_data_turno_a.strftime('%d/%m/%Y'))
print("O próximo turno B será em:", nova_data_turno_b.strftime('%d/%m/%Y'))

print('\n')
# solicita ao usuário o número de turnos que deseja exibir
num_turnos = int(input("Agora diga quantos turnos à frente deseja exibir: "))

# loop para imprimir as próximas datas conforme o número de turnos informado
print('\n')
for i in range(num_turnos):
    nova_data_turno_a = nova_data_turno_b + timedelta(days=3)
    nova_data_turno_b = nova_data_turno_a + timedelta(days=1)
    print("Turno A:", nova_data_turno_a.strftime('%d/%m/%Y'), "- Turno B:", nova_data_turno_b.strftime('%d/%m/%Y'))

print('\n')
opcao = input('Deseja exportar a tabela para uma planilha do Excel? (S/N) ').upper()
if opcao == 'S':
    turnos = []
    for i in range(num_turnos):
        nova_data_turno_a = nova_data_turno_b + timedelta(days=3)
        nova_data_turno_b = nova_data_turno_a + timedelta(days=1)
        turnos.append((nova_data_turno_a, nova_data_turno_b))
    exportar_csv(turnos)
    print('Tabela exportada com sucesso.')
else:
    print('Operação cancelada pelo usuário.')

