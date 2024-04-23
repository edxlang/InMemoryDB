from typing import Any


class InMemoryDB:

    def __init__(self):
        self.temp_trans_data = {}
        self.trans_data = {}
        self.is_active = False

    def begin_transaction(self):
        if self.is_active:
            raise Exception("Begin Err: Transaction already active")
        self.is_active = True

    def put(self, key: str, value: int):
        if not self.is_active:
            raise Exception("Put Err: Transaction not active")
        self.temp_trans_data[key] = value

    def get(self, key: str) -> int | None:
        if key in self.trans_data:
            return self.trans_data.get(key)
        return None

    def commit(self):
        if not self.is_active:
            raise Exception("Commit Err: No transaction in progress")
        self.trans_data.update(self.temp_trans_data)
        self.temp_trans_data = {}
        self.is_active = False

    def rollback(self):
        if not self.is_active:
            raise Exception("Rollback Err: No transaction in progress")
        self.temp_trans_data = {}
        self.is_active = False

