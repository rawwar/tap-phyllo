"""Schema for list_work_platforms endpoint."""
from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("name", th.StringType),
    th.Property("logo_url", th.StringType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("category", th.StringType),
    th.Property("status", th.StringType),
    th.Property("url", th.StringType),
    th.Property(
        "products",
        th.ObjectType(
            th.Property(
                "identity",
                th.ObjectType(
                    th.Property("is_supported", th.BooleanType),
                    th.Property(
                        "audience",
                        th.ObjectType(
                            th.Property("is_supported", th.BooleanType),
                        ),
                    ),
                ),
            ),
            th.Property(
                "engagement",
                th.ObjectType(
                    th.Property("is_supported", th.BooleanType),
                    th.Property(
                        "audience",
                        th.ObjectType(
                            th.Property("is_supported", th.BooleanType),
                        ),
                    ),
                ),
            ),
            th.Property(
                "income",
                th.ObjectType(th.Property("is_supported", th.BooleanType)),
            ),
            th.Property(
                "switch",
                th.ObjectType(th.Property("is_supported", th.BooleanType)),
            ),
            th.Property(
                "activity",
                th.ObjectType(th.Property("is_supported", th.BooleanType)),
            ),
            th.Property(
                "publish",
                th.ObjectType(th.Property("is_supported", th.BooleanType)),
            ),
        ),
    ),
)

schema_dict = schema.to_dict()
