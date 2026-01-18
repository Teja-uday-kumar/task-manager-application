from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from .forms import TaskForm, RegisterForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()   # Create user ONLY (no auto login)

            messages.success(
                request,
                "Account created successfully. Please login."
            )
            return redirect('login')   # Redirect to login page
        else:
            messages.error(
                request,
                "Registration failed. Please check the details."
            )

    return render(request, 'tasks/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'tasks/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')


@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/dashboard.html', {'tasks': tasks})


@login_required
def add_task(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            messages.success(request, "Task added successfully!")
            return redirect('dashboard')
        else:
            messages.error(request, "Failed to add task.")

    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect('dashboard')
        else:
            messages.error(request, "Failed to update task.")

    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def delete_task(request, id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=id, user=request.user)
        task.delete()
        messages.success(request, "Task deleted successfully!")

    return redirect('dashboard')
