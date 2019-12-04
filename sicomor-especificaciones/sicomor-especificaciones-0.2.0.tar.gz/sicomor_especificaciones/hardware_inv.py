# identificador xxyyzzzz
# xx-> tipo1: 10: HW
#             11: SW
# yy-> tipo2: HW: 01 PROC
# 			      10 MEM
# 			      11 DISK
# 			      11 CPU
# 			      02 GPU
# 			      20 BOA
# 			      22 RED
# 			      03 SON
# 			      30 CDR
# 			      33 IMP
# 			      04 MON
# 			      40 TEC

HARDWARE_INV = [
    ####################
    #      MEMORIA     #
    ####################
    {"tipo1": "HW",
     "tipo2": "MEM",
     "identificador": 10100001,
     "descripcion": "Información de Memoria Virtual",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 1,
                   "clase": "Memoria",
                   "function": "get_all_virt"}
     },
    {"tipo1": "HW",
     "tipo2": "MEM",
     "identificador": 10100002,
     "descripcion": "Memoria Física Por SLOTs",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 1,
                   "clase": "Memoria",
                   "function": "get_items"}
     },
    {"tipo1": "HW",
     "tipo2": "MEM",
     "identificador": 10100003,
     "descripcion": "Información de memoria Swap",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 1,
                   "clase": "Memoria",
                   "function": "get_all_swap"}
     },
    ####################
    #      CPU         #
    ####################
    {"tipo1": "HW",
     "tipo2": "CPU",
     "identificador": 10120001,
     "descripcion": "Información de CPU",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 2,
                   "clase": "CPU",
                   "function": "get_items"}
     },
    {"tipo1": "HW",
     "tipo2": "CPU",
     "identificador": 10120002,
     "descripcion": "Estadísticas  de CPU",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 2,
                   "clase": "Cpu",
                   "function": "get_all"}
     },
    ####################
    #      DISCO       #
    ####################
    {"tipo1": "HW",
     "tipo2": "DISK",
     "identificador": 10110001,
     "descripcion": "Información de Discos",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 3,
                   "clase": "DiscoWin",
                   "function": "get_items"}
     },
    {"tipo1": "HW",
     "tipo2": "DISK",
     "identificador": 10110002,
     "descripcion": "Información y estadísticas por cada partición de un disco",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 4,
                   "clase": "Disco",
                   "function": "get_uso_disco"}
     },
    {"tipo1": "HW",
     "tipo2": "DISK",
     "identificador": 10110004,
     "descripcion": "Información de las particiones de un disco",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 5,
                   "clase": "Particion",
                   "function": "get_items"}
     },
    ####################
    #      GPU         #
    ####################
    {"tipo1": "HW",
     "tipo2": "GPU",
     "identificador": 10020001,
     "descripcion": "Información de placas de videos",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 6,
                   "clase": "GPU",
                   "function": "get_items"}
     },
    ####################
    #      BOARD         #
    ####################
    {"tipo1": "HW",
     "tipo2": "BOA",
     "identificador": 10200001,
     "descripcion": "Información de placas Madre",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 7,
                   "clase": "Placa",
                   "function": "get_items"}
     },
    ####################
    #      RED         #
    ####################
    {"tipo1": "HW",
     "tipo2": "RED",
     "identificador": 10220001,
     "descripcion": "Información de dispositivos de Red",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 7,
                   "clase": "Red",
                   "function": "get_items"}
     },
    {"tipo1": "HW",
     "tipo2": "RED",
     "identificador": 10220002,
     "descripcion": "Información de dispositivos de Red Físicos",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 7,
                   "clase": "Red",
                   "function": "get_physicalDevices"}
     },
    {"tipo1": "HW",
     "tipo2": "RED",
     "identificador": 10220003,
     "descripcion": "Información de conectividad Ethernet",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 7,
                   "clase": "Red",
                   "function": "get_ethernetConnection"}
     },
    {"tipo1": "HW",
     "tipo2": "RED",
     "identificador": 10220004,
     "descripcion": "Información de conectividad Wi-Fi",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 7,
                   "clase": "Red",
                   "function": "get_wifiConnection"}
     },
    ####################
    #      SONIDO      #
    ####################
    {"tipo1": "HW",
     "tipo2": "SON",
     "identificador": 10030001,
     "descripcion": "Información de dispositivos de sonido",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 8,
                   "clase": "Sonido",
                   "function": "get_items"}
     },
    ####################
    #      CDROM       #
    ####################
    {"tipo1": "HW",
     "tipo2": "CDR",
     "identificador": 10300001,
     "descripcion": "Información de dispositivos de CD-ROM",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 9,
                   "clase": "CDROM",
                   "function": "get_items"}
     },
    ####################
    #      IMPRESORAS  #
    ####################
    {"tipo1": "HW",
     "tipo2": "IMP",
     "identificador": 10330001,
     "descripcion": "Información de dispositivos de Impresión",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 10,
                   "clase": "Impresora",
                   "function": "get_items"}
     },
    ####################
    #      MONITOR     #
    ####################
    {"tipo1": "HW",
     "tipo2": "MON",
     "identificador": 10040001,
     "descripcion": "Información de Monitores",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 11,
                   "clase": "Monitor",
                   "function": "get_items"}
     },
    ####################
    #      TECLADO     #
    ####################
    {"tipo1": "HW",
     "tipo2": "MON",
     "identificador": 10400001,
     "descripcion": "Información del Teclado",
     "estado": True,
     # ----------------------------------------------------
     "manejador": {"id": 12,
                   "clase": "Teclado",
                   "function": "get_items"}
     },
]
