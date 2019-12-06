import zeep
import requests
import xml.etree.ElementTree as et
import xmltodict
from chronopost_python_sdk import Delivery


def create_xml_string(data):
    str1 = f'''
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:tem="http://tempuri.org/">
            <soap:Header/>
            <soap:Body>
                <tem:RegistarExpedicao3 xmlns:ns0="http://tempuri.org/">
                    <tem:username>{data['username']}</tem:username>
                    <tem:password>{data['password']}</tem:password>
                    <tem:expedicao>
                        <tem:Conta>{data['expedicao']['Conta']}</tem:Conta>
                        <tem:OrigemMoradaNome>{data['expedicao']['OrigemMoradaNome']}</tem:OrigemMoradaNome>
                        <tem:OrigemMoradaLinha1>{data['expedicao']['OrigemMoradaLinha1']}</tem:OrigemMoradaLinha1>
                        <tem:OrigemMoradaCodigoPostal>{data['expedicao']['OrigemMoradaCodigoPostal']}</tem:OrigemMoradaCodigoPostal>
                        <tem:OrigemMoradaLocalidade>{data['expedicao']['OrigemMoradaLocalidade']}</tem:OrigemMoradaLocalidade>
                        <tem:OrigemMoradaPais>{data['expedicao']['OrigemMoradaPais']}</tem:OrigemMoradaPais>
                        <tem:OrigemEmail>{data['expedicao']['OrigemEmail']}</tem:OrigemEmail>
                        <tem:TipoDestino>{data['expedicao']['TipoDestino']}</tem:TipoDestino>
                        <tem:DestinoMoradaNome>{data['expedicao']['DestinoMoradaNome']}</tem:DestinoMoradaNome>
                        <tem:DestinoMoradaLinha1>{data['expedicao']['DestinoMoradaLinha1']}</tem:DestinoMoradaLinha1>
                        <tem:DestinoMoradaCodigoPostal>{data['expedicao']['DestinoMoradaCodigoPostal']}</tem:DestinoMoradaCodigoPostal>
                        <tem:DestinoMoradaLocalidade>{data['expedicao']['DestinoMoradaLocalidade']}</tem:DestinoMoradaLocalidade>
                        <tem:DestinoMoradaPais>{data['expedicao']['DestinoMoradaPais']}</tem:DestinoMoradaPais>
                        <tem:DataExpedicao>{data['expedicao']['DataExpedicao']}</tem:DataExpedicao>
                        <tem:EnviarEtiquetasEmail>{data['expedicao']['EnviarEtiquetasEmail']}</tem:EnviarEtiquetasEmail>
                        <tem:NumeroVolumes>{data['expedicao']['NumeroVolumes']}</tem:NumeroVolumes>
                    </tem:expedicao>
                    <tem:tipoResposta>{data['tipoResposta']}</tem:tipoResposta>
                    <tem:enviarEmail>{data['enviarEmail']}</tem:enviarEmail>
                    <tem:email>{data['email']}</tem:email>
                    <tem:tipoEtiqueta>{data['tipoEtiqueta']}</tem:tipoEtiqueta>
                </tem:RegistarExpedicao3>
            </soap:Body>
        </soap:Envelope>
    '''

    return str1


class ChronopostService:

    def __init__(self, username, password, tipoEtiqueta=0,
                 tipoResposta=1, enviarEmail=1,
                 wsdl='https://cliente.chronopost.pt:10003/Services/Services.asmx?wsdl'):
        self.client = zeep.Client(wsdl=wsdl)
        self.username = username
        self.password = password
        # self.email = 'laboratorio@youpii.pt'
        self.email = 'rosado_andre@live.com.pt'
        self.tipoEtiqueta = tipoEtiqueta
        self.tipoResposta = tipoResposta
        self.enviarEmail = enviarEmail

    def dispatch(self, delivery: Delivery):
        url = 'http://cliente.chronopost.pt:10002/Services/Services.asmx'
        header = {'Content-type': 'text/xml'}
        data = {
            "username": self.username,
            "password": self.password,
            "expedicao": delivery.__dict__,
            "tipoEtiqueta": self.tipoEtiqueta,
            "tipoResposta": self.tipoResposta,
            "enviarEmail": self.enviarEmail,
            "email": self.email
        }

        data_string = create_xml_string(data)

        r = requests.post(url, data=data_string, headers=header)
        response_content = xmltodict.parse(r.content)

        response_json = response_content['soap:Envelope']['soap:Body']['RegistarExpedicao3Response']['RegistarExpedicao3Result']

        return response_json

