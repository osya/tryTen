from django.views import generic
from braces import views

from .models import Category, Good
from .forms import GoodForm


class PageCategory2ContextMixin(generic.base.ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(PageCategory2ContextMixin, self).get_context_data(**kwargs)
        context['cats'] = Category.objects.order_by('name')
        cat_id = self.kwargs.get('cat_id')
        context['category'] = Category.objects.get(pk=cat_id) if cat_id else Category.objects.first()
        context['page'] = self.request.GET.get('page', 1)
        return context


class GoodList(PageCategory2ContextMixin, generic.ListView):
    model = Good
    paginate_by = 10

    def get_queryset(self):
        queryset = super(GoodList, self).get_queryset()
        cat_id = self.kwargs.get('cat_id') or Category.objects.first().id
        return queryset.filter(category=cat_id)


class GoodDetail(PageCategory2ContextMixin, generic.DetailView):
    model = Good


class GoodCreate(views.SetHeadlineMixin, generic.CreateView):
    model = Good
    headline = 'Add Good'
    form_class = GoodForm

    def get(self, request, *args, **kwargs):
        self.initial['category'] = self.kwargs.get('pk') or Category.objects.first().id
        return super(GoodCreate, self).get(request, *args, **kwargs)

    def get_success_url(self):
        url = super(GoodCreate, self).get_success_url()
        page = self.request.GET.get('page')
        if page:
            from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse
            url_parts = list(urlparse(url))
            query = dict(parse_qsl(url_parts[4]))
            query['page'] = page
            url_parts[4] = urlencode(query)
            url = urlunparse(url_parts)
        return url

    def get_context_data(self):
        context = super(GoodCreate, self).get_context_data()
        cat_id = self.kwargs.get('cat_id')
        context['category'] = Category.objects.get(pk=cat_id) if cat_id else Category.objects.first()
        context['page'] = self.request.GET.get('page', 1)
        return context
