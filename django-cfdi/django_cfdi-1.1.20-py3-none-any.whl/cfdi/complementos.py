from django.template.loader import render_to_string
from cfdi.functions import to_decimal, to_int

class ComplementoField():
    def __init__(self, *args, **kwargs):
        self.required = kwargs.pop("required", False)
        super(ComplementoField, self).__init__(*args, **kwargs)


    def clean(self, value, name):
        if not value and self.required:
            raise ValueError(
                f"{name}: El campo es obligatorio"
            )

class IntegerField(ComplementoField):
    def __init__(self, *args, **kwargs):
        self.max_digits = kwargs.pop("max_digits", None)
        super(IntegerField, self).__init__(*args, **kwargs)

    def clean(self, value, name):
        """
            valida que el valor del campo sea entero y el máximo de dígitos
        """
        super().clean(value, name)
        if isinstance(value, str) and value.isnumeric():
            return to_int(value)

        if not isinstance(value, int):
            raise ValueError(
                f"{name}: El valor debe ser entero"
            )

        if self.max_digits and len(value) > max_digits:
            raise ValueError(
                f"{name}: El número máximo de digitos es de {max_digits} ({len(value)})"
            )

        return value

class CharField(ComplementoField):
    def __init__(self, *args, **kwargs):
        self.max_length = kwargs.pop("max_length", None)
        super(CharField, self).__init__(*args, **kwargs)

    def clean(self, value, name):
        """
            valida el máximo de caracteres
        """
        super().clean(value, name)
        if self.max_length and len(value) > max_length:
            raise ValueError(
                f"{name}: El número máximo de caracteres es de"
                f"{max_length} ({len(max_length)})"
            )

        return value
    

class CfdiComplemento():
    xmlns_list = []
    schemaLocation = ""
    def get_xml_string(self):
        xml = render_to_string(
            self.template, 
            { 'complemento': self, }
        )
        
        return xml

    def __setattr__(self, name, value):
        field = getattr(self.__class__, name, None)
        if field and isinstance(field, IntegerField) or isinstance(field, CharField):
            value = field.clean(value,name)
        super().__setattr__(name, value)


class ComplementoINE(CfdiComplemento):
    tipo_proceso = CharField()
    tipo_comite = CharField()
    clave_entidad = CharField()
    id_contabilidad = CharField()
    template = 'cfdi/complementos/ine.xml'

    xmlns_list = [
        'xmlns:ine="http://www.sat.gob.mx/ine"',
    ]
    schemaLocation = 'http://www.sat.gob.mx/ine http://www.sat.gob.mx/inehttp://www.sat.gob.mx/sitio_internet/cfd/ine/ine11.xsd'

    def get_ambito_entidad(self):
        from cfdi.classes import escape
        if "estatal" in escape(self.tipo_comite).lower():
            return "Federal"
        else:
            return "Local"

    
class ComplementoIEDU(CfdiComplemento):
    nombreAlumno = CharField()
    CURP = CharField()
    nivelEducativo = CharField()
    autRVOE = CharField()
    rfcPago = CharField()
    template = 'cfdi/complementos/iedu.xml'

class ComplementoDetallista(CfdiComplemento):
    documentStatus = CharField()
    entityType = CharField()
    code = CharField()
    detallista = CharField()
    cantidad_letra = CharField()
    referenceIdentification = CharField(required=True)
    fecha_oc = CharField()
    deliveryNote = CharField()
    fecha_referencia = CharField()
    buyerGLN = IntegerField(required=True)
    personDepartament = CharField()
    sellerGLN = IntegerField(required=True)
    template = 'cfdi/complementos/detallista.xml'

    xmlns_list = [
        'xmlns:detallista="http://www.sat.gob.mx/detallista"',
    ]


class ComplementoImpuestosLocales(CfdiComplemento):
    retenciones_locales = []
    traslados_locales = []
    template = 'cfdi/complementos/impuestos_locales.xml'

    xmlns_list = [
        'xmlns:implocal="http://www.sat.gob.mx/implocal"',
    ]
    schemaLocation = "http://www.sat.gob.mx/implocal http://www.sat.gob.mx/sitio_internet/cfd/implocal/implocal.xsd"

    @property
    def total_retenciones_locales(self):
        total = 0
        for rl in self.retenciones_locales:
            total += to_decimal(rl["monto"])
        return total

    @property
    def total_traslados_locales(self):
        total = 0
        for rl in self.traslados_locales:
            total += to_decimal(rl["monto"])
        return total
 
class ComplementoComercioExterior(CfdiComplemento):

    CertificadoOrigen = CharField()
    ClaveDePedimento = CharField()
    NumCertificadoOrigen = CharField()
    NumeroExportadorConfiable = CharField()
    Incoterm = CharField()
    Observaciones = CharField()
    Subdivision = CharField()
    TipoCambioUSD = CharField()
    TipoOperacion = CharField()
    TotalUSD = CharField()
    Emisor = {}
    Receptor = {}
    template = 'cfdi/complementos/comercio_exterior.xml'

    xmlns_list = [
        'xmlns:cce11="http://www.sat.gob.mx/ComercioExterior11"',
    ]

class ComplementoContruccionLicencia(CfdiComplemento):
    licencia = CharField()
    calle = CharField()
    no_exterior = CharField()
    no_interior = CharField()
    colonia = CharField()
    localidad = CharField()
    referencia = CharField()
    municipio = CharField()
    estado = CharField()
    codigo_postal = CharField()
    template = 'cfdi/complementos/construccion_licencia.xml'

    xmlns_list = [
        'xmlns:servicioparcial="http://www.sat.gob.mx/servicioparcialconstruccion"',
    ]
    schemaLocation = "http://www.sat.gob.mx/servicioparcialconstruccion http://www.sat.gob.mx/sitio_internet/cfd/servicioparcialconstruccion/servicioparcialconstruccion.xsd"

class ComplementoLeyendasFiscales(CfdiComplemento):
    leyendasFiscales = []
    template = 'cfdi/complementos/leyendas_fiscales.xml'
    
    xmlns_list = [
        'xmlns:leyendasFisc="http://www.sat.gob.mx/leyendasFiscales"',
    ]
    schemaLocation = "http://www.sat.gob.mx/leyendasFiscales http://www.sat.gob.mx/sitio_internet/cfd/leyendasFiscales/leyendasFisc.xsd"


class ComplementoNomina(CfdiComplemento):
    TipoNomina = CharField()
    TipoNomina = CharField()
    FechaPago = CharField()
    FechaInicialPago = CharField()
    FechaFinalPago = CharField()
    NumDiasPagados = CharField()
    NumDiasPagados = CharField()
    Emisor = {}
    Receptor = {}
    Percepciones = {}
    Deducciones = {}
    OtrosPagos = {}
    Incapacidades = {}
    TotalPercepciones = CharField()
    TotalDeducciones = CharField()
    TotalOtrosPagos = CharField()
    
    template = 'cfdi/complementos/nomina.xml'
    xmlns_list = [
        'xmlns:nomina12="http://www.sat.gob.mx/nomina12"',
        'xmlns:catNomina="http://www.sat.gob.mx/sitio_internet/cfd/catalogos/Nomina"',
        'xmlns:tdCFDI="http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI"',
        'xmlns:catCFDI="http://www.sat.gob.mx/sitio_internet/cfd/catalogos"',
    ]
    schemaLocation = "http://www.sat.gob.mx/nomina12 http://www.sat.gob.mx/sitio_internet/cfd/nomina/nomina12.xsd"


class ComplementoPago(CfdiComplemento):
    pagos = []
    template = 'cfdi/complementos/pago.xml'
    xmlns_list = [
        'xmlns:pago10="http://www.sat.gob.mx/Pagos"',
    ]
    schemaLocation = "http://www.sat.gob.mx/Pagos http://www.sat.gob.mx/sitio_internet/cfd/Pagos/Pagos10.xsd"

