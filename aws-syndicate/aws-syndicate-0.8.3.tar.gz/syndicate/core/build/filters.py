"""
    Copyright 2018 EPAM Systems, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


def key_including_filter(resources, include_names):
    return dict((k, v) for (k, v) in resources.iteritems() if
                k in include_names)


def key_excluding_filter(resources, exclude_names):
    return dict((k, v) for (k, v) in resources.iteritems() if
                k not in exclude_names)


def value_including_filter(resources, key_name, include_names):
    return dict((k, v) for (k, v) in resources.iteritems() if
                v[key_name] in include_names)


def value_excluding_filter(resources, key_name, exclude_names):
    return dict((k, v) for (k, v) in resources.iteritems() if
                v[key_name] not in exclude_names)
