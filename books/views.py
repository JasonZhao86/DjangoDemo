from django.shortcuts import render, get_object_or_404
from .models import Publisher
from django.shortcuts import redirect
from .forms import PubliserForm, ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, View, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse


class PublisherAdd(CreateView):
    model = Publisher
    # fields = ("name", "address", "city", "state_province", "country", "website")
    initial = {"name": "长江出版社", "country": "中国"}
    form_class = PubliserForm
    template_name = "books/publisher_add.html"
    # success_url = reverse_lazy("books:publisher_detail", kwargs={'pk': self.object.id})

    def form_valid(self, form):
        publisher = form.save()
        self.object = publisher
        self.success_url = reverse_lazy("books:publisher_detail", kwargs={'pk': self.object.id})
        return super(PublisherAdd, self).form_valid(form)

    def form_invalid(self, form):
        return super(PublisherAdd, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(PublisherAdd, self).get_context_data(**kwargs)
        context.update({"publisher": self.object})
        return context



class PublisherUpdate(UpdateView):
    model = Publisher
    form_class = PubliserForm
    # fields = '__all__'
    template_name = "books/publisher_add.html"

    def form_valid(self, form):
        publisher_save = form.save()
        self.object = publisher_save
        self.success_url = reverse("books:publisher_detail", kwargs={"pk": publisher_save.id})
        return super(PublisherUpdate, self).form_valid(form)

    def form_invalid(self, form):
        return super(PublisherUpdate, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(PublisherUpdate, self).get_context_data(**kwargs)
        context.update({"publisher": self.object})
        return context



class PublisherDelete(DeleteView):
    model = Publisher
    success_url = reverse_lazy("books:publisher_list")
    template_name = "books/publisher_confirm_delete.html"



class PublisherDetail(DetailView):
    model = Publisher
    context_object_name = "publisher"

    # def get_context_data(self, publisher_id, **kwargs):
    #     context = super(PublisherDetail, self).get_context_data(**kwargs)
    #     publisher = get_object_or_404(Publisher, pk=publisher_id)
    #     context.update({"publisher": publisher})
    #     return context


class ContactUs(FormView):
    template_name = "books/email.html"
    form_class = ContactForm
    # success_url = '/books/add'
    success_url = reverse_lazy("books:publisher_add")


    def form_valid(self, form):
        subject = form.cleaned_data["subject"]
        message = form.cleaned_data["message"]
        sender = form.cleaned_data["sender"]
        cc_myself = form.cleaned_data["cc_myself"]
        recipients = ["zhaoxuan@beyondsoft.com"]
        if cc_myself:
            recipients.append(sender)
        send_mail(subject, message, sender, recipients)
        return super(ContactUs, self).form_valid(form)



class AboutView(TemplateView):
    template_name = "books/about.html"



class GreetingView(View):
    greeting = 'Nice Day'
    def get(self, request):
        return HttpResponse(self.greeting)


class MorningGreetingView(GreetingView):
    greeting = 'Nice Morning Day'


class PubliserList(ListView):
    model = Publisher
    queryset = Publisher.objects.all()
    # context_object_name = "publishers"
    # template_name = "books/publisher_list.html"

    # def get_queryset(self):
    #     return Publisher.objects.filter(pk=2)


"""
def publisher_add(request):
    if request.method == 'POST':
        name = request.POST.get("name", '')
        address = request.POST.get("address", '')
        city = request.POST.get("city", '')
        state_province = request.POST.get('state_province', '')
        country = request.POST.get('country', '')
        website = request.POST.get('website', '')

        error_messages = []
        if not name:
            error_messages.append("Name is required")
        elif len(name) > 30:
            error_messages.append("Name should be short than 30")
        if not address:
            error_messages.append("Address is required")
        if error_messages:
            return render(request, "books/publisher_add.html", {"error_messages": error_messages})

        publisher = Publisher(
            name=name,
            address=address,
            city=city,
            state_province=state_province,
            country=country,
            website=website,
        )
        publisher.save()
        return redirect("books:publisher_detail", publisher_id=publisher.id)

    else:
        return render(request, 'books/publisher_add.html')
"""


"""
def publisher_add(request):
    if request.method == "POST":
        form = PubliserForm(request.POST)
        if form.is_valid():
            publisher = Publisher(
                name=form.cleaned_data["name"],
                address=form.cleaned_data["address"],
                city=form.cleaned_data["city"],
                state_province=form.cleaned_data["state_province"],
                country=form.cleaned_data["country"],
                website=form.cleaned_data["website"],
            )
            publisher.save()
            return redirect("books:publisher_detail", publisher_id=publisher.id)
        else:
            return render(request, "books/publisher_add.html", {"form": form})
    else:
        form = PubliserForm()
        return render(request, 'books/publisher_add.html', {"form": form})
"""


"""
def publisher_list(request):
    publisers = Publisher.objects.all()
    return render(request, 'books/publisher_list.html', {"publisers": publisers})
"""


"""
def publisher_detail(request, publisher_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    return render(request, "books/publisher_detail.html", {"publisher": publisher})
"""


"""
def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["sender"]
            cc_myself = form.cleaned_data["cc_myself"]
            recipients = ["zhaoxuan@beyondsoft.com"]
            if cc_myself:
                recipients.append(sender)
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect(reverse("books:publisher_add"))
        else:
            return render(request, "books/email.html", {"form": form})
    else:
        form = ContactForm()
        return render(request, "books/email.html", {"form": form})
"""


"""
def publisher_add(request):
    if request.method == "POST":
        form = PubliserForm(request.POST)
        if form.is_valid():
            publisher = form.save()
            return redirect("books:publisher_list")
    else:
        form = PubliserForm(initial={"name": "长江出版社", "country": "中国"})
    return render(request, "books/publisher_add.html", {"form": form})
"""


"""
def publisher_update(request, publisher_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    if request.method == "POST":
        form = PubliserForm(request.POST, instance=publisher)
        if form.is_valid():
            publisher_save = form.save()
            return redirect("books:publisher_detail", pk=publisher_save.id)
    form = PubliserForm(instance=publisher)
    return render(request, "books/publisher_add.html", {"form": form})
"""