from django.shortcuts import render

# Create your views here.


pupils_list=[
    {"id":1,"Ism": "Abdujabborov Muhammadsaid","Examen": 3,},
    {"id":2,"Ism": "Yusufjon Muhammaadov", "Examen": 5,},
    {"id":3,"Ism": "Shukurjonova Xurshidabonu","Examen": 4},
    {"id":4,"Ism": "Otaboyeva Lobar","Examen": 4},
    {"id":5,"Ism": "Azizbek Aliyev", "Examen": 3},
]

def pupils(request):
    return render(request,'pupils_list.html',context={'pupils':pupils_list})


def pupil(request,pk):
    return render(request,"pupil.html",context={'pupil':pupils_list[pk-1]})