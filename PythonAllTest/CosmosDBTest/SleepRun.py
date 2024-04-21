import threading
import time

from abc import ABC, abstractmethod


class SleepRun(ABC):
    def __init__(self):
        self.__sleep_time = 10

    @abstractmethod
    def action(self):
        pass

    def run_task(self):
        """

        :return:
        """
        while True:
            self.action()
            time.sleep(self.__sleep_time)

    def start_task(self, sleep_time=10):
        """

        :param sleep_time:
        :return:
        """
        self.__sleep_time = sleep_time
        threading.Thread(target=self.run_task).start()
