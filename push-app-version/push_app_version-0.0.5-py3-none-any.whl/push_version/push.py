#!/usr/bin/env python3
#
# Copyright (C) 2019 by eHealth Africa : http://www.eHealthAfrica.org
#
# See the NOTICE file distributed with this work for additional information
# regarding copyright ownership.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

import argparse
import os
import sys

from google.cloud import exceptions
from google.cloud import storage

parser = argparse.ArgumentParser()
parser.add_argument('--project', required=True)
parser.add_argument('--version', required=True)


def get_required(name):
    try:
        return os.environ[name]
    except KeyError as key:
        raise RuntimeError('Missing {} environment variable!'.format(key))


def setup():
    client = storage.Client()
    client.from_service_account_json(get_required('GOOGLE_APPLICATION_CREDENTIALS'))
    bucket = client.get_bucket(get_required('RELEASE_BUCKET'))
    if not bucket.exists():
        raise RuntimeError('Bucket: {} does not exist or is not accessible.'.format(GCS_BUCKET))
    return bucket


def push_release(version, project):
    bucket = setup()
    print('Pushing new version {} for project {}...'.format(version, project))
    try:
        blob = bucket.blob('{}/version'.format(project))
        blob.upload_from_string(version, content_type='text/plain')
    except exceptions.GoogleCloudError as err:
        raise RuntimeError(err)


def main():
    try:
        args = parser.parse_args()
        push_release(args.version, args.project)
    except Exception as e:
        print(str(e))
        sys.exit(1)

if __name__ == '__main__':
    main()
