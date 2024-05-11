from CosmosDBTest.Entity.ConnectionStartEntity import ConnectionStartEntity
from CosmosDBTest.Entity.NetworkEntity import NetworkEntity
from CosmosDBTest.UUIDGenerator import UUIDGenerator

generator = UUIDGenerator()
connection_entity = ConnectionStartEntity("https://xiwtest.documents.azure.com:443/", "xiwtest", "xiwtest1")
network_entity = NetworkEntity("https://xiwtest.documents.azure.com:443/", "xiwtest", "xiwtest1")
connection_entity.set_generator(generator)
network_entity.set_generator(generator)

generator.start_task(20)
network_entity.start_task(2)
connection_entity.start_task(5)
