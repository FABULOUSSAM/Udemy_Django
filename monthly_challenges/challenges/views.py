from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
#from django.template.loader import render_to_string

# Create your views here.
month_data = {
    "january": "For January",
    "february": "For February",
    "march": "For March",
    "april": "For April",
    "may": None
}


def index(request):
    # month_val=""
    months = list(month_data.keys())
    # for month in  months:
    #    capitalizeval=month.capitalize()
    #    redirect_val=reverse("month-challenge",args=[month])
    #    month_val+=f"<li><h2><a href=\"{redirect_val}\">{capitalizeval}</a></h2></li>"
    # month_final=f"<ul>{month_val}</ul>"
    # return HttpResponse(month_final)
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenges_str(request, month):
    try:
        value = month_data[month]
        # response_data=f"<h1>{value}</h1>"
        # response_data=render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {
            "text": value,
            "month_name": month.capitalize()
        })
    except:
        return HttpResponseNotFound("<h1>Not in List</h1>")


def monthly_challenges_int(request, month):
    months = list(month_data.keys())
    if month > len(months):
        return HttpResponseNotFound("NUMBER NOT FOUND IN LIST")
    else:
        val = months[month-1]
        val_redirect = reverse("month-challenge", args=[val])
        return HttpResponseRedirect(val_redirect)
