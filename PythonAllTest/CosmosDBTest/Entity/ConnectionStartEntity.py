import random
import string

from CosmosDBTest.CosmosDBConnect import CosmosDBConnect
from CosmosDBTest.EntityGenerator import EntityGenerator
from CosmosDBTest.UUIDConsumer import UUIDConsumer


class ConnectionStartEntity(UUIDConsumer, EntityGenerator, CosmosDBConnect):
    def __init__(self, url, database_name, container_name):
        UUIDConsumer.__init__(self)
        EntityGenerator.__init__(self)
        CosmosDBConnect.__init__(self, url, database_name, container_name)
        self.State = []
        self.ClientOS = []
        self.ClientVersion = []
        self.ClientType = []
        self.PlatformName = []
        self.PlatformVersion = []
        self.PredecessorConnectionId = []
        self.ResourceType = []
        self.ResourceAlias = []
        self.SessionHostName = []
        self.SessionHostPoolType = []

    def operations_generate(self):
        self.operation_lst.clear()
        for i in range(len(self.primary_key_lst)):
            self.operation_lst.append(
                [
                    {"op": "set", "path": "/State", "value": self.State[i]},
                    {"op": "set", "path": "/ClientOS", "value": self.ClientOS[i]},
                    {"op": "set", "path": "/ClientVersion", "value": self.ClientVersion[i]},
                    {"op": "set", "path": "/ClientType", "value": self.ClientType[i]},
                    {"op": "set", "path": "/PlatformName", "value": self.PlatformName[i]},
                    {"op": "set", "path": "/PlatformVersion", "value": self.PlatformVersion[i]},
                    {"op": "set", "path": "/PredecessorConnectionId", "value": self.PredecessorConnectionId[i]},
                    {"op": "set", "path": "/ResourceType", "value": self.ResourceType[i]},
                    {"op": "set", "path": "/ResourceAlias", "value": self.ResourceAlias[i]},
                    {"op": "set", "path": "/SessionHostName", "value": self.SessionHostName[i]}
                ]
            )

    def document_generate(self):
        self.document_lst.clear()
        for i in range(len(self.primary_key_lst)):
            self.document_lst.append(
                {
                    "id": str(self.primary_key_lst[i]),
                    "State": self.State[i],
                    "ClientOS": self.ClientOS[i],
                    "ClientVersion": self.ClientVersion[i],
                    "ClientType": self.ClientType[i],
                    "PlatformName": self.PlatformName[i],
                    "PlatformVersion": self.PlatformVersion[i],
                    "PredecessorConnectionId": self.PredecessorConnectionId[i],
                    "ResourceType": self.ResourceType[i],
                    "ResourceAlias": self.ResourceAlias[i],
                    "SessionHostName": self.SessionHostName[i],
                    "SessionHostPoolType": self.SessionHostPoolType[i]
                }
            )

    def random_generate_field(self):
        self.State = ["started" for _ in range(len(self.primary_key_lst))]
        self.ClientOS = ["OS_".join(random.choices(string.ascii_letters, k=3)) for _ in range(len(self.primary_key_lst))]
        self.ClientVersion = ["CV_".join(random.choices(string.ascii_letters, k=3)) for _ in range(len(self.primary_key_lst))]
        self.ClientType = ["CT_".join(random.choices(string.ascii_letters, k=3)) for _ in range(len(self.primary_key_lst))]
        self.PlatformName = ["PN_".join(random.choices(string.ascii_letters, k=3)) for _ in range(len(self.primary_key_lst))]
        self.PlatformVersion = ["PV_".join(random.choices(string.ascii_letters, k=3)) for _ in range(len(self.primary_key_lst))]
        self.PredecessorConnectionId = ["CID_".join(random.choices(string.ascii_letters, k=3)) for _ in range(len(self.primary_key_lst))]
        self.ResourceType = ["RT_".join(random.choices(string.ascii_letters, k=3)) for _ in range(len(self.primary_key_lst))]
        self.ResourceAlias = ["RA_".join(random.choices(string.ascii_letters, k=3)) for _ in range(len(self.primary_key_lst))]
        self.SessionHostName = ["SH_".join(random.choices(string.ascii_letters, k=3)) for _ in range(len(self.primary_key_lst))]
        self.SessionHostPoolType = ["SHPT_".join(random.choices(string.ascii_letters, k=3)) for _ in range(len(self.primary_key_lst))]

    def consume_action(self):
        self.set_primary_key(self.uuid_lst)
        self.random_generate_field()
        self.operations_generate()
        self.document_generate()
        print("-----------------------------------------------------------------------------")
        self.create_or_update_item(self.primary_key_lst, self.document_lst, self.operation_lst)
