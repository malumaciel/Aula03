nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salario: "))
percentual = float(input("Digite seu percentual"))

## calculo
valorreal = (salario * percentual) / 100
novosalario = salario  + valorreal


print(f"ola! {nome} sua idade é {idade}, seu salário é {novosalario}")


