"""Defines workflow routing methods, to be used by route_strategy."""
# NOTE: Change these functions to perform custom routing to your workflows and
# steps in your environment. wf_steps.WF_STEPS must also be updated.

import logging
from ua_project_transfer import wf_steps

LOGGER = logging.getLogger("project_creation.next_steps")


def chimerism(payload):
    """Routes samples to the first step of the Chimerism workflow."""
    payload["lims_api"].tools.step_router(
        *wf_steps.WF_STEPS[payload["env"]]["chimerism"],
        payload["art_uris"])


def gce(payload):
    """Routes samples to the first step of the CS-GCE workflow."""
    payload["lims_api"].tools.step_router(
        *wf_steps.WF_STEPS[payload["env"]]["gce"],
        payload["art_uris"])


def pgx(payload):
    """Routes samples to the first step of the GS-PGx workflow."""
    payload["lims_api"].tools.step_router(
        *wf_steps.WF_STEPS[payload["env"]]["pgx"],
        payload["art_uris"])
