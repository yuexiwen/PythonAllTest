from CosmosDBTest.Entity.ConnectionStartEntity import ConnectionStartEntity
from CosmosDBTest.UUIDGenerator import UUIDGenerator

generator = UUIDGenerator()
connection_entity = ConnectionStartEntity("https://xiwtest.documents.azure.com:443/", "xiwtest", "xiwtest1")
connection_entity.set_generator(generator)
generator.start_task(20)
connection_entity.start_task(5)
