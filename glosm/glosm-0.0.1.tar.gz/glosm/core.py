"""Core API."""

import os
import json

from typing import Any


class Secrets:
    """Main API class representing a collection of secrets loaded from a secrets file."""

    path_secrets_file = "~/.glosm.json"

    def __init__(self) -> None:
        """Load secrets from JSON file into a dictionary."""
        with open(os.path.expanduser(self.path_secrets_file), "r") as f:
            self._secrets = json.load(f)

    def get(self, *keys) -> Any:
        """Get a secret, specified by one or more keys. Without any keys, return all secrets.

        The keys are traversed recursively. If `secrets.get()` returns `{1: {2: {3: 4}}}` then `secrets.get(1, 2, 3)`
        will return `4`.
        """
        if not keys:
            return self._secrets

        result = self._secrets
        for key in keys:
            result = result[key]

        return result
