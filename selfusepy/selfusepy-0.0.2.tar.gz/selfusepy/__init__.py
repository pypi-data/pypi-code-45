#  The Apache License Version 2.0
#  Copyright (c) 2019
#  Author : Luoming Xu
#  Project Name : selfusepy
#  File Name : __init__.py
#  CreateTime: 2019/11/26 20:45

import json
from typing import TypeVar
from url import Request, HTTPResponse

import jsonparse

T = TypeVar('T')


def parse_json(j: str, obj: T) -> T:
  """
  Json to Python Object
  >>>import selfusepy
  >>>obj: T = selfusepy.parse_json(jsonStr, Obj())
  :param j: json string
  :param obj: Py Object
  :return: obj
  """

  jsonparse.generate_class_dict(obj)
  json_dict: dict = json.loads(j)
  j_modified: str = jsonparse.add_classname(json_dict, type(obj).__name__)
  obj = json.loads(j_modified, object_hook = jsonparse.deserialize_object)

  jsonparse.class_dict.clear()
  return obj


req: Request = Request()


def get(url: str, head: dict = None, **params: dict) -> HTTPResponse:
  return req.get(url, head, **params)


def put(url: str, head: dict = None, body: object = None, **params: dict) -> HTTPResponse:
  return req.put(url, body, head, **params)


def post(url: str, body: object, head: dict = None, **params: dict) -> HTTPResponse:
  return req.post(url, body, head, **params)


def delete(url: str, head: dict = None, **params: dict) -> HTTPResponse:
  return req.delete(url, head, **params)
