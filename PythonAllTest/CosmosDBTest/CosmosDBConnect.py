from azure.cosmos import CosmosClient, PartitionKey, exceptions
from azure.identity import DefaultAzureCredential


class CosmosDBConnect:
    def __init__(self, url, database_name, container_name):
        self.url = url
        self.database_name = database_name
        self.container_name = container_name
        self.credential = DefaultAzureCredential()
        self.client = CosmosClient(url, self.credential)
        self.database = self.client.create_database_if_not_exists(id=database_name)
        self.container = self.database.create_container_if_not_exists(id=container_name, partition_key=PartitionKey(path='/id', kind='Hash'))

    def create_or_update_item(self, doc_id: list, documents: list, operations: list):
        if len(documents) != len(operations):
            print("input error")
            return
        for i in range(len(doc_id)):
            try:
                self.container.read_item(item=str(doc_id[i]), partition_key=str(doc_id[i]))
                print(f"find doc_id {str(doc_id[i])}, update it")
                self.container.patch_item(item=str(doc_id[i]), partition_key=str(doc_id[i]), patch_operations=operations[i])
            except exceptions.CosmosResourceNotFoundError:
                print(f"cannot find {str(doc_id[i])} in container, now create it")
                self.container.create_item(body=documents[i])
