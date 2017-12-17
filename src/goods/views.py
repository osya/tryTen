from braces.views import SetHeadlineMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.views.generic.base import ContextMixin, View
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from goods.forms import GoodForm
from goods.models import Category, Good
from goods.serializers import CategorySerializer, GoodSerializer


class Cats2ContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(Cats2ContextMixin, self).get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        return context


class Cat2ContextMixin1(Cats2ContextMixin, View):
    object = None

    def get_context_data(self, **kwargs):
        context = super(Cat2ContextMixin1, self).get_context_data(**kwargs)
        context['category'] = self.object.category
        return context


class Cat2ContextMixin2(Cats2ContextMixin, View):
    def get_context_data(self, **kwargs):
        context = super(Cat2ContextMixin2, self).get_context_data(**kwargs)
        cat_id = (self.cat_id if hasattr(self, 'cat_id') else None) or self.request.GET.get('cat_id')
        if cat_id:
            context['category'] = Category.objects.get(pk=cat_id)
        return context


class SuccessUrlMixin(View):
    def get_success_url(self):
        url = reverse('goods:goods:list')
        query = self.request.GET.urlencode()
        if query:
            url = f'{url}?{query}'
        return url


class GoodList(Cat2ContextMixin2, ListView):
    paginate_by = 10

    def get_queryset(self):
        return Good.objects.list(self.request.GET)


class GoodListApi(ListCreateAPIView):
    serializer_class = GoodSerializer

    def get_queryset(self):
        return Good.objects.list(self.request.GET)


class GoodDetail(Cat2ContextMixin1, DetailView):
    model = Good


class GoodDetailApi(RetrieveUpdateDestroyAPIView):
    serializer_class = GoodSerializer

    def get_queryset(self):
        return Good.objects.list(self.request.GET)


class GoodCreate(
        LoginRequiredMixin,
        SetHeadlineMixin,
        SuccessUrlMixin,
        Cat2ContextMixin2,
        CreateView):
    model = Good
    headline = 'Add good :: '
    form_class = GoodForm

    def get_initial(self):
        initial = super(GoodCreate, self).get_initial()
        cat_id = self.request.GET.get('cat_id')
        if cat_id:
            initial['category'] = cat_id
        if self.request.GET.get('tags'):
            initial['tags'] = self.request.GET.get('tags')
        return initial


class GoodUpdate(
        LoginRequiredMixin,
        SetHeadlineMixin,
        SuccessUrlMixin,
        Cat2ContextMixin1,
        UpdateView):
    model = Good
    form_class = GoodForm
    headline = 'Update good '


class GoodDelete(LoginRequiredMixin, SuccessUrlMixin, Cat2ContextMixin1, DeleteView):
    model = Good


class CategoryListApi(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetailApi(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

# TODO: Write tests for the API calls
