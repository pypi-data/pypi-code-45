# Copyright (C) 2019  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

import copy
import logging
import pytest

from os import path

from swh.loader.package.debian import (
    DebianLoader, download_package, dsc_information, uid_to_person,
    prepare_person, get_package_metadata, extract_package
)
from swh.loader.package.tests.common import check_snapshot, get_stats


logger = logging.getLogger(__name__)


PACKAGE_FILES = {
    'name': 'cicero',
    'version': '0.7.2-3',
    'files': {
        'cicero_0.7.2-3.diff.gz': {
            'md5sum': 'a93661b6a48db48d59ba7d26796fc9ce',
            'name': 'cicero_0.7.2-3.diff.gz',
            'sha256': 'f039c9642fe15c75bed5254315e2a29f9f2700da0e29d9b0729b3ffc46c8971c',  # noqa
            'size': 3964,
            'uri': 'http://deb.debian.org/debian/pool/contrib/c/cicero/cicero_0.7.2-3.diff.gz'  # noqa
        },
        'cicero_0.7.2-3.dsc': {
            'md5sum': 'd5dac83eb9cfc9bb52a15eb618b4670a',
            'name': 'cicero_0.7.2-3.dsc',
            'sha256': '35b7f1048010c67adfd8d70e4961aefd8800eb9a83a4d1cc68088da0009d9a03',  # noqa
            'size': 1864,
            'uri': 'http://deb.debian.org/debian/pool/contrib/c/cicero/cicero_0.7.2-3.dsc'},  # noqa
        'cicero_0.7.2.orig.tar.gz': {
            'md5sum': '4353dede07c5728319ba7f5595a7230a',
            'name': 'cicero_0.7.2.orig.tar.gz',
            'sha256': '63f40f2436ea9f67b44e2d4bd669dbabe90e2635a204526c20e0b3c8ee957786',  # noqa
            'size': 96527,
            'uri': 'http://deb.debian.org/debian/pool/contrib/c/cicero/cicero_0.7.2.orig.tar.gz'  # noqa
        }
    },
}

PACKAGE_FILES2 = {
    'name': 'cicero',
    'version': '0.7.2-4',
    'files': {
        'cicero_0.7.2-4.diff.gz': {
            'md5sum': '1e7e6fc4a59d57c98082a3af78145734',
            'name': 'cicero_0.7.2-4.diff.gz',
            'sha256': '2e6fa296ee7005473ff58d0971f4fd325617b445671480e9f2cfb738d5dbcd01',  # noqa
            'size': 4038,
            'uri': 'http://deb.debian.org/debian/pool/contrib/c/cicero/cicero_0.7.2-4.diff.gz'  # noqa
        },
        'cicero_0.7.2-4.dsc': {
            'md5sum': '1a6c8855a73b4282bb31d15518f18cde',
            'name': 'cicero_0.7.2-4.dsc',
            'sha256': '913ee52f7093913420de5cbe95d63cfa817f1a1daf997961149501894e754f8b',  # noqa
            'size': 1881,
            'uri': 'http://deb.debian.org/debian/pool/contrib/c/cicero/cicero_0.7.2-4.dsc'},  # noqa
        'cicero_0.7.2.orig.tar.gz': {
            'md5sum': '4353dede07c5728319ba7f5595a7230a',
            'name': 'cicero_0.7.2.orig.tar.gz',
            'sha256': '63f40f2436ea9f67b44e2d4bd669dbabe90e2635a204526c20e0b3c8ee957786',  # noqa
            'size': 96527,
            'uri': 'http://deb.debian.org/debian/pool/contrib/c/cicero/cicero_0.7.2.orig.tar.gz'  # noqa
        }
    }
}


PACKAGE_PER_VERSION = {
    'stretch/contrib/0.7.2-3': PACKAGE_FILES,
}


PACKAGES_PER_VERSION = {
    'stretch/contrib/0.7.2-3': PACKAGE_FILES,
    'buster/contrib/0.7.2-4': PACKAGE_FILES2,
}


def test_debian_first_visit(
        swh_config, requests_mock_datadir):
    """With no prior visit, load a gnu project ends up with 1 snapshot

    """
    loader = DebianLoader(
        url='deb://Debian/packages/cicero',
        date='2019-10-12T05:58:09.165557+00:00',
        packages=PACKAGE_PER_VERSION)

    actual_load_status = loader.load()
    expected_snapshot_id = '3b6b66e6ee4e7d903a379a882684a2a50480c0b4'
    assert actual_load_status == {
        'status': 'eventful',
        'snapshot_id': expected_snapshot_id
    }

    stats = get_stats(loader.storage)
    assert {
        'content': 42,
        'directory': 2,
        'origin': 1,
        'origin_visit': 1,
        'person': 1,
        'release': 0,
        'revision': 1,  # all artifacts under 1 revision
        'skipped_content': 0,
        'snapshot': 1
    } == stats

    expected_snapshot = {
        'id': expected_snapshot_id,
        'branches': {
            'releases/stretch/contrib/0.7.2-3': {
                'target_type': 'revision',
                'target': '2807f5b3f84368b4889a9ae827fe85854ffecf07',
            }
        },
    }  # different than the previous loader as no release is done

    check_snapshot(expected_snapshot, loader.storage)


def test_debian_first_visit_then_another_visit(
        swh_config, requests_mock_datadir):
    """With no prior visit, load a debian project ends up with 1 snapshot

    """
    url = 'deb://Debian/packages/cicero'
    loader = DebianLoader(
        url=url,
        date='2019-10-12T05:58:09.165557+00:00',
        packages=PACKAGE_PER_VERSION)

    actual_load_status = loader.load()

    expected_snapshot_id = '3b6b66e6ee4e7d903a379a882684a2a50480c0b4'
    assert actual_load_status == {
        'status': 'eventful',
        'snapshot_id': expected_snapshot_id
    }

    origin_visit = next(loader.storage.origin_visit_get(url))
    assert origin_visit['status'] == 'full'
    assert origin_visit['type'] == 'deb'

    stats = get_stats(loader.storage)
    assert {
        'content': 42,
        'directory': 2,
        'origin': 1,
        'origin_visit': 1,
        'person': 1,
        'release': 0,
        'revision': 1,  # all artifacts under 1 revision
        'skipped_content': 0,
        'snapshot': 1
    } == stats

    expected_snapshot = {
        'id': expected_snapshot_id,
        'branches': {
            'releases/stretch/contrib/0.7.2-3': {
                'target_type': 'revision',
                'target': '2807f5b3f84368b4889a9ae827fe85854ffecf07',
            }
        },
    }  # different than the previous loader as no release is done

    check_snapshot(expected_snapshot, loader.storage)

    # No change in between load
    actual_load_status2 = loader.load()
    assert actual_load_status2['status'] == 'uneventful'
    origin_visit2 = list(loader.storage.origin_visit_get(url))
    assert origin_visit2[-1]['status'] == 'full'
    assert origin_visit2[-1]['type'] == 'deb'

    stats2 = get_stats(loader.storage)
    assert {
        'content': 42 + 0,
        'directory': 2 + 0,
        'origin': 1,
        'origin_visit': 1 + 1,  # a new visit occurred
        'person': 1,
        'release': 0,
        'revision': 1,
        'skipped_content': 0,
        'snapshot': 1,  # same snapshot across 2 visits
    } == stats2

    urls = [
        m.url for m in requests_mock_datadir.request_history
        if m.url.startswith('http://deb.debian.org')
    ]
    # visited each package artifact twice across 2 visits
    assert len(urls) == len(set(urls))


def test_uid_to_person():
    uid = 'Someone Name <someone@orga.org>'
    actual_person = uid_to_person(uid)

    assert actual_person == {
        'name': 'Someone Name',
        'email': 'someone@orga.org',
        'fullname': uid,
    }


def test_prepare_person():
    actual_author = prepare_person({
        'name': 'Someone Name',
        'email': 'someone@orga.org',
        'fullname': 'Someone Name <someone@orga.org>',
    })

    assert actual_author == {
        'name': b'Someone Name',
        'email': b'someone@orga.org',
        'fullname': b'Someone Name <someone@orga.org>',
    }


def test_download_package(datadir, tmpdir, requests_mock_datadir):
    tmpdir = str(tmpdir)  # py3.5 work around (LocalPath issue)
    all_hashes = download_package(PACKAGE_FILES, tmpdir)
    assert all_hashes == {
        'cicero_0.7.2-3.diff.gz': {
            'checksums': {
                'blake2s256': '08b1c438e70d2474bab843d826515147fa4a817f8c4baaf3ddfbeb5132183f21',  # noqa
                'sha1': '0815282053f21601b0ec4adf7a8fe47eace3c0bc',
                'sha1_git': '834ac91da3a9da8f23f47004bb456dd5bd16fe49',
                'sha256': 'f039c9642fe15c75bed5254315e2a29f9f2700da0e29d9b0729b3ffc46c8971c'  # noqa
            },
            'filename': 'cicero_0.7.2-3.diff.gz',
            'length': 3964},
        'cicero_0.7.2-3.dsc': {
            'checksums': {
                'blake2s256': '8c002bead3e35818eaa9d00826f3d141345707c58fb073beaa8abecf4bde45d2',  # noqa
                'sha1': 'abbec4e8efbbc80278236e1dd136831eac08accd',
                'sha1_git': '1f94b2086fa1142c2df6b94092f5c5fa11093a8e',
                'sha256': '35b7f1048010c67adfd8d70e4961aefd8800eb9a83a4d1cc68088da0009d9a03'  # noqa
            },
            'filename': 'cicero_0.7.2-3.dsc',
            'length': 1864},
        'cicero_0.7.2.orig.tar.gz': {
            'checksums': {
                'blake2s256': '9809aa8d2e2dad7f34cef72883db42b0456ab7c8f1418a636eebd30ab71a15a6',  # noqa
                'sha1': 'a286efd63fe2c9c9f7bb30255c3d6fcdcf390b43',
                'sha1_git': 'aa0a38978dce86d531b5b0299b4a616b95c64c74',
                'sha256': '63f40f2436ea9f67b44e2d4bd669dbabe90e2635a204526c20e0b3c8ee957786'  # noqa
            },
            'filename': 'cicero_0.7.2.orig.tar.gz',
            'length': 96527
        }
    }


def test_dsc_information_ok():
    fname = 'cicero_0.7.2-3.dsc'
    dsc_url, dsc_name = dsc_information(PACKAGE_FILES)

    assert dsc_url == PACKAGE_FILES['files'][fname]['uri']
    assert dsc_name == PACKAGE_FILES['files'][fname]['name']


def test_dsc_information_not_found():
    fname = 'cicero_0.7.2-3.dsc'
    package_files = copy.deepcopy(PACKAGE_FILES)
    package_files['files'].pop(fname)

    dsc_url, dsc_name = dsc_information(package_files)

    assert dsc_url is None
    assert dsc_name is None


def test_dsc_information_too_many_dsc_entries():
    # craft an extra dsc file
    fname = 'cicero_0.7.2-3.dsc'
    package_files = copy.deepcopy(PACKAGE_FILES)
    data = package_files['files'][fname]
    fname2 = fname.replace('cicero', 'ciceroo')
    package_files['files'][fname2] = data

    with pytest.raises(
            ValueError, match='Package %s_%s references several dsc' % (
                package_files['name'], package_files['version'])):
        dsc_information(package_files)


def test_get_package_metadata(requests_mock_datadir, datadir, tmp_path):
    tmp_path = str(tmp_path)  # py3.5 compat.
    package = PACKAGE_FILES

    logger.debug('package: %s', package)

    # download the packages
    all_hashes = download_package(package, tmp_path)

    # Retrieve information from package
    _, dsc_name = dsc_information(package)

    dl_artifacts = [(tmp_path, hashes) for hashes in all_hashes.values()]

    # Extract information from package
    extracted_path = extract_package(dl_artifacts, tmp_path)

    # Retrieve information on package
    dsc_path = path.join(path.dirname(extracted_path), dsc_name)
    actual_package_info = get_package_metadata(
        package, dsc_path, extracted_path)

    logger.debug('actual_package_info: %s', actual_package_info)

    assert actual_package_info == {
        'changelog': {
            'date': '2014-10-19T16:52:35+02:00',
            'history': [
                ('cicero', '0.7.2-2'),
                ('cicero', '0.7.2-1'),
                ('cicero', '0.7-1')
            ],
            'person': {
                'email': 'sthibault@debian.org',
                'fullname': 'Samuel Thibault <sthibault@debian.org>',
                'name': 'Samuel Thibault'
            }
        },
        'maintainers': [
            {
                'email': 'debian-accessibility@lists.debian.org',
                'fullname': 'Debian Accessibility Team '
                '<debian-accessibility@lists.debian.org>',
                'name': 'Debian Accessibility Team'
            },
            {
                'email': 'sthibault@debian.org',
                'fullname': 'Samuel Thibault <sthibault@debian.org>',
                'name': 'Samuel Thibault'
            }
        ],
        'name': 'cicero',
        'version': '0.7.2-3'
    }


def test_debian_multiple_packages(swh_config, requests_mock_datadir):
    url = 'deb://Debian/packages/cicero'
    loader = DebianLoader(
        url=url,
        date='2019-10-12T05:58:09.165557+00:00',
        packages=PACKAGES_PER_VERSION)

    actual_load_status = loader.load()
    expected_snapshot_id = 'defc19021187f3727293121fcf6c5c82cb923604'
    assert actual_load_status == {
        'status': 'eventful',
        'snapshot_id': expected_snapshot_id
    }

    origin_visit = next(loader.storage.origin_visit_get(url))
    assert origin_visit['status'] == 'full'
    assert origin_visit['type'] == 'deb'

    expected_snapshot = {
        'id': expected_snapshot_id,
        'branches': {
            'releases/stretch/contrib/0.7.2-3': {
                'target_type': 'revision',
                'target': '2807f5b3f84368b4889a9ae827fe85854ffecf07',
            },
            'releases/buster/contrib/0.7.2-4': {
                'target_type': 'revision',
                'target': '8224139c274c984147ef4b09aa0e462c55a10bd3',
            }
        },
    }

    check_snapshot(expected_snapshot, loader.storage)
