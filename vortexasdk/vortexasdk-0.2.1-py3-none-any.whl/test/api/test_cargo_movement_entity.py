from unittest import TestCase

import jsons

from vortexasdk.api.cargo_movement import CargoEvent, CargoMovement
from vortexasdk.api.vessel import VesselEntity
from vortexasdk.api.corporation import CorporateEntity
from vortexasdk.api.product import ProductEntity
from vortexasdk.api.geography import GeographyEntity


class TestCargoMovementEntity(TestCase):

    def test_serialize(self):
        with open("tests/api/examples/cargo_movement_entity1.json", 'r') as f:
            serialized = f.read()
            deserialized = jsons.loads(serialized, CargoMovement)

            dictionary = {
                "cargo_movement_id": "00886b05a0747522b67322f50123ee60e61e2allowed_high_entropy_string",
                "quantity": 4401,
                "status": "unloaded_state",
                "vessels": [
                    VesselEntity(**{
                        "id": "9cbf7c0fc6ccf1dfeacde02b87f3b6b165303allowed_high_entropy_string",
                        "mmsi": 255804460,
                        "imo": 9480980,
                        "name": "JOHANN ESSBERGER",
                        "dwt": 5260,
                        "cubic_capacity": 6100,
                        "vessel_class": "tiny_tanker",
                        "corporate_entities": [
                            CorporateEntity(**{
                                "id": "f9bd45e65e292909a7b751b0026dcf7795c61allowed_high_entropy_string",
                                "label": "Essberger J.T.",
                                "layer": "commercial_owner",
                                "probability": 1,
                                "source": "external"
                            })
                        ],
                        "start_timestamp": "2017-04-18T21:38:34+0000",
                        "end_timestamp": "2017-04-25T00:40:46+0000",
                        "fixture_fulfilled": False,
                        "voyage_id": "401f0e74fc42401248a484aca2e9955dea885allowed_high_entropy_string",
                        "tags": [],
                        "status": "vessel_status_laden_known"
                    })
                ],
                "product": [
                    ProductEntity(**{
                        "id": "b68cbb746f8b9098c50e2ba36bcad83001a53allowed_high_entropy_string",
                        "layer": "group",
                        "probability": 0.4756425,
                        "source": "model",
                        "label": "Clean products"
                    }),
                    ProductEntity(**{
                        "id": "a75fcc09bfc7d16496de3336551bc52b58918allowed_high_entropy_string",
                        "layer": "group_product",
                        "probability": 0.4756425,
                        "source": "model",
                        "label": "Biodiesel"
                    }),
                    ProductEntity(**{
                        "id": "9d52ede1cff0421a8cd7283b0171afe8d23f5allowed_high_entropy_string",
                        "layer": "grade",
                        "probability": 0.4756425,
                        "source": "model",
                        "label": "Biodiesel Feedstock"
                    })
                ],
                "events": [
                    CargoEvent(**{
                        "event_type": "cargo_port_load_event",
                        "location": [
                            GeographyEntity(**{
                                "id": "2dfc3d43a21697c02ec3b2700b3b570a6ed1aallowed_high_entropy_string",
                                "layer": "country",
                                "label": "Netherlands",
                                "source": "model",
                                "probability": 1
                            })
                        ],
                        "probability": 1,
                        "pos": [
                            4.29914090037834,
                            51.87936163368058
                        ],
                        "start_timestamp": "2017-04-18T21:38:34+0000",
                        "end_timestamp": "2017-04-20T16:41:49+0000"
                    })
                ]
            }

            expected = CargoMovement(**dictionary)

            assert expected == deserialized
