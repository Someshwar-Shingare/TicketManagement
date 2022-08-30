

# Create your views here.
from cmath import log
from xml.dom.minidom import Identified
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Ticket
from .forms import TicketForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def user_registration_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name = 'ticketapp/user_reg.html'
    context = {'form': form}
    return render(request, template_name, context)


def user_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            tickets = Ticket.objects.all()
            if user.is_superuser:
                template_name = 'ticketapp/admin_home.html'
                context = {'tickets': tickets}
                return render(request, template_name, context)
            return redirect('home')
        return redirect('login')
    template_name = 'ticketapp/user_login.html'
    context = {}
    return render(request, template_name, context)


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def ticket_generation_view(request):
    tiks = Ticket.objects.all()
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    template_name = 'ticketapp/home.html'
    context = {'form': form, 'tiks': tiks}
    return render(request, template_name, context)


@login_required(login_url='login')
def admin_ticket_resolve_view(request):
    tiks = Ticket.objects.all()
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
    template_name = 'ticketapp/admin_home.html'
    context = {'form': form, 'tiks': tiks}
    return render(request, template_name, context)


@login_required(login_url='login')
def admin_view(request):
    tickets = Ticket.objects.all()
    template_name = 'ticketapp/admin_home.html'
    context = {'tickets': tickets}
    return render(request, template_name, context)


@login_required(login_url='login')
def user_update_view(request, id):
    tik = Ticket.objects.get(id=id)
    form = TicketForm(instance=tik)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=tik)
        if form.is_valid():
            form.save()
            return redirect('home')
    template_name = 'ticketapp/home.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='login')
def user_delete_view(request, id):
    tik = Ticket.objects.get(id=id)
    tik.delete()
    return redirect('home')


@login_required(login_url='login')
def admin_update_view(request, id):
    tik = Ticket.objects.get(id=id)
    form = TicketForm(instance=tik)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=tik)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
    template_name = 'ticketapp/admin_update.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='login')
def admin_delete_view(request, id):
    tik = Ticket.objects.get(id=id)
    tik.delete()
    return redirect('admin_home')


