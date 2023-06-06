"""Schema for list accounts."""

from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("created_at", th.StringType),
    th.Property("updated_at", th.StringType),
    th.Property(
        "user",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        ),
    ),
    th.Property(
        "work_platform",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
            th.Property("logo_url", th.StringType),
        ),
    ),
    th.Property("platform_username", th.StringType),
    th.Property("profile_pic_url", th.StringType),
    th.Property("status", th.StringType),
    th.Property("platform_profile_name", th.StringType),
    th.Property("platform_profile_id", th.StringType),
    th.Property("platform_profile_published_at", th.StringType),
    th.Property(
        "data",
        th.ObjectType(
            th.Property(
                "identity",
                th.ObjectType(
                    th.Property("status", th.StringType),
                    th.Property("last_sync_at", th.StringType),
                    th.Property("monitoring_type", th.StringType),
                ),
            ),
            th.Property(
                "engagement",
                th.ObjectType(
                    th.Property("status", th.StringType),
                    th.Property("last_sync_at", th.StringType),
                    th.Property("refresh_since", th.StringType),
                    th.Property("data_available_from", th.StringType),
                    th.Property("monitoring_type", th.StringType),
                ),
            ),
        ),
    ),
)

schema_dict = schema.to_dict()
