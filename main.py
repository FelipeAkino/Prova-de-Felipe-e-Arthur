from Classes import ContaLuz,Contas

historiContas = Contas()

historiContas.addContaLuz(ContaLuz("125","001",150,"29/05/23","05/06/23",300))
historiContas.addContaLuz(ContaLuz("125","002",175,"29/06/23","05/07/23",350))
historiContas.addContaLuz(ContaLuz("125","003",190,"29/07/23","05/08/23",400))
historiContas.addContaLuz(ContaLuz("125","004",210,"29/08/23","05/09/23",450))
historiContas.addContaLuz(ContaLuz("125","005",237,"29/09/23","05/10/23",260))
historiContas.addContaLuz(ContaLuz("125","006",143,"29/10/23","05/11/23",280))
print(historiContas.mediaConsumoValor())
print(historiContas.verificarContas())