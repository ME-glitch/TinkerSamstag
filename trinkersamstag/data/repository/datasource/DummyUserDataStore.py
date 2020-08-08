from trinkersamstag.data.repository.datasource.IUserDataStore import IUserDataStore


class DummyUserDataStore(IUserDataStore):
    def getUserStockDetails(self, stock_id: int):
        pass

    def getUserStocksList(self):
        pass
