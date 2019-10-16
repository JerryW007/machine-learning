


from django.shortcuts import render
from django.http import HttpResponse

def testJson(request):
    context          = {}
    context['hello'] = request.body
    print(request)
    # if request.POST:
    return HttpResponse(request.body)
    # return render(request, 'templates/hello.html', context)