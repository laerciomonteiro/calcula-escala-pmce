from datetime import datetime, timedelta

# solicita a data do turno A
data_turno_a_str = input("Digite a data do turno A (formato dd/mm/aaaa): ")

# converte a string de data para o objeto datetime
data_turno_a = datetime.strptime(data_turno_a_str, '%d/%m/%Y')

# solicita a data do turno B
data_turno_b_str = input("Digite a data do turno B (formato dd/mm/aaaa): ")

# converte a string de data para o objeto datetime
data_turno_b = datetime.strptime(data_turno_b_str, '%d/%m/%Y')

# calcula as novas datas dos turnos A e B
nova_data_turno_a = data_turno_b + timedelta(days=3)
nova_data_turno_b = nova_data_turno_a + timedelta(days=1)

print("O próximo turno A será em:", nova_data_turno_a.strftime('%d/%m/%Y'))
print("O próximo turno B será em:", nova_data_turno_b.strftime('%d/%m/%Y'))

print("\nTabela com os turnos A e B dos próximos 03 meses:\n")

# loop para imprimir as próximas 90 datas
for i in range(90):
    nova_data_turno_a = nova_data_turno_b + timedelta(days=3)
    nova_data_turno_b = nova_data_turno_a + timedelta(days=1)
    print("Turno A:", nova_data_turno_a.strftime('%d/%m/%Y'), "- Turno B:", nova_data_turno_b.strftime('%d/%m/%Y'))

