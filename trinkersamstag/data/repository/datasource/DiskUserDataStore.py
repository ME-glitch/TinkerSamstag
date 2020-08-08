from trinkersamstag.data.repository.datasource.IUserDataStore import IUserDataStore


class DiskUserDataStore(IUserDataStore):
    def getUserStockDetails(self, stock_id: int):
        pass

    def getUserStocksList(self):
        pass
