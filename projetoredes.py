#Projeto de Redes de Computadores 1
#Alunos: Maria Eduarda Guedes Pinto Gianisella
#        William Kutz

from netaddr import *

def calcular_prefixo(hosts):
    tabela = {
        (32769, 65536): '/16',
        (16385, 32768): '/17',
        (8193, 16384): '/18',
        (4097, 8192): '/19',
        (2049, 4096): '/20',
        (1025, 2048): '/21',
        (513, 1024): '/22',
        (257, 512): '/23',
        (129, 256): '/24',
        (65, 128): '/25',
        (33, 64): '/26',
        (17, 32): '/27',
        (9, 16): '/28',
        (5, 8): '/29',
        (0, 4): '/30',
    }

    # Verificar em qual intervalo o número de hosts se encontra
    for intervalo, prefixo in tabela.items():
        min_hosts, max_hosts = intervalo
        if min_hosts <= hosts <= max_hosts:
            return prefixo
    else:
        return None

def atribuir_enderecos(total_maquinas):
    ip_inicial = "192.168.0.0"

    prefixos = [' ', ' ', ' ', ' ']
    redes = [' ', ' ', ' ', ' ']

    # Calcula os intervalos de endereços para cada rede
    prefixos[0] = calcular_prefixo(total_maquinas[0])
    prefixos[1] = calcular_prefixo(total_maquinas[1])
    prefixos[2] = calcular_prefixo(total_maquinas[2])
    prefixos[3] = calcular_prefixo(total_maquinas[3])

    # Atribui os endereços às redes
    redes[0] = f"{ip_inicial}{prefixos[0]}"

    endereco = IPNetwork(redes[0])
    endereco_rede = endereco.broadcast + 1
    redes[1] = IPNetwork(f"{endereco_rede}{prefixos[1]}")

    endereco = IPNetwork(redes[1])
    endereco_rede = endereco.broadcast + 1
    redes[2] = IPNetwork(f"{endereco_rede}{prefixos[2]}")

    endereco = IPNetwork(redes[2])
    endereco_rede = endereco.broadcast + 1
    redes[3] = IPNetwork(f"{endereco_rede}{prefixos[3]}")

    # Retorna as redes atribuídas
    return redes

def imprime_rede(endereco):

    rede = IPNetwork(endereco)

    print("Endereço de rede:", rede.ip)
    print("Máscara de rede:", rede.netmask)
    print("Primeiro endereço útil:", (rede.ip + 1))
    print("Último endereço útil:", (rede.broadcast - 1))
    print("Endereço de broadcast:", rede.broadcast)
    return

# Solicitar o número de máquinas em cada rede 
# Soma 2 endereços para o endereço da rede e de broadcast
maquinas_dmz = int(input("Número de máquinas na DMZ: ")) + 2
maquinas_hosts = int(input("Número de máquinas na rede com hosts: ")) + 2
maquinas_filial = int(input("Número de máquinas na rede da filial: ")) + 2
maquinas_internet = int(input("Número de máquinas na rede da internet: ")) + 2

total_maquinas = [maquinas_dmz, maquinas_hosts, maquinas_filial, maquinas_internet]
total_maquinas = sorted(total_maquinas, reverse=True) # Ordena em ordem decrescente por número de máquinas

redes = atribuir_enderecos(total_maquinas)

# Imprime as redes atribuídas
for i, numero in enumerate(total_maquinas):
    
    if maquinas_dmz == numero:
        print("\nRede DMZ:")
        imprime_rede(redes[i])

    elif maquinas_hosts == numero:
        print("\nRede Hosts:")
        imprime_rede(redes[i])

    elif maquinas_filial == numero:
        print("\nRede Filial:")
        imprime_rede(redes[i])

    elif maquinas_internet == numero:
        print("\nRede Internet:")
        imprime_rede(redes[i])
