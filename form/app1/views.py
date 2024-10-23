from django.shortcuts import render

# Create your views here.
def fun1(request):
    print(request.GET)
    if request.method=="POST":
        paul="i am "+request.POST.get("wish")
        
    context={"mama":paul}
    return render(request,"aha.html",context)
def fun2(request):
    a=None
    result=None
    print(request.GET)
    if request.method=="POST":
        
        a=int(request.POST.get("even"))
        if a%2==0:
            result=True
        else:
            result=False
    resul={"res":result,"number":a}
    return render(request,"even.html",result)
def fun3(request):
    b=None
    result=None
    print(request.GET)
    if request.method == "POST":
        result = 1
        b=int(request.POST.get("fact"))
        fact = b
        for i in range(1,fact+1):
            result *=   i
    resul={"res":result,"number":b}
    return render(request,"fact.html",resul)



def fun4(request):
    a=None
    b=None
    result=None
    print(request.GET)
    print(request.POST)
    if request.method == "POST":
        a=int(request.POST.get("num1"))
        b=int(request.POST.get("num2"))
        if a>b:
            result = a
        else:
            result = b
    
    return render(request, "greater.html", context={"res": result, "n1": a, "n2": b})



def fun5(request):
    d={"students":[
        {"id": 2143281, "Name": "B.Purushotham", "total_sub": 6, "pass_sub": 6, "Fail_sub": 0},
        {"id": 2143297, "Name": "Sarfaraz", "total_sub": 6, "pass_sub": 6, "Fail_sub": 0},
        {"id": 21432114, "Name": "Sumanth", "total_sub": 6, "pass_sub": 6, "Fail_sub": 0},
        {"id": 21432133, "Name": "Tharun", "total_sub": 6, "pass_sub": 6, "Fail_sub": 2},
    ]}
    result = None
    if request.method=="POST":
        num=int(request.POST.get("num1"))
        print(num)
        for student in d["students"]:
            if student["id"] == num:
                result = student
                break
    context = {"result": result}
    return render(request, "student.html", context)



def fun6(request):
    arm = None
    if request.method=="POST":
        num=int(request.POST.get("num1"))
        print(num)
        result=0
        temp = num
        while temp > 0:
            digit = temp % 10
            result += digit ** 3
            temp //= 10
        arm=(result==num)
        print(arm)
    d={"result":arm}
    return render(request,"arm.html",d)

def fun7(request):
    result=None
    if request.method == "POST":
        num=int(request.POST.get("num1"))
        if num<=2:
            result=True
        for i in range(2,num):
            if num%i == 0:
                result =False
                break
        else:
            result=True
    context={"res":result}
    return render(request,"prime.html",context)
         
   


             
       



