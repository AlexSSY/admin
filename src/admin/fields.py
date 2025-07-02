from dataclasses import dataclass, field, asdict

from typing import Optional
from .templating import render_to_string


@dataclass
class Field:
    name: Optional[str] = None
    type: str = "text"
    validators: list = field(default_factory=list)
    normalizators: list = field(default_factory=list)
    abstract: bool = False
    list_template: str = ""
    input_template: str = ""
    label_template: str = ""
    detail_template: str = ""

    def parse_value(self, obj):
        """
        Returns value from sqla-model

        :param obj: SQLA model instance
        """
        return getattr(obj, self.name, None)


def render_field_label(request, field):
    return render_to_string(request, field.label_template, asdict(field))
