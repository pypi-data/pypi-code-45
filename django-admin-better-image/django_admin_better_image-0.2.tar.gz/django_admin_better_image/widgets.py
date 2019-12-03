from django import forms
from django.template import loader
from django.utils.safestring import mark_safe


class BetterImageWidget(forms.FileInput):
    def render(self, name, value, attrs=None, renderer=None):
        template = loader.get_template('django_admin_better_image/image.html')
        context = {'name': name, 'value': getattr(value, 'url', None)}
        return mark_safe(template.render(context))

    def value_from_datadict(self, data, files, name):
        return files.get(name)
