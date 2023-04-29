import sys
sys.path.insert(0, r'.\TP1-engsoft\Backend\utils')
from dbacess import ServerAcess
import tokenBalance as tb
import haveLunch as hv

def rotaHaveLunch(matricula):
    tes = ServerAcess("LAPTOP-4BELV735", "credito_ru")
    pegar = tb.GetToken(matricula, tes)
    comer = hv.HaveLunch(matricula, pegar.getToken(),tes )
    comer.haveLunch()