"""Schema for list_users endpoint."""
from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("name", th.StringType),
    th.Property("external_id", th.StringType),
    th.Property("id", th.StringType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("status", th.StringType),
)

schema_dict = schema.to_dict()
