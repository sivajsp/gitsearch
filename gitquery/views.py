from django.shortcuts import render
from .models import city_list
from .forms import get_city
from .gittask import git_task
def index(request):
    if(request.method == "POST"):
        Form = get_city(request.POST)
        if(Form.is_valid()):
            test = city_list()
            test.name = Form.cleaned_data["city"]
            data = git_task()
            print(type(request.POST["city"]))
            display_data = data.get_data(request.POST["city"])
            test.save()

    else:
        Form = get_city()
        data = git_task()
        display_data = data.get_data("bangalore")
    context = {"dev":display_data,"form":Form}
    return render(request, 'index.html',context)
