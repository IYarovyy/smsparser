class RowParser:
    def __init__(self, header, row):
        self.header = header
        self.row = row

    def get_text(self):
        i = self.header["text"]
        return str(self.row[i].value)

    def get_time(self):
        i = self.header.get("time")
        if i is None:
            i = self.header.get("event_timestamp")
        return str(self.row[i].value)

    def get_sender(self):
        i = self.header.get("sender")
        if i is None:
            i = self.header.get("a")
        return str(self.row[i].value)

    def get_recipient(self):
        i = self.header.get("recipient")
        if i is None:
            i = self.header.get("b")
        return str(self.row[i].value)

    def get_lac(self):
        i = self.header.get("lac")
        if i is None:
            i = 6
        return str(self.row[i].value)

    def get_cell(self):
        i = self.header.get("cell")
        if i is None:
            i = 7
        return str(self.row[i].value)

    def get_address(self):
        i = self.header.get("address")
        if i is None:
            i = 8
        return str(self.row[i].value)
