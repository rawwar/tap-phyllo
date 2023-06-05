"""Stream type classes for tap-phyllo."""

from __future__ import annotations

from tap_phyllo import schemas
from tap_phyllo.client import PhylloStream


class ConnectWorkPlatformStream(PhylloStream):
    """Connect - List Work platforms stream."""

    name = "list_work_platforms"
    path = "/v1/work-platforms"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema = schemas.list_work_platforms


class ConnectUserStream(PhylloStream):
    """Connect - List Work platforms stream."""

    name = "list_users"
    path = "/v1/users"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema = schemas.list_users
