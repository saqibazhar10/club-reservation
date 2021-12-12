from django.http import request
from django.http.request import HttpHeaders
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from club_app.models import Payment, Registered_User,Manager,Reservation,feedback,events,Room,Message
from django.core.mail import send_mail
import datetime 
from datetime import date
import string  
from werkzeug.security import check_password_hash, generate_password_hash
from socket import gaierror
from dateutil.relativedelta import relativedelta
from validate_email_address import validate_email
from django.http import HttpResponse, JsonResponse

from datetime import datetime
def register(request):

    global email
    global user
    msg = {'msg': "The Email Entered Doesnot Exists!"}
    if request.method == "POST":
        firstName = request.POST.get("myname")
        email = request.POST.get("myemail")
        password = request.POST.get("mypass")
        password_hash = generate_password_hash(password)
        check_if_user_exists = Registered_User.objects.filter(email=email).exists()
        if check_if_user_exists:
            return HttpResponse("User Already Exists")
        else:
            user =Registered_User(firstname=firstName,password=password_hash,email=email,Member_Availed=False,Membership_Start_time=datetime.now(),Membership_End_time=datetime.now(),Applied_event="False")
            isvalid=validate_email(email,verify=True)
            if(isvalid):
                snd_mail()

                return redirect("confirm")
            else:
                return render(request ,"reg.html",msg)

    return render(request, "reg.html")

def login(request):
    request.session['mang']=False
    global password
    global a
    global name
    global email
    
    request.session["login"]="1"
    params = {'msg': "Invalid Id or Password"}
    if request.method == "POST":
        email = request.POST.get("myemail")
        request.session["email"]=email
        password = request.POST.get("mypass")

        check_if_user_exists = Registered_User.objects.filter(email=email).exists()
        
        manager_email = Manager.objects.filter(email=email).exists()
        if check_if_user_exists:
            matcheing_password = Registered_User.objects.get(email=email).password
            name= Registered_User.objects.get(email=email).firstname
            if check_password_hash(matcheing_password, password):
                a=1
                request.session['user_name']=name.title()
                return redirect("/")

            else:
                return render(request, 'login.html', params)
                
        
        elif (manager_email):
            matcheing_password = Manager.objects.get(email=email).password
            name= Manager.objects.get(email=email).firstname
            if matcheing_password==password:
                request.session['manager'] = name
                request.session['mang']=True
                return redirect('/Manager')
            else:
    
                return render(request, 'login.html', params)
        
        else:
        
            return render(request, 'login.html', params)

    
    return render(request,"login.html")

def homepage(request):

    try:
        request.session['mang']=False
        user_name = request.session['user_name']
        if a==1:
            return render(request, 'homepage.html',{"name":user_name, "a":a})
        if a==2:
            return render(request, 'homepage.html',a)
    except( KeyError,NameError):
        
        return render(request, 'homepage.html')

def logout(request):
    global a
    a=2
    request.session.clear()
    return redirect("/")


def feed_back(request):
    global a
    try:
        
        if a==1:
            user_name = request.session['user_name']
            if request.method=="POST":
                email=request.session["email"]
                for key, value in email.items():
                    e=(value)
                rating1 = request.POST.get("rating1")
                rating2 = request.POST.get("rating2")
                rating = request.POST.get("rating")
                commentText= request.POST.get("commentText")
                feed = feedback(user_email=e,name=user_name,rating1=rating1,rating2=rating2,rating=rating,commentText=commentText)
                feed.save()
                return render(request,"homepage.html")

    except:
        request.session.clear()
        return redirect("/login")
    
    return render(request, 'feedback.html')

def membership(request):
    if request.method =="POST":
        Mbership = request.POST.get("membership_type")
        global M
        global st
        global fee
        global end
        global check
        global Mem
        email= request.session["email"]
        # member =Registered_User.objects.filter(Member_Availed= Mbership).exists()
        member = Registered_User.objects.filter(email=email).values('Member_Availed')
        if (a==1):
                Mem= Registered_User.objects.get(email=email)
                # resr=Reservation.objects.filter(Court_Types=type , Date=date,Court_Person=Pair).all()
                Mem.Membership_Start_time=datetime.now()
                st=datetime.now()
                fee=0
                if (Mbership=="Premium Membership"):
                    Mem.Membership_End_time=date.today()+ relativedelta(months=+12)
                    end=date.today()+ relativedelta(months=+12)
                    M="Premium Membership"
                    fee=1200
                    check=1
                    
                if (Mbership=="Standard Membership"):
                    Mem.Membership_End_time=date.today()+ relativedelta(months=+6)
                    end=date.today()+ relativedelta(months=+6)
                    M="Standard Membership"
                    fee=600
                    check=1

                if (Mbership=="Basic Membership"):
                    M="Basic Membership"
                    Mem.Membership_End_time=date.today()+ relativedelta(months=+1)
                    end=date.today()+ relativedelta(months=+1)
                    fee=100
                    check=1
                    
                Mem.Member_Availed=Mbership
                for m in member:
                    if (m["Member_Availed"]!="False"):
                        return HttpResponse("Already A member")
                    else:
                     
                        return redirect("/./payment")
    return render(request, 'membership.html')

import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
import random

def snd_mail():
    global rand
    global email
    global mg
    rand= str(random.randint(1000,9999))
    try:
        if mg==1:
            try:
                result = ''.join((random.choice(string.ascii_lowercase) for x in range(6)))
                # result="abcd"
                send_mail(
                    "Room Code",
                    "Your Room Code is Please join with the following roon no :"+ result ,
                    "uetupdates@gmail.com",
                    [email],
                    fail_silently=False

                )
                send_mail(
                    "Live Chat Update",
                    "Following User wants to contact with you "+email +"  Please contact with him with the following Room Code :"+ result ,
                    "uetupdates@gmail.com",
                    ["2019ce21@student.uet.edu.pk"],
                    fail_silently=False

                )
            except :
                return HttpResponse ("Please Login First")
              
    except:
                    send_mail(
                "Email Verification",
                "Your Email Verification Code is :"+ rand ,
                "uetupdates@gmail.com",
                [email],
                fail_silently=False)

def snd_mail2(ofee,email):

                    send_mail(
                    "Booking Scheduled",
                    "Thankyou For Paying :"+ ofee ,
                    "uetupdates@gmail.com",
                    [email],
                    fail_silently=False

                )


def confirm(request):
    if request.method == "POST":
        otp=request.POST.get("mycode")
        if otp==rand:
            user.save(); 
        return redirect("login")
    return render(request, "confirm.html")
from django.db.models import Sum
from collections import Counter

def Manage_Page(request):
    if request.method == "POST":

    #     return redirect("login")
        if (request.POST.get("desc")==None):
            Court_Types = request.POST.get("Court_type")
            Court_Person = request.POST.get("Court_Person")
            Court_Id = request.POST.get("Court_Id")
            Date = request.POST.get("date")
            STime = request.POST.get("stime")
            ETime = request.POST.get("etime")
            pay_amount=request.POST.get("pay_amount")
            R =Reservation(Court_Types=Court_Types,Court_Person=Court_Person,Court_Id=Court_Id,Date=Date,Start_Time=STime,End_Time=ETime,payment=pay_amount,Reserved_person=False,Reserved=False)
            R.save()

        else:
            Name = request.POST.get("name")
            Appling_Fee = request.POST.get("fee")
            Description = request.POST.get("desc")
            image = request.POST.get("img")
            Date=request.POST.get("date")
            Event =events(Name=Name,Description=Description,Appling_Fee=Appling_Fee,Date=Date,image=image)
            
            Event.save()

    manager = request.session['manager']
    member =Registered_User.objects.values_list('Member_Availed',flat=True)
    email_reserved_user=Reservation.objects.values_list("Reserved_person",flat =True)
    Paym=Payment.objects.filter(Date=datetime.now()).values('paid_amount')
    paym=Paym.aggregate(total_price=Sum('paid_amount'))
    day_pay=(paym["total_price"])
    li=[]
    club = Reservation.objects.filter(Reserved=True).values('Court_Types')
    c=list(club)
    grass = 0
    hard = 0
    clay = 0
    for i in c:
        if i["Court_Types"] == "Grass Court":
            grass += 1
        if i["Court_Types"] == "Hard Court":
            hard+=1
        if i["Court_Types"] == "Clay Court":
            clay+=1
            
    for i in email_reserved_user:
        if i !="False":
            li.append(i)
    val=Counter(li).values()
    key=Counter(li).keys()
    s=[]
    d=[]
    for i in val:
        s.append(i)
    for j in key:
        d.append(j)

    # For review section
    star= list(feedback.objects.all().values_list('rating1', flat=True)) 
    rating =feedback.objects.all()
    mylist = zip(star , rating)
    # print(manager)#request.session.clear()
    return render(request,"Manager.html",{"manager":manager,"member":member,"s":s,"d":d,"day_pay":day_pay,"grass":grass,"hard":hard,"clay":clay,"mylist":mylist})


def history(request):
    try:
        email=request.session["email"]
        History = Reservation.objects.filter(Reserved_person=email).all()

        return render(request,"history.html",{"History":History})
    except:
        return redirect("/login")
    
def reservation(request):
    global R
    global check
    global Id
    try:
        if a==1:
            if (request.method=="POST"):
                if "type" in request.POST:
                    type = request.POST.get("type")
                    date = request.POST.get("date")
                    Pair = request.POST.get("Pair")
                    resr=Reservation.objects.filter(Court_Types=type , Date=date,Court_Person=Pair).all()
                    b=1
                    time=datetime.time(datetime.now())
                        

                else:

                    id=(request.POST.get("r_id"))
                    Id=id
                    R = Reservation.objects.get(id=id)
                    R.Reserved_person=request.session["email"]
                    R.Reserved=True
                    check=0 
                    return redirect("/payment")
                    

                return render(request ,"reservation.html",{'resr': resr,'b':b,'time':time})
            return render(request ,"reservation.html")
        else:
            return redirect("/login")

    except NameError:
         HttpResponse("Not logged in")

    return redirect("/login")



def payment(request):
    email= request.session["email"]
    global court_id
    global check
    z="umar"
    if (request.method=="POST"):
        if (check==1):
            Mem.save()
        else:
            
            email = request.POST.get("name")
            ofee =request.POST.get("fee")
            member = Registered_User.objects.filter(email=email).values('Member_Availed')
            for val in member:
                reserved= (val['Member_Availed'])

            if (reserved != "False"):
                pfee = int(ofee)/0.7
                paym =Payment(email=email,reser_id=Id,original_amount=pfee,paid_amount=ofee,Date=datetime.now())
                paym.save()
                R.save()
                snd_mail2(ofee,email)
            else:
                pfee = int(ofee)
                paym =Payment(email=email,reser_id=Id,original_amount=pfee,paid_amount=ofee,Date=datetime.now())
                paym.save()
                R.save()
                snd_mail2(ofee,email)

                        
        return redirect("/")
    else:
        if (check==1):
            p=1
            return render(request, "payment.html",{"M":M,"start_date":st,"end":end,"fee":fee,"email":email,"p":p})
        elif(check==0):
            p=0
            court_id= R.Court_Id
            Start_Time=R.Start_Time
            End_Time=R.End_Time
            Pay=R.payment
            member = Registered_User.objects.filter(email=email).values('Member_Availed')
            re=""
            for val in member:
                re= (val['Member_Availed'])
            if (re != "False"):
                Pay =int(Pay*0.7)
                return render(request,"payment.html",{"court_id":court_id,"email":email,"payment":Pay,"Start_Time":Start_Time,"End_Time":End_Time,"p":p})
            else:
                return render(request,"payment.html",{"court_id":court_id,"email":email,"payment":Pay,"Start_Time":Start_Time,"End_Time":End_Time,"p":p})
            
        else:
            return HttpResponse("Some Error")

def chat(request):
    try:
        log = request.session['login']
        if (log=="1"):
        
            if request.session['mang']==True: 
                return render(request, 'chat.html')
            else:
                global mg
                mg=1
                snd_mail()
                return render(request, 'chat.html')
        else:
            return redirect("/login")
    except KeyError:
        return redirect("/login")

        

def room(request, room):
    try:
        room_details = Room.objects.get(name=room)
        username = request.GET.get('username')
        return render (request, 'room.html',{
        'username': username,
        'room': room,
        'room_details': room_details
    })

    except Room.DoesNotExist:
        room_details = None
        username = request.GET.get('username')
        return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def checkview(request):
    if request.method == "POST":
        room = request.POST['room_name']
        username = request.POST['username']
        # print(request.session['mang'])
        if request.session['mang']==True:
            if Room.objects.filter(name=room).exists():
                request.session.clear()
                return redirect('/'+room+'/?username='+username)
            else:
                new_room = Room.objects.create(name=room)
                new_room.save()
                return redirect('/'+room+'/?username='+username)
            
        else:
            if Room.objects.filter(name=room).exists():
                return redirect('/'+room+'/?username='+username)
            else:
                return redirect("/")
    return HttpResponse("None")


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})
