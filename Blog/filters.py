import django_filters

from Blog.models import Post


class PostFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='icontains', label='category')
    tags = django_filters.CharFilter(lookup_expr='icontains', label='tags')


    class Meta:
        model = Post
        fields = ['category', 'tags']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['category'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter category'})
        self.filters['tags'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter tag'})

