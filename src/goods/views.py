from braces import views
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.base import View, ContextMixin

from .forms import GoodForm
from .models import Good, Category


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
        url = reverse('goods:list')
        query = self.request.GET.urlencode()
        if query:
            url = f'{url}?{query}'
        return url


class GoodList(Cat2ContextMixin2, generic.ListView):
    model = Good
    paginate_by = 10
    cat_id = None

    def get_queryset(self):
        queryset = super(GoodList, self).get_queryset()
        self.cat_id = self.request.GET.get('cat_id')
        if self.cat_id:
            queryset = queryset.filter(category__id=self.cat_id).distinct()
        tags = self.request.GET.get('tags')
        if tags:
            tags = tags.split(',')
            queryset = queryset.filter(tags__name__in=tags).distinct()
        return queryset


class GoodDetail(Cat2ContextMixin1, generic.DetailView):
    model = Good


class GoodCreate(
        views.SetHeadlineMixin,
        views.LoginRequiredMixin,
        SuccessUrlMixin,
        Cat2ContextMixin2,
        generic.CreateView):
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
        views.SetHeadlineMixin,
        views.LoginRequiredMixin,
        SuccessUrlMixin,
        Cat2ContextMixin1,
        generic.UpdateView):
    model = Good
    form_class = GoodForm
    headline = 'Update good '


class GoodDelete(views.LoginRequiredMixin, SuccessUrlMixin, Cat2ContextMixin1, generic.DeleteView):
    model = Good