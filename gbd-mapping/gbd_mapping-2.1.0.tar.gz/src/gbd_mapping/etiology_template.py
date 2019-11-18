"""Mapping templates for GBD etiologies.

This code is automatically generated by gbd_mapping_generator/etiology_builder.py

Any manual changes will be lost.
"""
from typing import Union

from .id import reiid
from .base_template import ModelableEntity, GbdRecord


class Etiology(ModelableEntity):
    """Container for etiology GBD ids and metadata."""
    __slots__ = ('name', 'kind', 'gbd_id', 'population_attributable_fraction_yll_exists',
                 'population_attributable_fraction_yld_exists', 'population_attributable_fraction_yll_in_range',
                 'population_attributable_fraction_yld_in_range', )

    def __init__(self,
                 name: str,
                 kind: str,
                 gbd_id: Union[reiid, None],
                 population_attributable_fraction_yll_exists: bool,
                 population_attributable_fraction_yld_exists: bool,
                 population_attributable_fraction_yll_in_range: bool,
                 population_attributable_fraction_yld_in_range: bool, ):
        super().__init__(name=name,
                         kind=kind,
                         gbd_id=gbd_id)
        self.name = name
        self.kind = kind
        self.gbd_id = gbd_id
        self.population_attributable_fraction_yll_exists = population_attributable_fraction_yll_exists
        self.population_attributable_fraction_yld_exists = population_attributable_fraction_yld_exists
        self.population_attributable_fraction_yll_in_range = population_attributable_fraction_yll_in_range
        self.population_attributable_fraction_yld_in_range = population_attributable_fraction_yld_in_range


class Etiologies(GbdRecord):
    """Container for GBD etiologies."""
    __slots__ = ('cholera', 'non_typhoidal_salmonella', 'shigella', 'enteropathogenic_e_coli',
                 'enterotoxigenic_e_coli', 'campylobacter', 'entamoeba', 'cryptosporidium', 'rotavirus', 'aeromonas',
                 'clostridium_difficile', 'norovirus', 'adenovirus', 'influenza', 'pneumococcal_pneumonia',
                 'h_influenzae_type_b', 'respiratory_syncytial_virus', )

    def __init__(self,
                 cholera: Etiology,
                 non_typhoidal_salmonella: Etiology,
                 shigella: Etiology,
                 enteropathogenic_e_coli: Etiology,
                 enterotoxigenic_e_coli: Etiology,
                 campylobacter: Etiology,
                 entamoeba: Etiology,
                 cryptosporidium: Etiology,
                 rotavirus: Etiology,
                 aeromonas: Etiology,
                 clostridium_difficile: Etiology,
                 norovirus: Etiology,
                 adenovirus: Etiology,
                 influenza: Etiology,
                 pneumococcal_pneumonia: Etiology,
                 h_influenzae_type_b: Etiology,
                 respiratory_syncytial_virus: Etiology, ):
        super().__init__()
        self.cholera = cholera
        self.non_typhoidal_salmonella = non_typhoidal_salmonella
        self.shigella = shigella
        self.enteropathogenic_e_coli = enteropathogenic_e_coli
        self.enterotoxigenic_e_coli = enterotoxigenic_e_coli
        self.campylobacter = campylobacter
        self.entamoeba = entamoeba
        self.cryptosporidium = cryptosporidium
        self.rotavirus = rotavirus
        self.aeromonas = aeromonas
        self.clostridium_difficile = clostridium_difficile
        self.norovirus = norovirus
        self.adenovirus = adenovirus
        self.influenza = influenza
        self.pneumococcal_pneumonia = pneumococcal_pneumonia
        self.h_influenzae_type_b = h_influenzae_type_b
        self.respiratory_syncytial_virus = respiratory_syncytial_virus
