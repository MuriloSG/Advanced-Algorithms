from django.views.generic import FormView, View, ListView
from django.http import JsonResponse
from django.core.cache import cache
from .models import Product
from .forms import ProductSearchForm
from .trie import Trie


class ProductListView(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'page_obj'
    paginate_by = 30
    ordering = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query', '')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset.order_by('-price')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductSearchForm(initial={'query': self.request.GET.get('query', '')})
        return context


class ProductAutocompleteView(View):
    def get(self, request, *args, **kwargs):
        prefix = request.GET.get('query', '')
        trie = cache.get('product_trie')
        print(trie, "cache")
        if not trie:
            trie = Trie()
            for product in Product.objects.all():
                trie.insert(product.name) 
            cache.set('product_trie', trie, 60 * 5)
        suggestions = trie.starts_with(prefix) if prefix else []
        return JsonResponse({'suggestions': suggestions})
