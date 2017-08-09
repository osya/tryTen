from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.base import ContextMixin, View
from braces import views
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

from .models import Category, Good
from .forms import GoodForm


class PageCatsMixin(ContextMixin, View):
    def get_context_data(self, **kwargs):
        context = super(PageCatsMixin, self).get_context_data(**kwargs)
        context['cats'] = Category.objects.order_by('name')
        context['page'] = int(self.request.GET.get('page', 1))
        return context


class SuccessUrlMixin(View):
    cat_id = None

    def get_success_url(self):
        url = reverse('goods:list')
        url_parts = list(urlparse(url))
        query = dict(parse_qsl(url_parts[4]))
        cat_id = self.cat_id
        if cat_id:
            query['cat_id'] = cat_id
        page = self.request.GET.get('page')
        if page and int(page) > 1:
            query['page'] = page
        url_parts[4] = urlencode(query)
        return urlunparse(url_parts)


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


class GoodCreate(views.SetHeadlineMixin, views.LoginRequiredMixin, PageCatsMixin, SuccessUrlMixin, generic.CreateView):
    model = Good
    headline = 'Add Good :: '
    form_class = GoodForm

    @property
    def cat_id(self):
        return self.request.GET.get('cat_id') or Category.objects.first().id

    def get(self, request, *args, **kwargs):
        self.initial['category'] = self.cat_id
        return super(GoodCreate, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GoodCreate, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.request.GET.get('cat_id') or Category.objects.first().id)
        return context


class GoodUpdate(views.SetHeadlineMixin, views.LoginRequiredMixin, PageCatsMixin, SuccessUrlMixin, generic.UpdateView):
    model = Good
    headline = 'Update Good :: '
    form_class = GoodForm

    @property
    def cat_id(self):
        return self.object.category.id

    def get_context_data(self, **kwargs):
        context = super(GoodUpdate, self).get_context_data(**kwargs)
        context['category'] = self.object.category
        return context


class GoodDelete(views.LoginRequiredMixin, SuccessUrlMixin, generic.DeleteView):
    model = Good

    @property
    def cat_id(self):
        return self.object.category.id

    def get_context_data(self, **kwargs):
        context = super(GoodDelete, self).get_context_data(**kwargs)
        context['category'] = self.object.category
        return context
