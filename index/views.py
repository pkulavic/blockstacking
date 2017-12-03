from django.shortcuts import render
from .forms import TotalOverhang

def home(request):
    #if form is submitted with data
    if request.method == "POST":
        print(request.POST)
        form = TotalOverhang(request.POST)
        #validate form
        if form.is_valid():
            #clean the form data
            l = form.cleaned_data['l']
            n = form.cleaned_data['n']
            #function that calculates total overhang
            def total_overhang(l, n):
                i = 1
                total = 0
                while i <= n:
                    total += l/(2*i)
                    print (i, total)
                    i += 1
                return total
            #calculate overhang with form data
            totaloverhang = total_overhang(l, n)

            context = {'totaloverhang': totaloverhang, 'l': l, 'n': n, 'TotalOverhang': TotalOverhang}

    else:
        context = {'TotalOverhang': TotalOverhang}

    template = 'index/home.html'
    return render(request, template, context)
