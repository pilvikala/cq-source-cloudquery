from dataclasses import dataclass, field
from cloudquery.sdk.scheduler import Client as ClientABC

from plugin.cloudquery.client import CloudQueryClient

DEFAULT_CONCURRENCY = 100
DEFAULT_QUEUE_SIZE = 10000


@dataclass
class Spec:
    base_url: str = field(default="https://api.cloudquery.io")
    concurrency: int = field(default=DEFAULT_CONCURRENCY)
    queue_size: int = field(default=DEFAULT_QUEUE_SIZE)

    def validate(self):
        pass
        # if self.access_token is None:
        #     raise Exception("access_token must be provided")


class Client(ClientABC):
    def __init__(self, spec: Spec) -> None:
        self._spec = spec
        self._client = CloudQueryClient(spec.base_url)

    def id(self):
        return "cloudquery"

    @property
    def client(self) -> CloudQueryClient:
        return self._client
