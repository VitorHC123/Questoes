import json


faturamento_json = '''
{
    "faturamento_diario": [1000, 2000, 0, 1500, 3000, 0, 4000, 0, 3500, 0, 2000, 1800, 0, 1200, 2500, 0, 0, 1600, 3100, 0, 2200, 0, 1700, 0, 0, 1300, 0, 1900, 0, 2500, 0]
}
'''

dados = json.loads(faturamento_json)
faturamento = dados["faturamento_diario"]

faturamento_filtrado = [valor for valor in faturamento if valor > 0]

menor_faturamento = min(faturamento_filtrado)
maior_faturamento = max(faturamento_filtrado)

media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

dias_acima_da_media = sum(1 for valor in faturamento_filtrado if valor > media_mensal)

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")