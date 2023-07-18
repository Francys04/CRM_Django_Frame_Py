from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
import datetime
# context
from .models import Lead, Agent, Category
# forms
from .forms import LeadForm, LeadModelForm
from django.views import generic
from agents.mixins import OrganisorAndLoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.contrib.auth.forms import UserCreationForm

# CRUD + L - create, retrive, update, delete, List
class SignupView(generic.CreateView):
    template_name="registration/signup.html"
    form_class = UserCreationForm
    
    def get_success_url(self) -> str:
        return reverse('login')


# for dashboard
class DashboardView(OrganisorAndLoginRequiredMixin, generic.TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)

        user = self.request.user

        # How many leads we have in total
        total_lead_count = Lead.objects.filter(organisation=user.userprofile).count()

        # How many new leads in the last 30 days
        thirty_days_ago = datetime.date.today() - datetime.timedelta(days=30)

        total_in_past30 = Lead.objects.filter(
            organisation=user.userprofile,
            date_added__gte=thirty_days_ago
        ).count()

        # How many converted leads in the last 30 days
        converted_category = Category.objects.get(name="Converted")
        converted_in_past30 = Lead.objects.filter(
            organisation=user.userprofile,
            category=converted_category,
            converted_date__gte=thirty_days_ago
        ).count()

        context.update({
            "total_lead_count": total_lead_count,
            "total_in_past30": total_in_past30,
            "converted_in_past30": converted_in_past30
        })
        return context


# for leading view
def landing_page(request):
    return render(request, 'landing.html')



# Create your views here.
def home_page(request):
    # return HttpResponse("Hello world")
    # put in url path alexCRM
    
    # add templates, cretae html in templates/leads folder
    # context
    # context = {
    #     "name":"Joe",
    #     "age":32
    # }
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads\home_page.html", context)


# lead detail for view
def lead_detail(request, pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_list.html", context)


# forms
def lead_create(request):
    # print(request.POST) #print out data of user create data after enter data in localhost/leads/create/
    
    # check if the method post
    form = LeadModelForm()
    if request.method == "POST":
        print("Receiving a post request")
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)


# return for the previous cmd, form.save() cmd
            # print("Form is valid")
            # print(form.cleaned_data)
            
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # age = form.cleaned_data['age']
            # agent = form.cleaned_data['agent']
            # # create new lead
            # Lead.objects.create(
            #     first_name=first_name,
            #     last_name=last_name,
            #     age=age,
            #     agent=agent,
            # )
            # print("Lead has been craeted")


# delete leads
def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form,
        "lead": lead
    }
    return render(request, "leads/lead_update.html", context)


# # lead update
# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             # update new lead
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             return redirect('/leads')
#     context = {
#         "lead": lead,
#         "form": form
#     }
#     return render(request, "leads/lead_update.html", context)


# first model create for view

# def lead_create(request):
    # form = LeadForm()
    # if request.method == "POST":
    #     form = LeadForm(request.POST)
    #     if form.is_valid():
    #         first_name = form.cleaned_data['first_name']
    #         last_name = form.cleaned_data['last_name']
    #         age = form.cleaned_data['age']
    #         agent = Agent.objects.first()
    #         # create new lead
    #         Lead.objects.create(
    #             first_name=first_name,
    #             last_name=last_name,
    #             age=age,
    #             agent=agent,
    #         )
    #         return redirect('/leads')
    # context = {
    #     "form": form
    # }
#     return render(request, "leads/lead_create.html", context)