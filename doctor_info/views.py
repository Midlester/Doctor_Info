from django.contrib.auth import authenticate, login # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib.auth import logout # type: ignore
from django.shortcuts import render, redirect,get_object_or_404 # type: ignore
from .forms import DoctorInfoForm
from .models import DoctorInfo
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.core.paginator import Paginator # type: ignore

from .forms import DoctorInfoForm
from .models import DoctorInfo

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)  # Authenticate with raw password
        if user is not None:
            login(request, user)  # Log the user in
            return redirect("doctor_list")  # Redirect to the doctor list page after login
        else:
            return render(request, "doctor_info/login.html", {"error": "Invalid username or password"})

    return render(request, "doctor_info/login.html")

def register(request):
    from django.contrib.auth.forms import UserCreationForm # type: ignore
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user to the database
            return redirect("login")  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, "doctor_info/register.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("login")
def doctor_list(request):
    doctors = DoctorInfo.objects.all()
    # Filtering
    division = request.GET.get('division')
    district = request.GET.get('district')
    upazilla = request.GET.get('upazilla')
    union = request.GET.get('union')
    if division:
        doctors = doctors.filter(divisions=division)
    if district:
        doctors = doctors.filter(district=district)
    if upazilla:
        doctors = doctors.filter(upazilla=upazilla)
    if union:
        doctors = doctors.filter(union=union)
    # Unique values for dropdowns
    all_doctors = DoctorInfo.objects.all()
    divisions = all_doctors.values_list('divisions', flat=True).distinct()
    districts = all_doctors.values_list('district', flat=True).distinct()
    upazillas = all_doctors.values_list('upazilla', flat=True).distinct()
    unions = all_doctors.values_list('union', flat=True).distinct()
    paginator = Paginator(doctors, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = DoctorInfoForm()
    if request.method == "POST":
        form = DoctorInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorInfoForm()
    return render(request, 'doctor_info/doctor_list.html', {
        'page_obj': page_obj,
        'form': form,
        'divisions': divisions,
        'districts': districts,
        'upazillas': upazillas,
        'unions': unions,
    })

@login_required
def edit_doctor(request, doctor_id):
    doctor = get_object_or_404(DoctorInfo, id=doctor_id)
    if request.method == "POST":
        form = DoctorInfoForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorInfoForm(instance=doctor)
    return render(request, 'doctor_info/edit_doctor.html', {'form': form, 'doctor': doctor})

@login_required
def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(DoctorInfo, id=doctor_id)
    doctor.delete()
    return redirect('doctor_list')