class MenuItem:

    def __init__(self, title, submenu: set = None, callback=[]):
        if submenu is None:
            submenu = set({})
        self.title = title
        self.submenu = submenu

    def __len__(self):
        return len(self.submenu)

    def __iter__(self):
        self._n = 0
        return self

    def __next__(self):
        if self._n < len(self.submenu):
            result = list(self.submenu)[self._n]
            self._n += 1
            return result
        else:
            raise StopIteration


class BackMenuItem:

    def __init__(self):
        self.title = "Back"
        self.submenu = []
        callback = self.goto_parent_menu()
