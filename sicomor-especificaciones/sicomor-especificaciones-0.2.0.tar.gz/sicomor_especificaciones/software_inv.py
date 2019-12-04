# identificador xxyyzzzz
# xx-> tipo1: 11: SW
# yy-> tipo2: SW: 02 SW
SOFTWARE_INV = [
    {"tipo1": "SW",
     "tipo2": "SW",
     "identificador": 11020001,
     "descripcion": "Paquete Office Instalado",
     "unidad": "str",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 2,
                   "clase": "Aplicaciones",
                   "function": "get_app_office"}
     },
    {"tipo1": "SW",
     "tipo2": "SW",
     "identificador": 11020002,
     "descripcion": "Aplicaciones Instaladas",
     "unidad": "str",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 2,
                   "clase": "Aplicaciones",
                   "function": "get_app"}
     },
    {"tipo1": "SW",
     "tipo2": "SW",
     "identificador": 11020003,
     "descripcion": "Drivers Instalados",
     "unidad": "str",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 3,
                   "clase": "Driver",
                   "function": "get_items"}
     },
    {"tipo1": "SW",
     "tipo2": "SW",
     "identificador": 11020004,
     "descripcion": "Procesos",
     "unidad": "str",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 4,
                   "clase": "Proceso",
                   "function": "get_info_proccess"}
     },
    {"tipo1": "SW",
     "tipo2": "SW",
     "identificador": 11020005,
     "descripcion": "Servicios",
     "unidad": "str",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 5,
                   "clase": "Servicios",
                   "function": "get_items"}
     },
    {"tipo1": "SW",
     "tipo2": "SW",
     "identificador": 11020006,
     "descripcion": "Configuración de la Bios",
     "unidad": "str",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 6,
                   "clase": "Bios",
                   "function": "get_items"}
     },
]
