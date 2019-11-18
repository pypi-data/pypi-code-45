# Licensed to CRATE Technology GmbH ("Crate") under one or more contributor
# license agreements.  See the NOTICE file distributed with this work for
# additional information regarding copyright ownership.  Crate licenses
# this file to you under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.  You may
# obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations
# under the License.
#
# However, if you have executed another commercial license agreement
# with Crate these terms will supersede the license and you may use the
# software solely pursuant to the terms of the relevant commercial agreement.

from argparse import Namespace

from croud.config import get_output_format
from croud.printer import print_response
from croud.rest import Client
from croud.session import RequestMethod


def products_list(args: Namespace) -> None:
    """
    Lists available products
    """

    client = Client.from_args(args)
    url = "/api/v2/products/"
    if args.kind:
        data, errors = client.send(RequestMethod.GET, url, params={"kind": args.kind})
    else:
        data, errors = client.send(RequestMethod.GET, url)
    print_response(
        data=data,
        errors=errors,
        keys=["kind", "name", "tier", "description", "scale_summary"],
        output_fmt=get_output_format(args),
    )
