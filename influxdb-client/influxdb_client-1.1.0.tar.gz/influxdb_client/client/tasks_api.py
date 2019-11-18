import datetime
from typing import List

from influxdb_client import TasksService, Task, TaskCreateRequest, TaskUpdateRequest, LabelResponse, LabelMapping, \
    AddResourceMemberRequestBody, RunManually, Run, LogEvent


class TasksApi(object):

    def __init__(self, influxdb_client):
        self._influxdb_client = influxdb_client
        self._service = TasksService(influxdb_client.api_client)

    def find_task_by_id(self, task_id) -> Task:

        task = self._service.get_tasks_id(task_id)
        return task

    def find_tasks(self, **kwargs):
        """List tasks.

        :param str name: only returns tasks with the specified name
        :param str after: returns tasks after specified ID
        :param str user: filter tasks to a specific user ID
        :param str org: filter tasks to a specific organization name
        :param str org_id: filter tasks to a specific organization ID
        :param int limit: the number of tasks to return
        :return: Tasks
        """

        return self._service.get_tasks(**kwargs).tasks

    def create_task(self, task: Task = None, task_create_request: TaskCreateRequest = None) -> Task:

        if task_create_request is not None:
            return self._service.post_tasks(task_create_request)

        if task is not None:
            request = TaskCreateRequest(flux=task.flux, org_id=task.org_id, org=task.org, description=task.description,
                                        status=task.status)

            return self.create_task(task_create_request=request)

        raise ValueError("task or task_create_request must be not None")

    @staticmethod
    def _create_task(name: str, flux: str, every, cron, org_id: str) -> Task:

        task = Task(id=0, name=name, org_id=org_id, status="active", flux=flux)

        repetition = ""
        if every is not None:
            repetition += "every: "
            repetition += every

        if cron is not None:
            repetition += "cron: "
            repetition += '"' + cron + '"'

        flux_with_options = 'option task = {{name: "{}", {}}} \n {}'.format(name, repetition, flux)
        task.flux = flux_with_options

        return task

    def create_task_every(self, name, flux, every, organization) -> Task:
        task = self._create_task(name, flux, every, None, organization.id)
        return self.create_task(task)

    def create_task_cron(self, name: str, flux: str, cron: str, org_id: str) -> Task:
        task = self._create_task(name=name, flux=flux, cron=cron, org_id=org_id, every=None)
        return self.create_task(task)

    def delete_task(self, task_id: str):
        if task_id is not None:
            return self._service.delete_tasks_id(task_id=task_id)

    def update_task(self, task: Task) -> Task:

        req = TaskUpdateRequest(flux=task.flux, description=task.description, every=task.every, cron=task.cron,
                                status=task.status, offset=task.offset)

        return self.update_task_request(task_id=task.id, task_update_request=req)

    def update_task_request(self, task_id, task_update_request: TaskUpdateRequest) -> Task:
        return self._service.patch_tasks_id(task_id=task_id, task_update_request=task_update_request)

    def clone_task(self, task: Task) -> Task:
        cloned = Task(name=task.name, org_id=task.org_id, org=task.org, flux=task.flux, status="active")

        created = self.create_task(cloned)
        labels = self.get_labels(task)
        for label in labels:
            self.add_label(label, created.id)
        return created

    def get_labels(self, task_id):
        return self._service.get_tasks_id_labels(task_id=task_id)

    def add_label(self, label_id: str, task_id: str) -> LabelResponse:
        label_mapping = LabelMapping(label_id=label_id)
        return self._service.post_tasks_id_labels(task_id=task_id, label_mapping=label_mapping)

    def delete_label(self, label_id: str, task_id: str):
        return self._service.delete_tasks_id_labels_id(task_id=task_id, label_id=label_id)

    def get_members(self, task_id: str):
        return self._service.get_tasks_id_members(task_id=task_id).users

    def add_member(self, member_id, task_id):
        user = AddResourceMemberRequestBody(id=member_id)
        return self._service.post_tasks_id_members(task_id=task_id, add_resource_member_request_body=user)

    def delete_member(self, member_id, task_id):
        return self._service.delete_tasks_id_members_id(user_id=member_id, task_id=task_id)

    def get_owners(self, task_id):
        return self._service.get_tasks_id_owners(task_id=task_id).users

    def add_owner(self, owner_id, task_id):
        user = AddResourceMemberRequestBody(id=owner_id)
        return self._service.post_tasks_id_owners(task_id=task_id, add_resource_member_request_body=user)

    def delete_owner(self, owner_id, task_id):
        return self._service.delete_tasks_id_owners_id(user_id=owner_id, task_id=task_id)

    def get_runs(self, task_id, **kwargs) -> List['Run']:
        """
        Retrieve list of run records for a task

        :param task_id: task id
        :param str after: returns runs after specified ID
        :param int limit: the number of runs to return
        :param datetime after_time: filter runs to those scheduled after this time, RFC3339
        :param datetime before_time: filter runs to those scheduled before this time, RFC3339
        """
        return self._service.get_tasks_id_runs(task_id=task_id, **kwargs).runs

    def get_run(self, task_id: str, run_id: str) -> Run:
        """
        Get run record for specific task and run id
        :param task_id: task id
        :param run_id: run id
        :return: Run for specified task and run id
        """
        return self._service.get_tasks_id_runs(task_id=task_id, run_id=run_id)

    def get_run_logs(self, task_id: str, run_id: str) -> List['LogEvent']:
        return self._service.get_tasks_id_runs_id_logs(task_id=task_id, run_id=run_id).events

    def run_manually(self, task_id: str, scheduled_for: datetime = None):
        """
        Manually start a run of the task now overriding the current schedule.

        :param task_id:
        :param scheduled_for: planned execution
        """
        r = RunManually(scheduled_for=scheduled_for)
        return self._service.post_tasks_id_runs(task_id=task_id, run_manually=r)

    def retry_run(self, task_id: str, run_id: str):
        """
        Retry a task run.
        :param task_id: task id
        :param run_id: run id
        """
        return self._service.post_tasks_id_runs_id_retry(task_id=task_id, run_id=run_id)

    def cancel_run(self, task_id: str, run_id: str):
        """
        Cancels a currently running run.
        :param task_id:
        :param run_id:
        """
        return self._service.delete_tasks_id_runs_id(task_id=task_id, run_id=run_id)

    def get_logs(self, task_id: str) -> List['LogEvent']:
        """
        Retrieve all logs for a task.
        :param task_id: task id
        """
        return self._service.get_tasks_id_logs(task_id=task_id).events

    def find_tasks_by_user(self, task_user_id):
        return self.find_tasks(user=task_user_id)
