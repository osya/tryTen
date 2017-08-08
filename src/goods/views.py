from django.core.urlresolvers import reverse_lazy
from django.views import generic
from braces import views

from .models import Category, Good
from .forms import GoodForm


class PageCatsMixin(object):
    def get_context_data(self, **kwargs):
        context = super(PageCatsMixin, self).get_context_data(**kwargs)
        context['cats'] = Category.objects.order_by('name')
        context['page'] = self.request.GET.get('page')
        return context


class GoodList(PageCatsMixin, generic.ListView):
    model = Good
    paginate_by = 10
    cat_id = None

    def get_queryset(self):
        queryset = super(GoodList, self).get_queryset()
        self.cat_id = self.request.GET.get('cat_id') or Category.objects.first().id
        return queryset.filter(category=self.cat_id)

    def get_context_data(self, **kwargs):
        context = super(GoodList, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.cat_id)
        return context


class GoodDetail(PageCatsMixin, generic.DetailView):
    model = Good

    def get_context_data(self, **kwargs):
        context = super(GoodDetail, self).get_context_data(**kwargs)
        context['category'] = self.object.category
        return context


class GoodCreate(views.SetHeadlineMixin, PageCatsMixin, generic.CreateView):
    model = Good
    headline = 'Add Good'
    form_class = GoodForm

    def get(self, request, *args, **kwargs):
        self.initial['category'] = self.request.GET.get('cat_id') or Category.objects.first().id
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
        context['category'] = Category.objects.get(pk=self.request.GET.get('cat_id') or Category.objects.first().id)
        return context


class GoodUpdate(views.SetHeadlineMixin, PageCatsMixin, generic.UpdateView):
    model = Good
    headline = 'Update Good'
    form_class = GoodForm

    def get_context_data(self):
        context = super(GoodUpdate, self).get_context_data()
        context['category'] = self.object.category
        return context


class GoodDelete(generic.DeleteView):
    model = Good
    success_url = reverse_lazy('goods:list')
