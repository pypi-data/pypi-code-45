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

from ecl import exceptions
from ecl.orchestration import orchestration_service
from ecl import resource2 as resource
from ecl import utils


class Stack(resource.Resource):
    name_attribute = 'stack_name'
    resource_key = 'stack'
    resources_key = 'stacks'
    base_path = '/stacks'
    service = orchestration_service.OrchestrationService()

    # capabilities
    allow_create = True
    allow_list = True
    allow_get = True
    allow_update = True
    allow_delete = True

    # Properties
    #: Placeholder for AWS compatible template listing capabilities
    #: required by the stack.
    capabilities = resource.Body('capabilities')
    #: Timestamp of the stack creation.
    created_at = resource.Body('creation_time')
    #: A text description of the stack.
    description = resource.Body('description')
    #: Whether the stack will support a rollback operation on stack
    #: create/update failures. *Type: bool*
    is_rollback_disabled = resource.Body('disable_rollback', type=bool)
    #: A list of dictionaries containing links relevant to the stack.
    links = resource.Body('links')
    #: Name of the stack.
    name = resource.Body('stack_name')
    #: Placeholder for future extensions where stack related events
    #: can be published.
    notification_topics = resource.Body('notification_topics')
    #: A list containing output keys and values from the stack, if any.
    outputs = resource.Body('outputs')
    #: The ID of the owner stack if any.
    owner_id = resource.Body('stack_owner')
    #: A dictionary containing the parameter names and values for the stack.
    parameters = resource.Body('parameters', type=dict)
    #: The ID of the parent stack if any
    parent_id = resource.Body('parent')
    #: A string representation of the stack status, e.g. ``CREATE_COMPLETE``.
    status = resource.Body('stack_status')
    #: A text explaining how the stack transits to its current status.
    status_reason = resource.Body('stack_status_reason')
    #: A dict containing the template use for stack creation.
    template = resource.Body('template', type=dict)
    #: Stack template description text. Currently contains the same text
    #: as that of the ``description`` property.
    template_description = resource.Body('template_description')
    #: A string containing the URL where a stack template can be found.
    template_url = resource.Body('template_url')
    #: Stack operation timeout in minutes.
    timeout_mins = resource.Body('timeout_mins')
    #: Timestamp of last update on the stack.
    updated_at = resource.Body('updated_time')
    #: The ID of the user project created for this stack.
    user_project_id = resource.Body('stack_user_project_id')
    #: A Environment information for stack
    environment = resource.Body('environment', type=dict)


    def stack_prepare_request(self, session, requires_id=True, prepend_key=False):
        """Prepare a request with auth header"""

        body = self._body.dirty
        if prepend_key and self.resource_key is not None:
            body = {self.resource_key: body}

        headers = self._header.dirty

        headers["X-Auth-User"] = session.auth._username
        headers["X-Auth-Key"] = session.auth._password

        uri = self.base_path % self._uri.attributes
        if requires_id:
            id = self._get_id(self)
            if id is None:
                raise exceptions.InvalidRequest(
                    "Request requires an ID but none was found")

            uri = utils.urljoin(uri, id)

        return resource._Request(uri, body, headers)

    def create(self, session):
        # This overrides the default behavior of resource creation because
        # heat doesn't accept resource_key in its request.
        # & Will use self.stack_prepare_request to get proper headers.
        if not self.allow_create:
            raise exceptions.MethodNotSupported(self, "create")

        if self.put_create:
            request = self.stack_prepare_request(session, requires_id=True,
                                            prepend_key=False)
            response = session.put(request.uri, endpoint_filter=self.service,
                                   json=request.body, headers=request.headers)
        else:
            request = self.stack_prepare_request(session, requires_id=False,
                                            prepend_key=False)
            response = session.post(request.uri, endpoint_filter=self.service,
                                    json=request.body, headers=request.headers)

        self._translate_response(response)
        return self

    def update(self, session):
        # This overrides the default behavior of resource creation because
        # heat doesn't accept resource_key in its request.
        return super(Stack, self).update(session, prepend_key=False,
                                         has_body=False)

    def _action(self, session, body):
        """Perform stack actions"""
        url = utils.urljoin(self.base_path, self._get_id(self), 'actions')
        resp = session.post(url, endpoint_filter=self.service, json=body)
        return resp.json()

    def check(self, session):
        return self._action(session, {'check': ''})

    def get(self, session, requires_id=True):
        stk = super(Stack, self).get(session, requires_id=requires_id)
        if stk and stk.status in ['DELETE_COMPLETE', 'ADOPT_COMPLETE']:
            raise exceptions.NotFoundException(
                "No stack found for %s" % stk.id)
        return stk

    def abandon(self, session):
        self.base_path = '/stacks/%s/%s/abandon' % (self.name, self.id)

        if not self.allow_delete:
            raise exceptions.MethodNotSupported(self, "delete")

        request = self._prepare_request(requires_id=False)

        response = session.delete(request.uri, endpoint_filter=self.service,
                                  headers={"Accept": ""})

        self._translate_response(response, has_body=False)
        return self


class StackPreview(Stack):
    base_path = '/stacks/preview'

    allow_create = True
    allow_list = False
    allow_get = False
    allow_update = False
    allow_delete = False
