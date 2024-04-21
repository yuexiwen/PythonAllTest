import uuid

from readerwriterlock import rwlock
from CosmosDBTest.SleepRun import SleepRun


class UUIDGenerator(SleepRun):
    def __init__(self, size=10):
        self.__lst = []
        self.__size = size
        self.__lock = rwlock.RWLockFairD()

    def generate_ids(self):
        """
        Clear the original list and fill in new UUID, count is __size
        This operation will write lock to __lst
        :return: no return but will change the __lst
        """
        with self.__lock.gen_wlock():
            self.__lst.clear()
            self.__lst = [uuid.uuid4() for i in range(self.__size)]

    def fetch_ids(self):
        """
        Fetch the current __lst, this operation will read lock __lst
        :return: __lst
        """
        with self.__lock.gen_rlock():
            return self.__lst

    def action(self):
        self.generate_ids()
