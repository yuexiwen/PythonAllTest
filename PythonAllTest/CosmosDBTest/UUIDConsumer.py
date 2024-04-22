from abc import abstractmethod
from CosmosDBTest.SleepRun import SleepRun
from CosmosDBTest.UUIDGenerator import UUIDGenerator


class UUIDConsumer(SleepRun):
    def __init__(self):
        super().__init__()
        self.uuid_lst = []
        self.__uuid_generator: UUIDGenerator = None

    def set_generator(self, uuid_generator: UUIDGenerator):
        self.__uuid_generator = uuid_generator

    def action(self):
        self.uuid_lst = self.__uuid_generator.fetch_ids()
        self.consume_action()

    @abstractmethod
    def consume_action(self):
        pass

