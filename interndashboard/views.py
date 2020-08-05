from django.shortcuts import render


def retail(request):
   return render(request, 'interndashboard/retail.html', {})


def marketing(request):
   return render(request, 'interndashboard/marketing.html', {})
