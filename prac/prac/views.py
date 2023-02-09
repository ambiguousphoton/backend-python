from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data = {
        'title' : 'jai shree ram ! jai bhole baba page',
        'bdata' : 'aryavrat ki jai!',
        'clist' : ['shubhi', "surayanshi",'vedanshi',"vikranta","snehleen kaur", "shivani","shreyas","shreyansh","himashi",'ankit','manrajeshwari','samrat'],
        'student_details': [
            {'name':'Ram', 'phone':984394934},
            {'name':'Krishna', 'phone':324234344}
        ],
        'numbers':[10,20,30,40,50]
    }
    return render(request, "index.html",data)


def about_us(request):
    return HttpResponse("Jai shree ram")

def jai_ho(request):
    return HttpResponse("<h1>hari om hari om !!!!!</h1><br><h2>jai ho</h2>")

def diffpages(request, numbering):
    return HttpResponse(numbering)