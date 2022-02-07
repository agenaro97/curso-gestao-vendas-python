import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC81a6ee5fee6c9ba727e231c181b84f1a"
# Your Auth Token from twilio.com/console
auth_token  = "e50a723c491427a8aff585d371a5553c"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'data/{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():    # .any() algum valor
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]   # .loc localiza [linha, coluna] resposta em tabela
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]    # quando usa loc, usar .values[0] onde retorna apenas valor
        print(f'No mes {mes}, alguém bateu a meta. Vendedor: {vendedor}, vendas: {vendas}')

