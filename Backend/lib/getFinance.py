import pandas as pd
import sqlalchemy as sa
import plotly.express as px
import plotly
from utils.dbframe import SQL2df

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
            if self.option == 1:
                customer = pd.read_sql_query(sa.text(command), conn)
            else:
                customer = conn.execute(sa.text(command)).fetchall()
        customer['DataVisita'] = pd.to_datetime( customer['DataVisita'].dt.strftime('%d/%m/%Y'))
        user = SQL2df("SELECT Matricula, ValorFicha FROM Usuario0", self.acesso)
        user.rename(columns={"ValorFicha": "Receita"}, inplace =True)
        aux = pd.merge(customer, user, on="Matricula")
        output_filtered = aux.groupby(['DataVisita']).sum().reset_index()
        output_chart = px.bar(output_filtered, x='DataVisita', y="Receita", title='Receita financeira')
        output_chart.update_layout(
        xaxis_title='Data',
        yaxis_title='Receita',
        paper_bgcolor='rgba(0,0,0,0)',
        )
        output_chart.update_xaxes(
            dtick="D1", # sets minimal interval to day
            tickformat="%d/%m/%Y", # the date format you want 
        )
        output_html = plotly.offline.plot(output_chart, filename='.\TP1-engsoft\Backend\\templates\\finance.html', auto_open= True)
        return output_html
