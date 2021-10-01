from django.shortcuts import render, redirect


def home(request):
    return render(request, "home/home.html", {"title": "Home"})


def certification(request):
    return render(
        request,
        "home/certification.html",
        {
            "title": "Certification",
            "imgBx": "card__imgBx",
            "input": "card__radio",
        },
    )
