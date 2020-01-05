class OneShotDict(dict):
    def __init__(self, existing=None):
        super().__init__()
        if existing is not None:
            for k,v in existing:
                self[k] = v

    def __setitem__(self, key, value):
        if key in self:
            raise ValueError("cant assign to existing key")
        super().__setitem__(key, value)

