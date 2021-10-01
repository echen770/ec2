from django.shortcuts import render, redirect
from .forms import MessageForm
from django.contrib import messages
from .models import Profile


def home(request):
    qs = Profile.objects.all()
    return render(request, "home/home.html", {"title": "Home", "profile": qs})


def certification(request):
    return render(
        request,
        "home/certification.html",
        {
            "title": "Certification",
            "imgBx": "mobile__imgBx",
            "input": "card__radio",
        },
    )


def contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your message has been received.")
            return redirect("home")
    else:
        form = MessageForm()
    return render(
        request,
        "home/contact.html",
        {
            "title": "Contact",
            "imgBx": "mobile__imgBx",
            "input": "card__radio",
            "form": MessageForm,
        },
    )
