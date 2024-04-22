import random

from CosmosDBTest.CosmosDBConnect import CosmosDBConnect
from CosmosDBTest.EntityGenerator import EntityGenerator
from CosmosDBTest.UUIDConsumer import UUIDConsumer


class NetworkEntity(UUIDConsumer, EntityGenerator, CosmosDBConnect):

    def __init__(self, url, database_name, container_name):
        UUIDConsumer.__init__(self)
        EntityGenerator.__init__(self)
        CosmosDBConnect.__init__(self, url, database_name, container_name)
        self.round_trip_times = []
        self.band_width_mbps = []

    def operations_generate(self):
        self.operation_lst.clear()
        for i in range(len(self.primary_key_lst)):
            self.operation_lst.append(
                [
                    {"op": "set", "path": "/RTT", "value": self.round_trip_times[i]},
                    {"op": "set", "path": "/BandWidth", "value": self.band_width_mbps[i]}
                ]
            )

    def document_generate(self):
        self.document_lst.clear()
        for i in range(len(self.primary_key_lst)):
            self.document_lst.append(
                {
                    "id": str(self.primary_key_lst[i]),
                    "RTT": self.round_trip_times[i],
                    "BandWidth": self.band_width_mbps[i]
                }
            )

    def random_generate_field(self):
        self.round_trip_times = [random.randint(0, 100) for _ in range(len(self.primary_key_lst))]
        self.band_width_mbps = [random.randint(1000, 2000) for _ in range(len(self.primary_key_lst))]

    def consume_action(self):
        self.set_primary_key(self.uuid_lst)
        self.random_generate_field()
        self.operations_generate()
        self.document_generate()
        print("=============================================================================")
        self.create_or_update_item(self.primary_key_lst, self.document_lst, self.operation_lst)
