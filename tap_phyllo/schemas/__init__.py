"""Schemas for tap-phyllo."""
from .connect.list_users import schema_dict as list_users
from .connect.list_work_platforms import schema_dict as list_work_platforms

__all__ = ["list_users", "list_work_platforms"]
