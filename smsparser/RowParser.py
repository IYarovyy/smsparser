class RowParser:
    def __init__(self, header, row):
        self.header = header
        self.row = row

    def get_text(self):
        i = self.header.get("text")
        if i is None:
            i = 4
        return str(self.row[i].value or "")

    def get_time(self):
        i = self.header.get("time")
        if i is None:
            i = self.header.get("event_timestamp")
            if i is None:
                i = 1
        return str(self.row[i].value or "")

    def get_sender(self):
        i = self.header.get("sender")
        if i is None:
            i = self.header.get("a")
            if i is None:
                i = 2
        return str(self.row[i].value or "")

    def get_recipient(self):
        i = self.header.get("recipient")
        if i is None:
            i = self.header.get("b")
            if i is None:
                i = 3
        return str(self.row[i].value or "")

    def get_lac(self):
        i = self.header.get("lac")
        if i is None:
            i = 5
        try:
            return str(self.row[i].value or "")
        except Exception:
            return ""

    def get_cell(self):
        i = self.header.get("cell")
        if i is None:
            i = 6
        try:
            return str(self.row[i].value or "")
        except Exception:
            return ""

    def get_address(self):
        i = self.header.get("address")
        if i is None:
            i = 7
        try:
            return str(self.row[i].value or "")
        except Exception:
            return ""
