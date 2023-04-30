import pandas as pd
from utils.dbframe import SQL2df
import utils.dbacess as dbacess
from datetime import datetime 
from utils.dbframe import SQL2df
from dbacess import ServerAcess
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
import sqlalchemy as sa
import plotly.express as px
import plotly

class GetFinance(): 
    def __init__(self, data_begin:str, data_end:str, acesso, option = 1):
        self.data_begin = data_begin
        self.data_end = data_end
        self.acesso = acesso
        self.option = option

    def getFinance(self):
        if self.data_begin == self.data_end:
            command = f"SELECT * FROM Clientes WHERE CAST(DataVisita AS DATE) = \'{self.data_begin}\';"
        else:
            command = f"SELECT * FROM Clientes WHERE DataVisita BETWEEN \'{self.data_begin}\' AND \'{self.data_end} 23:59:59\';"
        with self.acesso.begin() as conn:
            if self.option:
                customer = pd.read_sql_query(sa.text(command), conn)
            else:
                customer = conn.execute(sa.text(command)).fetchall()
        customer['DataVisita'] = customer['DataVisita'].apply(lambda x: x.strftime('%Y-%m-%d'))
        user = pd.read_sql_table('Usuario0', self.acesso)
        aux = pd.merge(customer, user, on="Matricula")
        output_filtered = aux.groupby(['DataVisita'])['ValorFicha'].sum().reset_index()
        output_chart = px.line(output_filtered, x='DataVisita', y='ValorFicha', title='ValorFicha por DataVisita')
        output_html = plotly.offline.plot(output_chart, include_plotlyjs=False, output_type='div', filename=r'.\Backend\finance.html')
        return output_html