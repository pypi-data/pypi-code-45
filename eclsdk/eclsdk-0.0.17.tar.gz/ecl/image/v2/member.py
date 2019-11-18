# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from ecl.image import image_service
from ecl import resource2


class Member(resource2.Resource):
    resources_key = 'members'
    service = image_service.ImageService()
    base_path = '/' + service.version + '/images/%(image_id)s/members'

    # Capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    # Properties

    # See https://bugs.launchpad.net/glance/+bug/1526991 for member/member_id
    # 'member' is documented incorrectly as being deprecated but it's the
    # only thing that works. 'member_id' is not accepted.

    #: The ID of the image member. An image member is a tenant
    #: with whom the image is shared.
    member_id = resource2.Body('member_id')
    #: The date and time when the member was created.
    created_at = resource2.Body('created_at')
    #: Image ID stored through the image API. Typically a UUID.
    image_id = resource2.URI('image_id')
    #: The status of the image.
    status = resource2.Body('status')
    #: The URL for schema of the member.
    schema = resource2.Body('schema')
    #: The date and time when the member was updated.
    updated_at = resource2.Body('updated_at')
    #: Member_id used to create a member
    member = resource2.Body('member', alternate_id=True)

    def update(self, session, image_id, member_id, status):
        """Update the member of an image."""

        uri = self.base_path + '/%(member_id)s'
        uri = uri % {"image_id":image_id, "member_id":member_id}
        resp = session.put(
            uri,
            json={"status":status},
            headers={"Accept": "application/json"},
            endpoint_filter=self.service
        )
        self._translate_response(resp, has_body=True)
        return self
