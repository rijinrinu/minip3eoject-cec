from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import MySQLdb
import webbrowser
db=MySQLdb.connect("localhost","root","","dbrealistic")
c=db.cursor()


    ######################################################################
#                           SMS FUNCTION
######################################################################
def sendsms(ph,msg):
    sendToPhoneNumber= ph
    url = "http://sms.mdsmedia.in/http-api.php?username=7000183&password=LCCCOK123&senderid=LCCCOK&route=23&number="+sendToPhoneNumber+"&message="+msg
    # contents = urllib.request.urlopen(url)
    webbrowser.open(url)

######################################################################
#                           LOAD INDEX PAGE
######################################################################
def index(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    return render(request,"index.html")

######################################################################
#                           LOAD LOGIN PAGE
######################################################################
def login(request):
    """ 
        The function for login process
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        email=request.POST.get("txtEmail")
        pwd=request.POST.get("txtPassword")
        s="select count(*) from tbllogin where username='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            s="select * from tbllogin where username='"+email+"'"
            c.execute(s)
            i=c.fetchone()
            if(i[1]==pwd):
                request.session['email'] = email
                if(i[3]=="1"):
                    if(i[2]=="admin"):
                        return HttpResponseRedirect("/adminhome")
                    elif(i[2]=="architect"):
                        return HttpResponseRedirect("/architecthome")
                    elif(i[2]=="designer"):
                        return HttpResponseRedirect("/designerhome")
                    elif(i[2]=="contractor"):
                        return HttpResponseRedirect("/contractorhome")
                    elif(i[2]=="customer"):
                        return HttpResponseRedirect("/customerhome")
                    elif(i[2]=="shop"):
                        return HttpResponseRedirect("/shophome")
                else:
                    msg="You are not authenticated to login"
            else:
                msg="Incorrect password"
        else:
            msg="User doesnt exist"
    return render(request,"login.html",{"msg":msg})
######################################################################
#                           CUSTOMER REGISTRATION
######################################################################
def customer(request):
    """ 
        The function for customer registration
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        name=request.POST.get("txtName")
        address=request.POST.get("txtAddress")
        contact=request.POST.get("txtContact")
        email=request.POST.get("txtEmail")
        pwd=request.POST.get("txtPassword")
        aadhar=request.FILES["txtaadhar"]
        fs=FileSystemStorage()
        filename=fs.save(aadhar.name,aadhar)
        uploaded_file_url=fs.url(filename)
        s="select count(*) from tbllogin where username='"+str(email)+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="User already registered"
        else:
            s="insert into tblcustomer(cName,cAddress,cContact,cEmail,aadhar) values('"+str(name)+"','"+str(address)+"','"+str(contact)+"','"+str(email)+"','"+str(uploaded_file_url)+"')"
            print(s)
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry registration error"
            else:
                s="insert into tbllogin (username,password,utype,status) values('"+str(email)+"','"+str(pwd)+"','customer','1')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg="Sorry login error"
                else:
                    msg="Registration successfull"
    return render(request,"customer.html",{"msg":msg})


def about(request):
    return render(request,"about.html")


def registeration(request):
    return render(request,"registeration.html")

######################################################################
#                           ARCHITECT REGISTRATION
######################################################################
def architect(request):
    """ 
        The function for architect registration
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        name=request.POST.get("txtName")
        address=request.POST.get("txtAddress")
        contact=request.POST.get("txtContact")
        quali=request.POST.get("txtquali")

        qproof=request.FILES["proof"]
        print(quali)
        fs=FileSystemStorage()
        filename=fs.save(qproof.name,qproof)
        uploaded_file=fs.url(filename)

        email=request.POST.get("txtEmail")
        pwd=request.POST.get("txtPassword")
        about=request.POST.get("about")


        img=request.FILES["txtFile"]
        fs=FileSystemStorage()
        fileimg=fs.save(img.name,img)
        uploaded_file_url=fs.url(fileimg)

        s="select count(*) from tbllogin where username='"+str(email)+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="User already registered"
        else:
            s="insert into tblarchitect(aName,aAddress,aContact,aqualification,aqproof,aEmail,aPhoto,description) values('"+str(name)+"','"+str(address)+"','"+str(contact)+"','"+str(quali)+"','"+str(uploaded_file)+"','"+str(email)+"','"+str(uploaded_file_url)+"','"+str(about)+"')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry registration error"
            else:
                s="insert into tbllogin (username,password,utype,status) values('"+str(email)+"','"+str(pwd)+"','architect','0')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg="Sorry login error"
                else:
                    msg="Registration successfull"
    return render(request,"architect.html",{"msg":msg})
######################################################################
#                           DESIGNER REGISTRATION
######################################################################
def designer(request):
    """ 
        The function for designer registration
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        name=request.POST.get("txtName")
        address=request.POST.get("txtAddress")
        contact=request.POST.get("txtContact")
        quali=request.POST.get("txtquali")
        about=request.POST.get("about")

        qproof=request.FILES["txtproof"]
        fs=FileSystemStorage()
        filename=fs.save(qproof.name,qproof)
        uploaded_file=fs.url(filename)
        email=request.POST.get("txtEmail")
        pwd=request.POST.get("txtPassword")
        img=request.FILES["txtFile"]
        fs=FileSystemStorage()
        filename=fs.save(img.name,img)
        uploaded_file_url=fs.url(filename)

        s="select count(*) from tbllogin where username='"+str(email)+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="User already registered"
        else:
            s="insert into tbldesigner(dName,dAddress,dContact,dqualification,dqproof,dEmail,dPhoto,description) values('"+str(name)+"','"+str(address)+"','"+str(contact)+"','"+str(quali)+"','"+str(uploaded_file)+"','"+str(email)+"','"+str(uploaded_file_url)+"','"+str(about)+"')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry registration error"
            else:
                s="insert into tbllogin (username,password,utype,status) values('"+str(email)+"','"+str(pwd)+"','designer','0')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg="Sorry login error"
                else:
                    msg="Registration successfull"
    return render(request,"designer.html",{"msg":msg})
######################################################################
#                           CONTRACTOR REGISTRATION
######################################################################
def contractor(request):
    """ 
        The function for contractor registration
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        name=request.POST.get("txtName")
        address=request.POST.get("txtAddress")
        contact=request.POST.get("txtContact")
        about=request.POST.get("about")

        pw=request.FILES["txtpw"]
        fs=FileSystemStorage()
        filename=fs.save(pw.name,pw)
        uploaded_file=fs.url(filename)

        email=request.POST.get("txtEmail")
        pwd=request.POST.get("txtPassword")

        img=request.FILES["txtFile"]
        fs=FileSystemStorage()
        filename=fs.save(img.name,img)
        uploaded_file_url=fs.url(filename)

        s="select count(*) from tbllogin where username='"+str(email)+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="User already registered"
        else:
            s="insert into tblcontractor(cName,cAddress,cContact,cprework,cEmail,cPhoto,description) values('"+str(name)+"','"+str(address)+"','"+str(contact)+"','"+str(uploaded_file)+"','"+str(email)+"','"+str(uploaded_file_url)+"','"+str(about)+"')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry registration error"
            else:
                s="insert into tbllogin (username,password,utype,status) values('"+str(email)+"','"+str(pwd)+"','contractor','0')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg="Sorry login error"
                else:
                    msg="Registration successfull"
    return render(request,"contractor.html",{"msg":msg})
######################################################################
#                          ADMIN HOME
######################################################################
def adminhome(request):
    """ 
        The function for adminhome
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    return render(request,"adminhome.html")
######################################################################
#                          ADMIN ARCHITECT
######################################################################
def adminarchitect(request):
    """ 
        The function for architect details for admin
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select * from tblarchitect where aEmail in(select username from tbllogin where status='0')"
    c.execute(s)
    data=c.fetchall()
    print("*"*300)
    print(data)
    print("*"*300)

    s="select * from tblarchitect where aEmail in(select username from tbllogin where status='1')"
    c.execute(s)
    data1=c.fetchall()
    print("*"*300)
    print(data1)
    print("*"*300)
    return render(request,"adminarchitect.html",{"data":data,"data1":data1})

def deletearch(request):
    email=request.GET.get("email")
    print(email)
    c.execute("delete from tblarchitect where aEmail='"+str(email)+"'")
    db.commit()
    return HttpResponseRedirect("adminarchitect")



######################################################################
#                          ADMIN DESIGNER
######################################################################
def admindesigner(request):
    """ 
        The function for designer details for admin
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select * from tbldesigner where dEmail in(select username from tbllogin where status='0')"
    c.execute(s)
    data=c.fetchall()
    s="select * from tbldesigner where dEmail in(select username from tbllogin where status='1')"
    c.execute(s)
    data1=c.fetchall()
    return render(request,"admindesigner.html",{"data":data,"data1":data1})


def deletedesi(request):
    email=request.GET.get("email")
    print(email)
    c.execute("delete from 	tbldesigner where dEmail='"+str(email)+"'")
    db.commit()
    return HttpResponseRedirect("admindesigner")



######################################################################
#                          ADMIN CONTRACTOR
######################################################################
def admincontractor(request):
    """ 
        The function for contractor details for admin
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select * from tblcontractor where cEmail in(select username from tbllogin where status='0')"
    c.execute(s)
    data=c.fetchall()
    s="select * from tblcontractor where cEmail in(select username from tbllogin where status='1')"
    c.execute(s)
    data1=c.fetchall()
    return render(request,"admincontractor.html",{"data":data,"data1":data1})

def deletecon(request):
    email=request.GET.get("email")
    print(email)
    c.execute("delete from tblcontractor where cEmail='"+str(email)+"'")
    db.commit()
    return HttpResponseRedirect("admincontractor")
######################################################################
#                          ADMIN CUSTOMER
######################################################################
def admincustomer(request):
    """ 
        The function for customer details for admin
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select * from tblcustomer where cEmail in(select username from tbllogin where status='1')"
    c.execute(s)
    data=c.fetchall()
    return render(request,"admincustomer.html",{"data":data})
######################################################################
#                          ADMIN APPROVE CUSTOMER
######################################################################
def adminapproveuser(request):
    """ 
        The function to approve users
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.GET.get("id")
    status=request.GET.get("status")
    url=request.GET.get("url")
    s="update tbllogin set status='"+status+"' where username='"+email+"'"
    c.execute(s)
    db.commit()
    c.execute("select utype from tbllogin where username='"+email+"'")
    k=c.fetchone()
    if(k[0]=='architect'):
        n="Select aContact from tblarchitect where aEmail='"+email+"'"
        c.execute(n)
        d=c.fetchone()
        contact=d[0]
        msg="Your registeration is approved"
       
    if(k[0]=='designer'):
        n="Select dContact from tbldesigner where dEmail='"+email+"'"
        c.execute(n)
        d=c.fetchone()
        contact=d[0]
        msg="Your registeration is approved"
        
    if(k[0]=='contractor'):
        n="Select cContact from tblcontractor where cEmail='"+email+"'"
        c.execute(n)
        d=c.fetchone()
        contact=d[0]
        msg="Your registeration is approved"
        
    if(k[0]=='customer'):
        n="Select cContact from tblcustomer where cEmail='"+email+"'"
        c.execute(n)
        d=c.fetchone()
        contact=d[0]
        msg="Your registeration is approved"
        
    if(k[0]=='shop'):
        n="Select scontact from shop where semail='"+email+"'"
        c.execute(n)
        d=c.fetchone()
        contact=d[0]
        msg="Your registeration is approved"
        
    return HttpResponseRedirect(url)
######################################################################
#                          CUSTOMER HOME
######################################################################
def customerhome(request):
    """ 
        The function for customer home
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select * from tblcustomer where cEmail='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    if request.POST:
        name=request.POST.get("txtName")
        address=request.POST.get("txtAddress")
        contact=request.POST.get("txtContact")
        email=request.POST.get("txtEmail")
        txtAbout=request.POST.get("txtAbout")

        e="update tblcustomer set cName='"+str(name)+"',cAddress='"+str(address)+"',cContact='"+str(contact)+"',cemail='"+str(email)+"' where cEmail='"+str(email)+"'"
        c.execute(e)
        db.commit()
        return HttpResponseRedirect("/customerhome")
    
        

    return render(request,"customerhome.html",{"data":data})
######################################################################

#                          CUSTOMER REQUIREMENT
######################################################################
def customerrequirement(request):
    """ 
        The function for customer requirement
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    msg=""
   

    if(request.POST):
        bed=request.POST["txtBed"]
        bath=request.POST["txtBath"]
        attached=request.POST["txtAttached"]
        car=request.POST["txtCar"]
        kitchen=request.POST["txtKitchen"]
        sitout=request.POST["txtSitout"]
        work=request.POST["txtWork"]
        floor=request.POST["txtFloor"]
        sqft=request.POST["txtSqft"]
        other=request.POST["txtOther"]
        sd="select count(*) from account where u_id='"+str(email)+"'"
        c.execute(sd)
        dp=c.fetchone()
        print(dp)
        if dp[0]>0:
            s="insert into tblrequirement(cEmail,bedroom,bathroom,attached,carporch,kitchen,sitout,workarea,floor,sqft,other,reqDate,reqStatus) values('"+email+"','"+bed+"','"+bath+"','"+attached+"','"+car+"','"+kitchen+"','"+sitout+"','"+work+"','"+floor+"','"+sqft+"','"+other+"',(select sysdate()),'requested')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry some error occured"
            else:
                msg="Requirement submitted"
        else:
            msg="please add an account"
    s="Select * from tblrequirement where cEmail='"+email+"'  and tblrequirement.reqStatus<>'plan approved'"
    c.execute(s)
    data=c.fetchall()

    email=request.session["email"]
    s1="Select * from tblrequirement where cEmail='"+email+"'"
    c.execute(s1)
    data1=c.fetchall()
    return render(request,"customerrequirement.html",{"msg":msg,"data":data,"data1":data1})
######################################################################
#                          CUSTOMER PLANS
######################################################################
def customerplan(request):
    """ 
        The function to load plan status
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    rid=request.GET.get("id")
    s="select tblrequirement.reqId,tblarchitect.aName,tblplan.sqft,tblplan.cost,tblplan.planStatus,tblplan.planId,tblplan.plan from tblrequirement,tblplan,tblarchitect where tblarchitect.aEmail=tblplan.aEmail and tblplan.reqId=tblrequirement.reqId and tblplan.reqId='"+str(rid)+"' and tblrequirement.cEmail='"+str(email)+"'"
    c.execute(s)
    data=c.fetchall()


    email=request.session["email"]
    s12="select tblrequirement.reqId,tblarchitect.aName,tblplan.sqft,tblplan.cost,tblplan.planStatus,tblplan.planId,tblplan.plan,tblplan.fees from tblrequirement,tblplan,tblarchitect where tblarchitect.aEmail=tblplan.aEmail and tblplan.reqId=tblrequirement.reqId and tblrequirement.cEmail='"+email+"' and tblplan.planStatus='approved' or tblplan.planStatus='3D requested'"
    c.execute(s12)
    data12=c.fetchall()
    print(data12)
    return render(request,"customerplan.html",{"data":data,"data12":data12})
######################################################################
#                          CUSTOMER VIEW PLANS
######################################################################
def customerviewplan(request):
    """ 
        The function to view plan
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    plan=request.GET.get("id")
    return render(request,"customerviewplan.html",{"plan":plan})

    ###########################################

def shopview(request):
    """ 
        The function to view plan
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    simage=request.GET.get("id")
    return render(request,"shopview.html",{"simage":simage})



def cview(request):
    """ 
        The function to view plan
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    simage=request.GET.get("id")
    return render(request,"cview.html",{"simage":simage})
#####################3

def archviewplan(request):
   
    plan=request.GET.get("id")
    return render(request,"archviewplan.html",{"plan":plan})
######################################################################
#                          CUSTOMER PLAN UPDATE
######################################################################
def customerplanupdate(request):
    """ 
        The function to update plan status
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    pid=request.GET.get("id")
    fees=request.GET.get("fees")
    rid=request.GET.get("rid")


    request.session["pid"]=pid
    request.session["fees"]=fees
    request.session["rid"]=rid

    status=request.GET.get("status")
    url=request.GET.get("url")
    rid=request.GET.get("rid")
    s="update tblplan set planStatus='"+status+"',feesstatus='paid' where planId='"+pid+"'"
    try:
        c.execute(s)
        db.commit()
    except:
        pass
    else:
        if(status=="approved"):
            status1="rejected"
        elif(status=="rejected"):
            status1="approved"
        s="update tblplan set planStatus='"+status1+"' where reqId='"+rid+"' and planId<>'"+pid+"'"
        # s="delete from tblplan  where reqId='"+rid+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            pass
        else:
            if(status=="approved"):
                status="plan approved"
                s="update tblrequirement set reqStatus='"+status+"' where reqId='"+rid+"'"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    pass
                else:
                    url='paymentplan'
                    # return HttpResponseRedirect(?id="+pid)
                    return HttpResponseRedirect("/"+url+"?id="+pid)
                    return 
            else:
                return HttpResponseRedirect("/"+url)
######################################################################
#                  
    
######################################################################
#                          CUSTOMER APPROVED PLANS
######################################################################
def customerapprovedplan(request):
    """ 
        The function to load plan status
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select tblrequirement.reqId,tblarchitect.aName,tblplan.sqft,tblplan.cost,tblplan.planStatus,tblplan.planId,tblplan.plan,tblplan.fees from tblrequirement,tblplan,tblarchitect where tblarchitect.aEmail=tblplan.aEmail and tblplan.reqId=tblrequirement.reqId and tblrequirement.cEmail='"+email+"' and (tblplan.planStatus='approved' or tblplan.planStatus='3D requested')"
    c.execute(s)
    data=c.fetchall()
    print(data)
    return render(request,"customerapprovedplan.html",{"data":data})
######################################################################
#                          CUSTOMER VIEW DESIGNER
######################################################################
def customerviewdesigner(request):
    """ 
        The function to load designers
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    y=request.GET.get("id")
    print(y)
    request.session["planid"]=y
    s="select * from tbldesigner where dEmail in (select username from tbllogin where status='1')"
    c.execute(s)
    data=c.fetchall()
    return render(request,"customerviewdesigner.html",{"data":data})
######################################################################
#                          CUSTOMER PASS PLAN
######################################################################
def customerpassplan(request):
    """ 
        The function to pass work to designer
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.GET.get("id")
    planid=request.session["planid"]
    s="insert into tbldesignrequest(planId,dEmail,dreqStatus) values('"+str(planid)+"','"+str(email)+"','requested')"
    try:
        c.execute(s)
        db.commit()
    except:
        pass
    else:
        s="update tblplan set planStatus='3D requested' where planId='"+str(planid)+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            pass
        else:
            return HttpResponseRedirect("/customerdesignrequest")
######################################################################
#                        CUSTOMER DESIGN REQUEST
######################################################################
def customerdesignrequest(request):
    """ 
        The function for request for design
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select tblrequirement.reqId,tbldesigner.dName,tblplan.sqft,tblplan.cost,tbldesignrequest.dreqId,tbldesignrequest.dreqStatus from tblrequirement,tbldesigner,tblplan,tbldesignrequest where tblrequirement.reqId=tblplan.reqId and tblplan.planId=tbldesignrequest.planid and tbldesigner.dEmail=tbldesignrequest.dEmail and tblrequirement.cEmail='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"customerdesignrequest.html",{"data":data})
######################################################################
#                        CUSTOMER VIDEOS
######################################################################
def customervideo(request):
    """ 
        The function for request for design
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select tbldesignrequest.dreqId,tbldesigner.dName,tblvideo.video,tblvideo.video,tblvideo.videoId,tblvideo.amount from tbldesignrequest,tbldesigner,tblvideo where tbldesignrequest.dreqId=tblvideo.dreqId and tbldesignrequest.dEmail=tbldesigner.dEmail and tbldesignrequest.planId in(select planId from tblplan where reqId in(select reqId from tblrequirement where cEmail='"+email+"')) and tbldesignrequest.dreqStatus='video uploaded'"
    c.execute(s)
    data=c.fetchall()
    
    print("*"*300)
    print(data)
    print("*"*300)

    s="select tbldesignrequest.dreqId,tbldesigner.dName,tblvideo.video,tblvideo.videoId from tbldesignrequest,tbldesigner,tblvideo where tbldesignrequest.dreqId=tblvideo.dreqId and tbldesignrequest.dEmail=tbldesigner.dEmail and tbldesignrequest.planId in(select planId from tblplan where reqId in(select reqId from tblrequirement where cEmail='"+email+"')) and tbldesignrequest.dreqStatus='video approved'"
    c.execute(s)
    data1=c.fetchall()



    s1="select tbldesignrequest.dreqId,tbldesigner.dName,tblvideo.video,tblvideo.video,tblvideo.videoId,tblvideo.amount from tbldesignrequest,tbldesigner,tblvideo where tbldesignrequest.dreqId=tblvideo.dreqId and tbldesignrequest.dEmail=tbldesigner.dEmail and tbldesignrequest.planId in(select planId from tblplan where reqId in(select reqId from tblrequirement where cEmail='"+email+"')) "
    print(s1)
    c.execute(s1)
    pdata=c.fetchall()
    return render(request,"customervideo.html",{"data":data,"data1":data1,"pdata":pdata})
######################################################################
#                          CUSTOMER VIDEO UPDATE
######################################################################
def customervideoupdate(request):
    """ 
        The function to update video status
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    pid=request.GET.get("id")
    print("piddd=",pid)
    fees=request.GET.get("fees")
    print("fees=",fees)

    request.session["vid"]=pid
    request.session["fees"]=fees
    print(request.session["vid"])

    status=request.GET.get("status")
    print(status)
    url=request.GET.get("url")
    s="update tblvideo set videoStatus='"+status+"'and paymentstatus='paid' where dreqId='"+pid+"'"
    print("sssssssssssssssssssttttttttaaaaaaaaattttttttuuuuuuuuuuussssssssss",s)
    try:
        c.execute(s)
        db.commit()
    except:
        pass
    else:
        if(status=="approved"):
                status="video approved"
                s="update tbldesignrequest set dreqStatus='"+status+"' where dreqId in(select dreqId from tblvideo where dreqId	='"+pid+"')"
                print(s)
                try:
                    c.execute(s)
                    db.commit()
                except:
                    pass
                else:
                    url="paymentplan"
                    return HttpResponseRedirect("/"+url+"?amount="+fees)
        else:
                return HttpResponseRedirect(url)
######################################################################
#                        CUSTOMER VIEW VIDEO
######################################################################
def customerview3D(request):
    """ 
        The function for request for design
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    video=request.GET.get("id")
    
    return render(request,"customerview3D.html",{"video":video})
######################################################################
#                          CUSTOMER SELECT CONTRACTOR
######################################################################
def customerselectcontractor(request):
    """ 
        The function for request for architect
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    
   
    s="select * from tblcontractor where cEmail in(select username from tbllogin where status='1')"
    c.execute(s)
    data=c.fetchall()
    print(data)
    return render(request,"customerselectcontractor.html",{"data":data})
######################################################################
#                          CUSTOMER ASSIGN WORK
######################################################################
def customerassignwork(request):
    """ 
        The function for request for contractor
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    cemail=request.GET.get("id")
    vid=request.session["vid"]
    
    s="insert into tblwork (videoId,cEmail,wDate,wStatus) values('"+str(vid)+"','"+str(cemail)+"',(select sysdate()),'assigned')"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/customerwork")
######################################################################
#                          CUSTOMER SELECT CONTRACTOR
######################################################################
def customerwork(request):
    """ 
        The function to view current works
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select tblwork.workId,tblcontractor.cName,tblplan.sqft,tblwork.wStatus from tblwork,tblcontractor,tblplan,tblvideo,tbldesignrequest where tblwork.videoId=tblvideo.videoId and tblvideo.dreqId=tbldesignrequest.dreqId and tbldesignrequest.planId=tblplan.planId and tblwork.cEmail=tblcontractor.cEmail and tblplan.reqId in(select reqId from tblrequirement where cEmail='"+email+"') "
    c.execute(s)
    data=c.fetchall()
    return render(request,"customerwork.html",{"data":data})
######################################################################
#                          ARCHITECT HOME
######################################################################
def architecthome(request):
    """ 
        The function for request for architect
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select * from tblarchitect where aEmail='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    if request.POST:
        name=request.POST.get("txtName")
        address=request.POST.get("txtAddress")
        contact=request.POST.get("txtContact")
        email=request.POST.get("txtEmail")
        txtAbout=request.POST.get("txtAbout")
        e="update tblarchitect set aName='"+str(name)+"',aAddress='"+str(address)+"',aContact='"+str(contact)+"',description='"+str(txtAbout)+"' where aEmail='"+str(email)+"'"
        c.execute(e)
        db.commit()
        return HttpResponseRedirect("/architecthome")
    return render(request,"architecthome.html",{"data":data})
######################################################################
#                          ARCHITECT REQUEST
######################################################################
def architectrequest(request):
    """ 
        The function for request for architect
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session['email']
    s="select tblrequirement.*,tblcustomer.cName from tblcustomer,tblrequirement,tblallocation,tblarchitect where tblrequirement.cEmail=tblcustomer.cEmail and tblallocation.Status='assigned' and tblallocation.archid='"+str(email)+"' and tblallocation.archid=tblarchitect.aEmail and tblallocation.requid=tblrequirement.reqId and tblrequirement.reqStatus='requested'"
    print("0"*20)
    print(s)
    print("0"*20)
    c.execute(s)
    data=c.fetchall()
    print(data)
    print("0"*20)
    return render(request,"architectrequirement.html",{"data":data})
######################################################################
#                          ARCHITECT ADD PLAN
######################################################################
def architectaddplan(request):
    """ 
        The function to add plan
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    email=request.session["email"]
    rid=request.GET.get("id")
    if(request.POST):
        img=request.FILES["txtFile"]
        fs=FileSystemStorage()
        filename=fs.save(img.name,img)
        uploaded_file_url=fs.url(filename)
        sqft=request.POST["txtSqft"]
        cost=request.POST["txtCost"]
        fees=sqft
        s="insert into tblplan (aEmail,reqId,plan,sqft,cost,planStatus,fees) values('"+email+"','"+rid+"','"+uploaded_file_url+"','"+sqft+"','"+cost+"','submitted','"+str(fees)+"')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            s="update tblrequirement set reqStatus='plan uploaded' where reqId='"+rid+"'"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry error"
            else:
                msg="Plan added"
    return render(request,"architectaddplan.html",{"msg":msg})
######################################################################
#                          ARCHITECT PLANS
######################################################################
def architectplan(request):
    """ 
        The function to load plan status
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select tblrequirement.reqId,tblcustomer.cName,tblplan.sqft,tblplan.cost,tblplan.planStatus,tblplan.plan from tblrequirement,tblplan,tblcustomer where tblcustomer.cEmail=tblrequirement.cEmail and tblplan.reqId=tblrequirement.reqId and tblplan.aEmail='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    print(data)
    return render(request,"architectplan.html",{"data":data})
######################################################################
#                          DESIGNER HOME
######################################################################
def designerhome(request):
    """ 
        The function for designer home
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select * from tbldesigner where dEmail='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    if request.POST:
        name=request.POST.get("txtName")
        address=request.POST.get("txtAddress")
        contact=request.POST.get("txtContact")
        email=request.POST.get("txtEmail")
        txtAbout=request.POST.get("txtAbout")

        e="update tbldesigner set dName='"+str(name)+"',dAddress='"+str(address)+"',dContact='"+str(contact)+"',description='"+str(txtAbout)+"' where dEmail='"+str(email)+"'"
        c.execute(e)
        db.commit()
        return HttpResponseRedirect("/designerhome")

    return render(request,"designerhome.html",{"data":data})
######################################################################
#                          DESIGNER REQUEST
######################################################################
def designerrequest(request):
    """ 
        The function to view all design request
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select tblcustomer.cName,tblcustomer.cAddress,tblcustomer.cContact,tblplan.plan,tblplan.sqft,tbldesignrequest.dreqId from tbldesignrequest,tblcustomer,tblplan,tblrequirement where tbldesignrequest.dEmail='"+str(email)+"' and tbldesignrequest.planId=tblplan.planId and tblplan.reqId=tblrequirement.reqId and tblrequirement.cEmail=tblcustomer.cEmail and tbldesignrequest.dreqStatus='requested'"
    print(s)
    c.execute(s)
    data=c.fetchall()
    print(data)
    return render(request,"designerrequest.html",{"data":data})
######################################################################
#                          DESIGNER ADD VIDEO
######################################################################
def designeraddvideo(request):
    """ 
        The function to view all design request
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    dreqid=request.GET.get("id")
    if(request.POST):
        fees=request.POST["fees"]
        img=request.FILES["txtFile"]
        sqft=request.POST["txtSqft"]
        fs=FileSystemStorage()
        filename=fs.save(img.name,img)
        uploaded_file_url=fs.url(filename)
        
        s="insert into tblvideo (dreqId,video,videoStatus,amount) values('"+dreqid+"','"+uploaded_file_url+"','video uploaded','"+fees+"')"
        print(s)
        try:

            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            s="update tbldesignrequest set dreqStatus='video uploaded' where dreqId='"+dreqid+"'"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry som error"
            else:
                msg="Video added successfully"
    return render(request,"designeraddvideo.html",{"msg":msg})
######################################################################
#                          CONTRACTOR HOME
######################################################################
def contractorhome(request):
    """ 
        The function for contractor home
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select * from tblcontractor where cEmail='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    if request.POST:
        name=request.POST.get("txtName")
        address=request.POST.get("txtAddress")
        contact=request.POST.get("txtContact")
        email=request.POST.get("txtEmail")
        txtAbout=request.POST.get("txtAbout")

        e="update tblcontractor set cName='"+str(name)+"',cAddress='"+str(address)+"',cContact='"+str(contact)+"',description='"+str(txtAbout)+"' where cEmail='"+str(email)+"'"
        c.execute(e)
        db.commit()
        return HttpResponseRedirect("/contractorhome")
    return render(request,"contractorhome.html",{"data":data})
######################################################################
#                          CONTRACTOR REQUEST
######################################################################
def contractorrequest(request):
    """ 
        The function to view contractor request
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    print(email)
    s="SELECT tblcustomer.cName,tblcustomer.cAddress,tblcustomer.cContact,tblplan.plan,tblplan.sqft,tblwork.*,tblrequirement.* FROM tblrequirement JOIN tblcustomer ON tblrequirement.cEmail=tblcustomer.cEmail JOIN tblplan ON tblplan.reqId=tblrequirement.`reqId` JOIN tbldesignrequest ON tbldesignrequest.planId=tblplan.`planId` JOIN tblvideo ON tblvideo.`dreqId`=tbldesignrequest.dreqId JOIN tblwork ON tblwork.`videoId`=tblvideo.`videoId` where tblwork.cEmail='"+str(email)+"' and tblwork.wStatus='assigned'"
    print("0"*100)
    print(s)
    print("0"*100)
    c.execute(s)
    data=c.fetchall()
    print(data)
    print("0"*100)
    return render(request,"contractorrequest.html",{"data":data})
    ########################myself#######################33
def customerviewplans(request):
    email=request.session["email"]
    s="Select * from tblrequirement where cEmail='"+email+"'  and tblrequirement.reqStatus<>'plan approved'"
    c.execute(s)
    data1=c.fetchall()
    print(data1)


    email=request.session["email"]
    s1="select tblrequirement.reqId,tblarchitect.aName,tblplan.sqft,tblplan.cost,tblplan.planStatus,tblplan.planId,tblplan.plan,tblplan.fees from tblrequirement,tblplan,tblarchitect where tblarchitect.aEmail=tblplan.aEmail and tblplan.reqId=tblrequirement.reqId and tblrequirement.cEmail='"+email+"' and (tblplan.planStatus='approved' or tblplan.planStatus='3D requested')"
    c.execute(s1)
    data12=c.fetchall()
    print(data12)
    return render(request,"customerviewplans.html",{"data1":data1,"data12":data12})
#############################
def assignarchitect(request):
    msg=""
    data=""

    if(request.POST):
        msg=""
        
        reqid=request.GET.get('reqid')
        aid=request.POST.get('archid')
        m="insert into tblallocation(requid,archid,status) values('"+str(reqid)+"','"+str(aid)+"','assigned')"
        c.execute(m)
        db.commit()
        
        msg="Assigned successfuly"
    n="select * from tblarchitect,tbllogin where tbllogin.status='1' and tblarchitect.aEmail=tbllogin.username "
    c.execute(n)
    data1=c.fetchall()
    print(data1)
    data=showarchitect()
    return render(request,"assignarchitect.html",{"data":data,"msg":msg,"data1":data1})
def showarchitect():

    data=""
    c.execute("select * from tblarchitect where aEmail in(select username from tbllogin where status='1')")
    
    data=c.fetchall()
    return data
   

def contractorapprove(request):
    if(request.GET):

        email=request.GET.get("cemail")
        m=("update tblwork,tblcontractor set tblwork.wStatus='Approved' where tblwork.cEmail='"+str(email)+"' and tblcontractor.cEmail=tblwork.cEmail and tblwork.wStatus='assigned'")
        c.execute(m)
        print(m)
        db.commit()
    return render(request,"contractorrequest.html")




###################updated By Bvb##############################


#########customer add feed back #################################


def feedback(request):
    uid=request.session['email']
    if(request.POST):
        msg=""
        
        # reqid=request.GET.get('subject')
        aid=request.POST.get('feedback')
        m="insert into feedback(feedback,uid) values('"+str(aid)+"','"+str(uid)+"')"
        c.execute(m)
        db.commit()
        
    return render(request,"customeraddfeedback.html")

# def payment(request):
#     return render(request,"payment.html")


def payment(request):
    if request.GET:
        request.session["amount"]=request.GET.get("amount")
    if request.POST:
        return HttpResponseRedirect("/payment1/")

    return render(request,"payment1.html")

import datetime
def payment1(request):
    amount=request.session["amount"]
    if request.POST:
       
        # date=datetime.date.today()
        # print(date)
        # query="insert into payment (uid,bid,amount,date) values('"+str(uid)+"','"+str(bid)+"','"+str(amount)+"','"+str(date)+"')"
        # c.execute(query)
        # db.commit()
        


        return HttpResponseRedirect("/payment2/")
    return render(request,"payment2.html",{"amount":amount})
def payment2(request):
    if request.POST:

        return HttpResponseRedirect("/payment3/")
    return render(request,"payment3.html")
def payment3(request):
    if request.POST:
        return HttpResponseRedirect("/payment4/")
    return render(request,"payment4.html")
def payment4(request):
    # a="update booking set status='paid' where uid='"+str(request.session['userid'])+"' and bookid='"+str(request.session['bookingid'])+"'"
    # c.execute(a)
    # db.commit()
    # if request.POST:
    #     return HttpResponseRedirect("/payment3/")
    return render(request,"payment5.html")




#############admin view feed back #################

def viewfeedback(request):

    data=""
    c.execute("select feedback.*,tblcustomer.* from feedback join tblcustomer on feedback.uid=tblcustomer.cEmail")
    
    data=c.fetchall()
    print(data)
    return render(request,"adminviewfeedback.html",{"data":data})


    ###################Add Shop ###########
def shop(request):
    """ 
        The function for contractor registration
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        name=request.POST.get("txtName")
        address=request.POST.get("txtAddress")
        contact=request.POST.get("txtContact")
        pw=request.FILES["txtpw"]
        fs=FileSystemStorage()
        filename=fs.save(pw.name,pw)
        uploaded_file=fs.url(filename)

        email=request.POST.get("txtEmail")
        pwd=request.POST.get("txtPassword")

       
        s="select count(*) from tbllogin where username='"+str(email)+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="User already registered"
        else:
            s="insert into shop(sname,saddress,scontact,simage,semail) values('"+str(name)+"','"+str(address)+"','"+str(contact)+"','"+str(uploaded_file)+"','"+str(email)+"')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry registration error"
            else:
                s="insert into tbllogin (username,password,utype,status) values('"+str(email)+"','"+str(pwd)+"','shop','0')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg="Sorry login error"
                else:
                    msg="Registration successfull"
    return render(request,"shop.html",{"msg":msg})




def product(request):
    sid=request.session['email']
    msg=""
    if(request.POST):
        name=request.POST.get("txtName")
        address=request.POST.get("txtAddress")
        contact=request.POST.get("txtContact")
        pw=request.FILES["proof"]
        fs=FileSystemStorage()
        filename=fs.save(pw.name,pw)
        uploaded_file=fs.url(filename)


       
        s="insert into product(sid,pname,price,description,image) values('"+str(sid)+"','"+str(name)+"','"+str(contact)+"','"+str(address)+"','"+str(uploaded_file)+"')"
        c.execute(s)
        db.commit()
        msg="Added SuccessFully"
    return render(request,"shopaddproduct.html",{"msg":msg})


def viewproduct(request):
    msg=""

    data=""
    c.execute("select product.*,shop.* from product join shop on product.sid=shop.semail")
    
    data=c.fetchall()
    print(data)
    if request.POST:
        pid=request.POST.get("pid")
        sid=request.POST.get("sid")
        q=request.POST.get("q")
        uid=request.session['email']
        s="insert into booking(sid,pid,q,uid) values('"+str(pid)+"','"+str(sid)+"','"+str(q)+"','"+str(uid)+"')"
        c.execute(s)
        db.commit()
        msg="Booked Successfully"
    return render(request,"zcviewproduct.html",{"data":data,"msg":msg})

######################################################
def adminviewshop(request):
    """ 
        The function for designer details for admin
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select * from shop where semail in(select username from tbllogin where status='0')"
    c.execute(s)
    data=c.fetchall()
    s="select * from shop where semail in(select username from tbllogin where status='1')"
    c.execute(s)
    data1=c.fetchall()
    return render(request,"adminviewshop.html",{"data":data,"data1":data1})

###############################################################
def shophome(request):
    """ 
        The function for customer home
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select * from shop where semail='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    if request.POST:
        name=request.POST.get("txtName")
        address=request.POST.get("txtAddress")
        contact=request.POST.get("txtContact")
        email=request.POST.get("txtEmail")
        e="update shop set sname='"+str(name)+"',saddress='"+str(address)+"',scontact='"+str(contact)+"' where semail='"+str(email)+"'"
        c.execute(e)
        db.commit()
        return HttpResponseRedirect("/shophome")
    return render(request,"shophome.html",{"data":data})


    ##############################################################
def shopviewbook(request):
    sid=request.session['email']

    data=""
    c.execute("select booking.*,tblcustomer.*,shop.* from booking join tblcustomer on booking.uid=tblcustomer.cEmail join shop on shop.semail=booking.sid where shop.semail='"+str(sid)+"'")
    
    data=c.fetchall()
    print(data)
    return render(request,"shopviewbooking.html",{"data":data})
################view previous booking###########
def previous(request):
    email=request.session["email"]
    s="Select * from tblrequirement where cEmail='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"customerviewpreviousrequirements.html",{"data":data})


################add account #############

def account(request):
    msg=""
    if request.POST:
        upi=request.POST.get("upi")
        cardno=request.POST.get("cardno")
        cvv=request.POST.get("cvv")
        exp=request.POST.get("exp")
        upi=request.POST.get("upi")


        uid=request.session['email']
        s="insert into account(u_id,acc_no,card_no,cvv,exp_date,upi,bal) values('"+str(uid)+"','"+str(upi)+"','"+str(cardno)+"','"+str(cvv)+"','"+str(exp)+"','"+str(upi)+"','100000')"
        c.execute(s)
        db.commit()
        msg="Added  Successfully"
    return render(request,"customeraddaccount.html",{"msg":msg})



    ########new Payment#################
#########################################
def contractorprequest(request):
    """ 
        The function to view contractor request
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="SELECT tblcustomer.cName,tblcustomer.cAddress,tblcustomer.cContact,tblplan.plan,tblplan.sqft,tblwork.*,tblrequirement.* FROM tblrequirement JOIN tblcustomer ON tblrequirement.cEmail=tblcustomer.cEmail JOIN tblplan ON tblplan.reqId=tblrequirement.`reqId` JOIN tbldesignrequest ON tbldesignrequest.planId=tblplan.`planId` JOIN tblvideo ON tblvideo.`dreqId`=tbldesignrequest.dreqId JOIN tblwork ON tblwork.`videoId`=tblvideo.`videoId` WHERE tblwork.cEmail='"+str(email)+"'"

    print("#"*100)
    
    print(s)
    print("#"*100)
    c.execute(s)
    data=c.fetchall()

    # print(data)

    return render(request,"contractorprequest.html",{"data":data})



############view Approved Videos

#############################
def customerpvideo(request):
    """ 
        The function for request for design
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s1="select tbldesignrequest.dreqId,tbldesigner.dName,tblvideo.video,tblvideo.video,tblvideo.videoId,tblvideo.amount,tblplan.plan from tbldesignrequest,tbldesigner,tblvideo,tblplan where tbldesignrequest.dreqId=tblplan.reqid and tbldesignrequest.dreqId=tblvideo.dreqId and tbldesignrequest.dEmail=tbldesigner.dEmail and tbldesignrequest.planId in(select planId from tblplan where reqId in(select reqId from tblrequirement where cEmail='"+email+"')) "
    print(s1)
    c.execute(s1)
    data=c.fetchall()
    
    print("*"*300)
    print(data)
    print("*"*300)

    s="select tbldesignrequest.dreqId,tbldesigner.dName,tblvideo.video,tblvideo.videoId from tbldesignrequest,tbldesigner,tblvideo where tbldesignrequest.dreqId=tblvideo.dreqId and tbldesignrequest.dEmail=tbldesigner.dEmail and tbldesignrequest.planId in(select planId from tblplan where reqId in(select reqId from tblrequirement where cEmail='"+email+"')) "
    c.execute(s)
    data1=c.fetchall()
    return render(request,"customerpvideo.html",{"data":data})




def paymentplan(request):
    alert=''
    id=''
    fees=request.session['fees']
    uid=request.session['email']
    s="Select * from account where u_id='"+uid+"'"
    c.execute(s)
    data=c.fetchone()
    bal=data[8]
    print("hellooooooo",fees)
    newbal=int(bal)-int(fees)
    dcvv=data[5]
    print(dcvv)
    msg=''
    if request.GET.get("id"):
        id=request.GET.get("id")
        print(id)
        msg="plan"
        pid=id
        request.session['pid']=pid
        print(pid)
    if request.GET.get("amount"):
        amount=request.GET.get("amount")
        # print(id)
        msg="video"
       
    print(msg)
    if request.POST:
        cvv=request.POST.get("cvv")
        print(cvv)
        if int(cvv)==int(dcvv):
            if msg=='plan':
                d="update account set bal='"+str(newbal)+"' where u_id='"+str(uid)+"'"
                c.execute(d)
                db.commit()
                url="customerviewdesigner"
                return HttpResponseRedirect("/"+url+"?id="+pid)
            else:
                print("msg not found")
            if msg=='video':
                d="update account set bal='"+str(newbal)+"'"
                c.execute(d)
                db.commit()
                url="customerselectcontractor"
                return HttpResponseRedirect(url)


        else:
            alert="incorrect Cvv"
            s="Select * from account where u_id='"+uid+"'"
            c.execute(s)
            data=c.fetchone()
            # return render(request,"paymentindex.html",{"data":data,"fees":fees,"a"})



    return render(request,"paymentindex.html",{"data":data,"fees":fees,"msg":alert,"id":id})



def upipayment(request):
    alert=''
    id=''
    pid=""
    fees=request.session['fees']
    uid=request.session['email']
    ppid=request.session['pid']
    s="Select * from account where u_id='"+uid+"'"
    c.execute(s)
    data=c.fetchone()
    bal=data[8]
    print("hellooooooo",fees)
    newbal=int(bal)-int(fees)
    dcvv=data[5]
    print(dcvv)
    msg=''
    if request.GET.get("id"):
        id=request.GET.get("id")
        print(id)
        msg="plan"
        pid=id
        print(pid)
    if request.POST:
        
        
        if pid==ppid:
                d="update account set bal='"+str(newbal)+"' where u_id='"+str(uid)+"'"
                c.execute(d)
                db.commit()
                url="customerviewdesigner"
                return HttpResponseRedirect("/"+url+"?id="+pid)
        else:
                d="update account set bal='"+str(newbal)+"'"
                c.execute(d)
                db.commit()
                url="customerselectcontractor"
                return HttpResponseRedirect(url)


    return render(request,"upipayment.html")



##########view account details#########
def viewaccount(request):
    uid=request.session['email']
    s="Select * from account where u_id='"+uid+"'"
    c.execute(s)
    data=c.fetchone()
    return render(request,"customerviewaccount.html",{"data":data})


def designerviewwork(request):
    email=request.session["email"]
    s="select tbldesignrequest.dreqId,tbldesigner.dName,tblvideo.video,tblvideo.video,tblvideo.videoId,tblvideo.amount,tblplan.plan from tbldesignrequest,tbldesigner,tblvideo,tblplan where tbldesignrequest.dreqId=tblplan.reqid and tbldesignrequest.dreqId=tblvideo.dreqId and tbldesignrequest.dEmail=tbldesigner.dEmail and tbldesignrequest.dreqStatus='video uploaded' and tbldesignrequest.dEmail='"+str(email)+"'"
    print(s)
    c.execute(s)
    data=c.fetchall()
    print("*"*90)
    print(data)
    print("@"*90)
    return  render(request,"dviewvideo.html",{"data":data})


##############edit req


def editreq(request):
    reqid=request.GET.get("reqid")
    s1="Select * from tblrequirement where reqid='"+reqid+"'"
    c.execute(s1)
    data1=c.fetchone()
    if request.POST:
        t1=request.POST.get("t1")
        t2=request.POST.get("t2")
        t3=request.POST.get("t3")
        t4=request.POST.get("t4")
        t5=request.POST.get("t5")
        t6=request.POST.get("t6")
        t7=request.POST.get("t7")
        t8=request.POST.get("t8")
        t9=request.POST.get("t9")
        t10=request.POST.get("t10")
        e="update tblrequirement set bedroom='"+str(t1)+"',bathroom='"+str(t2)+"',attached='"+str(t3)+"',carporch='"+str(t4)+"',kitchen='"+str(t5)+"',sitout='"+str(t6)+"',workarea='"+str(t7)+"',floor='"+str(t8)+"',sqft='"+str(t9)+"',other='"+str(t10)+"'  where reqid='"+str(reqid)+"'"
        c.execute(e)
        db.commit()
        return HttpResponseRedirect("/customerrequirement")

    return  render(request,"editreq.html",{"data":data1})


