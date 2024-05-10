# NetAddr Subnet Calculator

## Desenvolvido por:
- Maria Eduarda Guedes Pinto Gianisella
- William Kutz

## Descrição:
Este projeto consiste em um script Python para calcular e atribuir endereços IP a redes de computadores com base no número de máquinas em cada rede. Ele também imprime informações detalhadas sobre cada rede atribuída, como endereço de rede, máscara de rede, primeiro e último endereço útil e endereço de broadcast.

## Funcionalidades:
- Calcula o prefixo da máscara de sub-rede com base no número de máquinas em cada rede.
- Atribui endereços IP a redes de computadores.
- Imprime informações detalhadas sobre cada rede atribuída.

## Requisitos:
- Python 3.x
- Biblioteca `netaddr`

## Como usar:
1. Execute o script Python.
2. Siga as instruções para inserir o número de máquinas em cada rede.
3. O script calculará automaticamente os endereços IP para cada rede e imprimirá as informações detalhadas.

## Exemplo de Uso:
```bash
$ python netaddr_subnet_calculator.py
Número de máquinas na DMZ: 50
Número de máquinas na rede com hosts: 100
Número de máquinas na rede da filial: 20
Número de máquinas na rede da internet: 500

Rede DMZ:
Endereço de rede: 192.168.0.0
Máscara de rede: 255.255.255.192
Primeiro endereço útil: 192.168.0.1
Último endereço útil: 192.168.0.62
Endereço de broadcast: 192.168.0.63

Rede Hosts:
Endereço de rede: 192.168.0.64
Máscara de rede: 255.255.255.128
Primeiro endereço útil: 192.168.0.65
Último endereço útil: 192.168.0.126
Endereço de broadcast: 192.168.0.127

Rede Filial:
Endereço de rede: 192.168.0.128
Máscara de rede: 255.255.255.224
Primeiro endereço útil: 192.168.0.129
Último endereço útil: 192.168.0.158
Endereço de broadcast: 192.168.0.159

Rede Internet:
Endereço de rede: 192.168.0.160
Máscara de rede: 255.255.255.128
Primeiro endereço útil: 192.168.0.161
Último endereço útil: 192.168.0.254
Endereço de broadcast: 192.168.0.255
