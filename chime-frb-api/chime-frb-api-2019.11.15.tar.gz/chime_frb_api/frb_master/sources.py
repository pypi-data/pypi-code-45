#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import typing as t

from chime_frb_api.core import API

JSON = t.Union[str, int, float, bool, None, t.Mapping[str, "JSON"], t.List["JSON"]]
log = logging.getLogger(__name__)


class Sources(object):
    """
    CHIME/FRB Sources API

    Parameters
    ----------
    API : chime_frb_api.core.API class-type

    Returns
    -------
    object-type
    """

    def __init__(self, API: API):
        self.API = API

    def get_source(self, source_name: str) -> JSON:
        assert source_name, AttributeError("source_name is required")
        return self.API.get("/v1/sources/{}".format(source_name))

    def get_expected_spectrum(self, source_name: str) -> JSON:
        assert source_name, AttributeError("source_name is required")
        return self.API.get("/v1/sources/spectrum/{}".format(source_name))
