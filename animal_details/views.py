
from django.contrib.auth import authenticate, login,logout
from django.views import generic
from .models import Animal,Medicine,Accounts,Organisation_grants,Staff,Tourists
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View

from .forms import UserForm




def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                animal=Animal.objects.all()
               
                return render(request, 'animal_details/index1.html', {'animals': animal})
    context = {
        "form": form,
    }
    return render(request, 'animal_details/register.html', context)


def home(request):
    return render(request,'animal_details/home.html')




def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                animal=Animal.objects.all()
               
                return render(request, 'animal_details/index1.html', {'animals': animal})
               
            else:
                return render(request, 'animal_details/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'animal_details/login.html', {'error_message': 'Invalid login'})
    return render(request, 'animal_details/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'animal_details/login.html', context)






class IndexView(generic.ListView):
    template_name = 'animal_details/index.html'

    def get_queryset(self):
        return Animal.objects.all()

class DetailView(generic.DetailView):
    model = Animal
    template_name = 'animal_details/detail.html'
#-----------------------------------------------------------------------------------------------------------------------

class AnimalCreate(CreateView):
    model = Animal
    fields = ['id', 'Animal_species', 'Animal_count', 'Animal_type', 'Scientific_name', 'Country', 'Animal_feed','Feed_cost']

class AnimalUpdate(UpdateView):
    model = Animal
    fields = ['id', 'Animal_species', 'Animal_count', 'Animal_type', 'Scientific_name', 'Country', 'Animal_feed','Feed_cost']

class AnimalDelete(DeleteView):
    model =Animal
    success_url = reverse_lazy('animal_details:index')

class MedicineDetail(generic.ListView):
    model = Medicine
    template_name = 'animal_details/med.html'

class MedicineCreate(CreateView):
    model = Medicine
    fields = ['Animal_id', 'Medicine_name', 'Medicine_cost']

class MedicineUpdate(UpdateView):
    model = Medicine
    fields = ['Animal_id', 'Medicine_name', 'Medicine_cost']

#-----------------------------------------------------------------------------------------------------------------------

class AccountCreate(CreateView):
    model=Accounts
    fields=['Income','Expenditure']

class AccountUpdate(UpdateView):
    model=Accounts
    fields=['Income','Expenditure']

class AccountDetail(generic.ListView):
    model=Accounts
    template_name='animal_details/acc.html'

    def get_queryset(self):
        return Accounts.objects.all()

class GrantsCreate(CreateView):
    model=Organisation_grants
    fields=['id','Organisation_name','Organisation_phno','Address','Amount']

class GrantsUpdate(UpdateView):
    model=Organisation_grants
    fields=['id','Organisation_name','Organisation_phno','Address','Amount']

class GrantsDetail(generic.ListView):
    model=Organisation_grants
    template_name='animal_details/grant.html'
#-----------------------------------------------------------------------------------------------------------------------
#staff
class StaffCreate(CreateView):
    model = Staff
    fields = ['id','Staff_name','Designation','Salary']
class StaffUpdate(UpdateView):
    model = Staff
    fields = ['id','Staff_name','Designation','Salary']

class StaffDetail(generic.ListView):
    model =Staff
    template_name='animal_details/staff.html'

    def get_queryset(self):
        return Staff.objects.all()

class StaffDelete(DeleteView):
    model=Staff
    success_url = reverse_lazy('animal_details:staff_detail')




#tourist
class TouristCreate(CreateView):
    model = Tourists
    fields = ['id','Tourists_name','Donation','GuideName','Phone_number']
class TouristUpdate(UpdateView):
    model = Tourists
    fields = ['id','Tourists_name','Donation','GuideName','Phone_number']
class TouristDelete(DeleteView):
    model = Tourists
    success_url = reverse_lazy('animal_details:index')
class TouristDetail(generic.ListView):
    model = Tourists
    template_name='animal_details/tourists.html'

