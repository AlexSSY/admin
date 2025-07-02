from .fields import Field


class AdminViewMeta(type):
    # ! возможная проблема ибо нету обхода __mro__
    def __new__(cls, name, bases, namespace):

        # collect all fields
        collected_fields = []
        for name, attr in namespace.items():
            if issubclass(attr, Field):
                # set the field name
                if attr.name is None:
                    attr.name = name
                collected_fields.append(attr)
        
        # cleanup namespace
        for field in collected_fields:
            namespace.pop(field.name)

        # adding 'collected_fields' attribute
        namespace.update({
            "collected_fields": collected_fields
        })

        return super().__new__(cls, name, bases, namespace)


class AdminView(metaclass=AdminViewMeta):
    class Meta:
        model = None # SQLA model class


def render_index(request):
    pass
