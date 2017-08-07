from django.views import generic

from .models import Category, Good


class CategoryMixin(generic.base.ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(CategoryMixin, self).get_context_data(**kwargs)
        cat_id = self.kwargs.get('cat_id')
        context['category'] = Category.objects.get(pk=cat_id) if cat_id else Category.objects.first()
        context['cats'] = Category.objects.all()
        return context


class GoodList(CategoryMixin, generic.ListView):
    model = Good
    paginate_by = 10

    def get_queryset(self):
        queryset = super(GoodList, self).get_queryset()
        cat_id = self.kwargs.get('cat_id') or Category.objects.first().id
        return queryset.filter(category=cat_id)


class GoodDetail(CategoryMixin, generic.DetailView):
    model = Good

    def get_context_data(self, **kwargs):
        context = super(GoodDetail, self).get_context_data(**kwargs)
        context['page'] = self.request.GET.get('page', 1)
        return context
