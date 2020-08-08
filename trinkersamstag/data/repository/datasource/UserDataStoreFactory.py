from trinkersamstag.data.repository.datasource.DummyUserDataStore import DummyUserDataStore
from trinkersamstag.data.repository.datasource.IUserDataStore import IUserDataStore


class UserDataStoreFactory:
    #    def __init__(self):
    #        pass
    def create(self, userId: int):
        return DummyUserDataStore()
