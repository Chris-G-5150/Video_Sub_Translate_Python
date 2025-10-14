class DotDict(dict):
    """Dictionary supporting dot notation access."""

    def __getattr__(self, key):
        try:
            value = self[key]
        except KeyError:
            raise AttributeError(f"No such attribute: {key}")  # noqa: B904

        # If the value is another dict, convert it recursively
        if isinstance(value, dict) and not isinstance(value, DotDict):
            value = DotDict(value)
            self[key] = value  # Cache the converted version
        return value

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        del self[key]

    def to_dict(self):
        """
		Converts back to a dict, handy for JSON usage later. 
		"""
        result = {}
        for k, v in self.items():
            if isinstance(v, DotDict):
                result[k] = v.to_dict()
            else:
                result[k] = v
        return result