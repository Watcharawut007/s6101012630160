from django.shortcuts import render

# Create your views here.
from calculator.models import Calculate


def home(request):
    history_list = Calculate.objects.all()
    string_list = []
    for history in history_list:
        string_list.append(str(history.num1) + history.operate + str(history.num2) + " " + str(history.result))
    if request.POST.get("find value"):
        num = request.POST['x']
        num2 = request.POST['y']
        operate = request.POST.getlist("operate_list")
        result_list = {}
        for operate in operate:
            object = Calculate.objects.create()
            if operate == "+":
                result = int(num) + int(num2)
                result_list[operate]=result
                object.calculate(num, num2, operate, result)
            elif operate == "-":
                result = int(num) - int(num2)
                result_list[operate]=result
                object.calculate(num, num2, operate, result)
            elif operate == "*":
                result = int(num) * int(num2)
                result_list[operate]=result
                object.calculate(num, num2, operate, result)
            elif operate == "/":
                result = int(num) / int(num2)
                result_list[operate]=result
                object.calculate(num,num2,operate,result)
        return render(request, "calculator/home.html", {"result": result, "operate": operate, "x": num, "y": num2,"result_list":result_list,"history":string_list})
    if request.POST.get('clear_history'):
        for history in history_list:
            history.delete()
        return render(request,"calculator/home.html",{"history":Calculate.objects.all()})
    return render(request,"calculator/home.html",{"history":string_list})