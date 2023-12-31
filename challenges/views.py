from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january" : "Eat no meat for the entire month!",
    "february" : "Walk for at least 20 minutes every day.",
    "march" : "Read at least 2 books.",
    "april" : "Meditate 10 min every day.",
    "may" : "No sweets.",
    "june" : "Meal prep all lunches.",
    "july" : "Make one new connection a week.",
    "august" : "Write a blog every week.",
    "september" : "Take stairs all time.",
    "october" : "Write a letter to someone new every evening.",
    "november": "Cook a new recipe a week.",
    "december": None
}



# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        raise Http404()
