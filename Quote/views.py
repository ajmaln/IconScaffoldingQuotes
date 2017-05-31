from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.views.generic.base import View
from Quote.forms import TermsForm
from Quote.models import Terms
from .forms import QuoteForm, ItemForm
from .models import Quote, Item
from django.shortcuts import reverse, render


class Index(ListView):
    queryset = Quote.objects.all().order_by('-id')[:10]
    template_name = 'Quote/quotes.html'


class QuoteView(DetailView):
    template_name = 'Quote/quote.html'
    model = Quote

    def get_context_data(self, **kwargs):
        context = super(QuoteView, self).get_context_data()
        context['terms'] = Terms.objects.get(id=1)
        return context


class QuoteCreate(CreateView):
    form_class = QuoteForm
    model = Quote
    template_name = 'Quote/create.html'


class QuoteCreta(View):
    form_class = QuoteForm
    form_class1 = TermsForm
    template_name = 'Quote/create.html'
    terms = Terms.objects.get(id=1)

    def get_success_url(self, pk):
        return reverse('add_item', kwargs={'pk': pk})

    def get(self, request):
        form1 = self.form_class(None)
        form2 = self.form_class1(None)
        return render(request, self.template_name, {'form1': form1, 'form2': form2})

    def post(self, request):
        form1 = self.form_class(request.POST)
        form2 = self.form_class1(request.POST)

        if form1.is_valid():
            obj = form1.save()
            if form2.is_valid():
                self.terms.terms = form2.cleaned_data['terms']
                print(self.terms.terms)
                self.terms.save()
                return HttpResponseRedirect(self.get_success_url(obj.id))
        return render(request, self.template_name, {'form1': form1, 'form2': form2, 'terms': self.terms})


class AddItem(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'Quote/add_items.html'

    def get_context_data(self, **kwargs):
        context = super(AddItem, self).get_context_data(**kwargs)
        context['quote'] = Quote.objects.get(id=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        quote = Quote.objects.get(id=self.kwargs['pk'])
        self.object.quote = quote
        return super(AddItem, self).form_valid(form)

    def get_success_url(self):
        return reverse('add_item', kwargs={'pk': self.object.quote.id})


class ItemDelete(DeleteView):
    model = Item

    def get_object(self, queryset=None):
        return self.model.objects.get(id=self.kwargs['id'])

    def get_success_url(self):
        return reverse('add_item', kwargs={'pk': self.object.quote.id})
