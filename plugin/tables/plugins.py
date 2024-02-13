from typing import Any, Generator

import pyarrow as pa
from cloudquery.sdk.scheduler import TableResolver
from cloudquery.sdk.schema import Column
from cloudquery.sdk.schema import Table
from cloudquery.sdk.schema.resource import Resource

from plugin.client import Client


class Plugins(Table):
    def __init__(self) -> None:
        super().__init__(
            name="cloudquery_plugins",
            title="CloudQuery Plugins",
            columns=[
                Column("name", pa.string()),
                Column("kind", pa.string()),
                Column("team_name", pa.string()),
                Column("display_name", pa.string()),
                Column("category", pa.string()),
                Column("created_at", pa.string()),
                Column("updated_at", pa.string()),
                Column("homepage", pa.string()),
                Column("logo", pa.string()),
                Column("official", pa.bool_()),
                Column("short_description", pa.string()),
                Column("repository", pa.string()),
                Column("tier", pa.string()),
                Column("usd_per_row", pa.string()),
                Column("free_rows_per_month", pa.uint64()),
                Column("release_stage", pa.string()),
            ],
        )

    @property
    def resolver(self):
        return PluginResolver(table=self)


class PluginResolver(TableResolver):
    def __init__(self, table) -> None:
        super().__init__(table=table)

    def resolve(
        self, client: Client, parent_resource: Resource
    ) -> Generator[Any, None, None]:
        for item_response in client.client.item_iterator():
            yield item_response
