menu = [{'title': "My Shop", 'url_name': 'home'},
        {'title': "Shopping Cart", 'url_name': 'basket'},
        {'title': "Detail Information", 'url_name': 'product'},
        ]


class DataMixin:
    paginate_by = 5
    title_page = None
    cat_selected = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.cat_selected

    def get_mixin_context(self, context, **kwargs):
        context['cat_selected'] = None
        context.update(kwargs)
        return context