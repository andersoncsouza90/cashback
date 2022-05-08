#importando as bibliotecas
import pandas as pd
import seaborn as sns
import numpy as np
import requests
import matplotlib.pyplot as plt
import streamlit as st


st.set_page_config(layout='centered')
sns.set()

#fazendo a leitura do arquivo e criando um dataframe para o nosso trabalho
df = pd.read_csv(
    'https://docs.google.com/spreadsheets/d/e/2PACX-1vSGf8ui4vEWIk6XUwBkJLaZ0z505o3nC7ozBQmi9Bc4NbDxon15HUEVjZbHSbJemLqdb4GUG_2N52Ne/pub?gid=1806610395&single=true&output=csv')

#limitando para duas casas decimais e desabilitando a notação cientifica
pd.set_option('display.float_format', lambda x: '%.2f' % x)

#verificando dados ausentes
df.isnull().sum()

#alterando a (,) como separador de numeros para (.)
df = df.replace({',': '.'}, regex=True)

#transformandos os dados 'objects' em 'floats'
df.limite_credito=df.limite_credito.astype(float, copy=False)
df.valor_transacoes=df.valor_transacoes.astype(float, copy=False)
df.cp_mercado=df.cp_mercado.astype(float, copy=False)
df.cp_lazer=df.cp_lazer.astype(float, copy=False)
df.cp_servicos=df.cp_servicos.astype(float, copy=False)
df.cp_saude =df.cp_saude .astype(float, copy=False)
df.cp_vestuario=df.cp_vestuario.astype(float, copy=False)
df.cp_casa=df.cp_casa.astype(float, copy=False)


st.write(df)

plt.rc('figure', figsize=(15, 12))
fig, axes = plt.subplots(3, 2)
sns.barplot(ax = axes[0, 0], x='tipo_cartao', y='cp_mercado', 
            data=df,estimator=sum, ci=None)
sns.barplot(ax = axes[0, 1], x='tipo_cartao', y='cp_lazer', 
            data=df,estimator=sum,ci=None)
sns.barplot(ax = axes[1, 0], x='tipo_cartao', y='cp_servicos', 
            data=df,estimator=sum,ci=None)
sns.barplot(ax = axes[1, 1], x='tipo_cartao', y='cp_saude', 
            data=df,estimator=sum,ci=None)
sns.barplot(ax = axes[2, 0], x='tipo_cartao', y='cp_vestuario',
            data=df,estimator=sum,ci=None)
sns.barplot(ax = axes[2, 1], x='tipo_cartao', y='cp_casa',
            data=df,estimator=sum, ci = None)
st.pyplot(fig=plt)



tip =  df.groupby('tipo_cartao')['cp_mercado', 'cp_lazer','cp_servicos'].sum()
tip
st.bar_chart(tip)

# Apply the default theme
sns.set_theme()

# Create a visualization
fig1=sns.relplot(data=df,x="qtd_transacoes", y="cp_mercado",
                 hue="tipo_cartao", style="tipo_cartao")
st.pyplot(fig=fig1)

#sns.jointplot(data=df, x="qtd_transacoes", y="valor_transacoes", hue="tipo_cartao")

figed = sns.catplot(x="estado_civil", y="cp_mercado", 
                    hue="tipo_cartao", kind="bar", data=df, ci = None)
st.pyplot(fig=figed)

fig2 = sns.catplot(x="sexo", y="cp_mercado", hue="tipo_cartao",
                   kind="violin", data=df, ci = None)
st.pyplot(fig=fig2)

