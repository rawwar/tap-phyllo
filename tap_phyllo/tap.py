"""phyllo tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_phyllo import streams


class Tapphyllo(Tap):
    """phyllo tap class."""

    name = "tap-phyllo"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "client_id",
            th.StringType,
            required=True,
            secret=False,  # Flag config as protected.
            description="Client ID provided in the Phyllo developer dashboard",
        ),
        th.Property(
            "secret",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="Secret provided in the Phyllo developer dashboard",
        ),
        th.Property(
            "api_url",
            th.StringType,
            default="https://api.sandbox.getphyllo.com",  # Defaults to sandbox url
            description="The url for the API service",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.PhylloStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.ConnectWorkPlatformStream(self),
            streams.ConnectUserStream(self),
        ]


if __name__ == "__main__":
    Tapphyllo.cli()
