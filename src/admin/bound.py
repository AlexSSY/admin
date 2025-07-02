class BoundField:
    """
    Field + FormData
    """
    def __init__(self, field, form_data):
        self.field = field
        self.form_data = form_data
        self.value = form_data.get(self.field.name)
        self.errors = []

    def _normalize(self, value):
        normalized_value = value.copy()
        for n in self.field.normalizators:
            normalized_value = n(normalized_value)
        return normalized_value


    def validate(self):
        self.errors = []

        for v in self.field.validators:
            field_name = self.field.name
            field_value = self._normalize(self.form_data.get(field_name))
            validation_result = v(field_name, field_value)
            if validation_result is not None:
                self.errors.append(validation_result)

        return bool(self.errors)