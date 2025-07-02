class Field:
    def __init__(self, name, abstract=False):
        self.name = name
        self.validators = []
        self.normalizators = []
        self.abstract = abstract
        self.list_template = ""
        self.input_template = ""
        self.label_template = ""
        self.detail_template = ""

    def parse_value(self, obj):
        """
        Returns value from sqla-model

        :param obj: SQLA model instance
        """
        return getattr(obj, self.name, None)