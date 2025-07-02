class Admin:
    def __init__(self, **context_kwargs):
        self.context = context_kwargs if context_kwargs else {}

    def extend_context(self, context):
        self.context.update(context)