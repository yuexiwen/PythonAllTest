from abc import ABC, abstractmethod


class EntityGenerator(ABC):
    def __init__(self):
        self.primary_key_lst = []
        self.operation_lst = []
        self.document_lst = []

    def set_primary_key(self, primary_key_lst: list):
        self.primary_key_lst = [x for x in primary_key_lst]

    @abstractmethod
    def random_generate_field(self):
        pass

    @abstractmethod
    def operations_generate(self):
        pass

    @abstractmethod
    def document_generate(self):
        pass
