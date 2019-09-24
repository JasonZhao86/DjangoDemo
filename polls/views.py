from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.translation import ugettext as _
import csv
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
# Create your views here.


def auth_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            next = request.GET.get('next')
            if next and next.startswith('/'):
                return redirect(next)
            else:
                return redirect('/')
        else:
            return HttpResponse(_('Authentication Failed'))
    return render(request, 'polls/auth_login.html')

def auth_logout(request):
    logout(request)
    return HttpResponse(_("Logout Successful"))


"""
def index(request):
    if request.user.is_authenticated:
        print("User {} had been authenticated.".format(request.user.username))
        query_set = Question.objects.all().order_by("-pub_date")[:5]
        return render(request, "polls/lastest_five_books.html", {"query_set": query_set})
    else:
        print(request.user)
        return redirect('{}?next={}'.format(settings.LOGIN_URL, request.path))
"""


"""
@login_required(redirect_field_name="next", login_url=settings.LOGIN_URL)
def index(request):
    query_set = Question.objects.all().order_by("-pub_date")[:5]
    return render(request, "polls/lastest_five_books.html", {"query_set": query_set})
"""


class LoginRequiredMixin(TemplateView):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name="next", login_url=settings.LOGIN_URL)


class Index(LoginRequiredMixin):
    template_name = "polls/lastest_five_books.html"

    def get_context_data(self, **kwargs):
        query_set = Question.objects.all().order_by("-pub_date")[:5]
        kwargs = super(Index, self).get_context_data(**kwargs)
        kwargs.update({"query_set": query_set})
        return kwargs



"""
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
"""



def question_choice(request, question_id):
    return HttpResponse('Your are looking at choice of question {}'.format(question_id))


"""
@permission_required('polls.can_vote', login_url=settings.LOGIN_URL)
def voting(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        selected_id = request.POST.get("choice", 0)
        try:
            choice = question.choice_set.get(pk=selected_id)
        except Choice.DoesNotExist:
            return render(
                request,
                "polls/detail.html",
                {
                    "question": question,
                    "error_message": "Your choice is not valid",
                }
            )
        else:
            choice.voting += 1
            choice.save()
            return HttpResponseRedirect(reverse("polls:result", args=(question_id)))
"""


class Voting(TemplateView):
    template_name = "polls/detail.html"

    @method_decorator(permission_required('polls.can_vote', login_url=settings.LOGIN_URL))
    def dispatch(self, request, *args, **kwargs):
        return super(Voting, self).dispatch(request, *args, **kwargs)

    def post(self, request, question_id):
        context = self.get_context_data(question_id)
        selected_id = request.POST.get("choice", 0)
        try:
            question = context.get("question")
            choice = question.choice_set.get(pk=selected_id)
        except Choice.DoesNotExist:
            context.update({"error_message": "Your choice is not valid"})
            return self.render_to_response(context)
        else:
            choice.voting += 1
            choice.save()
            return HttpResponseRedirect(reverse("polls:result", args=(question_id,)))

    def get_context_data(self, question_id, **kwargs):
        question = get_object_or_404(Question, pk=question_id)
        kwargs = super(Voting, self).get_context_data(**kwargs)
        kwargs.update({"question": question})
        return kwargs


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/result.html", {"question": question})


def send_email(request):
    if request.method == "POST":
        subject = request.POST.get("subject", '')
        message = request.POST.get("message", '')
        from_email = request.POST.get("from_email", '')
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ["zhao13164113074@163.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return HttpResponseRedirect(reverse("polls:index", args=()))
        else:
            return HttpResponse("Make sure all fields are entered and valid")
    elif request.method == "GET":
        return render(request, "polls/email.html")


def download_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename='test.csv'"
    writer = csv.writer(response)
    writer.writerow(["Name", "Gender", "Age", "Province", "City"])
    writer.writerow(["赵宣", "男", "29", "湖北", "武汉"])
    writer.writerow(["金晶", "女", "27", "湖北", "武汉"])
    return response


def download_file(request):
    with open("d:/3.3Django-Template.pdf", "rb") as f:
        response = HttpResponse(f, "Content-Type: application/pdf")
        response["Content-Disposition"] = "attachment; filename=Django-Template.pdf"
    return response


def upload_file(request):
    if request.method == "POST":
        up_file = request.FILES.get("file", None)
        if up_file:
            with open("d:/{}".format(up_file), "wb") as f:
                f.write(up_file.read())
            return HttpResponse("Upload Finished.")
        else:
            return HttpResponse("[ ERROR ]: No File Found.")
    else:
        return render(request, "polls/upload_file.html")