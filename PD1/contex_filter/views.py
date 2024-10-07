from django.shortcuts import render

# Create your views here.
def home(request):
    person = {
        "name" : "Khirul Islam",
        "age" : 22,
        "marks" : [70, 60, 86, 91, 56, 80],
        "friends": ["Karim", "Zoy", "Pial", "Nayeem", "Najmul"],
    }
    return render(request, 'index.html',person)