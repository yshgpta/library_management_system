from django.shortcuts import render

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from library.models import Book, Add_No, StudentProfile, Semester_Book
from django.contrib.auth.models import User
from django.core.mail import send_mail
from Library_management_system.settings import EMAIL_HOST_USER
from library.forms import UserForm, StudentProfileForm
from django.http import JsonResponse


from datetime import date,timedelta
import re
import time
import requests
import json




# Create your views here.
g_i_book=[]
count_book=0
issue_day_limit = 15 #Edit max limit to issue book
per_day_fine = 10

def index(request):
    new_books = Book.objects.all()[:10]
    n_booklist = []
    for n_book in new_books:
        b_isbn = n_book.isbn
        try:
            book_url = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + str(b_isbn)
            response = requests.get(book_url)
            result = json.loads(response.text)
        except:
            return HttpResponse("Connection error.")
        
        if result['totalItems']:
            book = result['items'][0]['volumeInfo']
            b_imagelink = book['imageLinks']['thumbnail']
            n_booklist.append([b_isbn,b_imagelink])
    user_form = UserForm()
    std_profile_form = StudentProfileForm()
    return render(request, 'home.html',{'new_books':n_booklist,'user_form': user_form,'std_profile_form':std_profile_form})

# ----------------------------------------------------------------------------

# STUDENT OPERATIONS

@login_required
def delete_issue(request):
    global count_book
    if request.method == 'POST':
        book_no = request.POST.get('b_info')
        print(book_no)
        user_book_info = Add_No.objects.get(book_no=book_no)
        i_book = []
        i_book.append(book_no)
        i_book.append(user_book_info.book_name)
        g_i_book.remove(i_book)
        count_book = len(g_i_book)
    return user_login_success(request,g_i_book)

@login_required
def renewal(request):
    if request.method == 'POST':
        book_no = request.POST.get('b_info')
        print(book_no)
        user_book_info = Add_No.objects.get(book_no=book_no)
        if user_book_info.reissue_cycle >= 4:
            return user_login_success(request)
        else:
            message = request.user.first_name +" "+ request.user.last_name + " ("+request.user.username+") \n\n"
            message = message + "Following book has been Renewed out: \n\n"
            user_book_info.reissue_cycle +=1
            user_book_info.save()
            message = message + "Renewal Date: "+str(date.today()) +" | Book No: "+book_no+" | Title: "+user_book_info.book_name.title+" | Author: "+user_book_info.book_name.author+" | Due Date : "+str(date.today() + timedelta(days = issue_day_limit))+".\n\n"
            subject = 'IIITL Library Renewals'
            message = message + 'Circulation Desk | Library IIIT Lucknow.'
            recepient = request.user.email
            print(message)
            send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    return user_login_success(request)

@login_required
def checkout(request):
    if request.method == 'POST':
        global g_i_book
        t = StudentProfile.objects.filter(user = request.user)
        std_prof = StudentProfile.objects.get(user = request.user)
        # print(t)
        # print(g_i_book)
        message = request.user.first_name +" "+ request.user.last_name + " ("+request.user.username+") \n\n"
        message = message + "Following book/s has been checked out: \n\n"
        flag = [True,True,True,True]
        for book_info in g_i_book:
            book_no = book_info[0]
            user_book_info = Add_No.objects.get(book_no=book_no)
            user_book_info.availability='I'
            user_book_info.assigned_to = std_prof
            user_book_info.save()
            print(user_book_info.issued_on)
            message = message + "Issue Date: "+str(user_book_info.issued_on) +" | Book No: "+book_no+" | Title: "+user_book_info.book_name.title+" | Author: "+user_book_info.book_name.author+" | Due Date : "+str(user_book_info.issued_on + timedelta(days = issue_day_limit))+".\n\n"
            # print(book_no)
            if not request.user.studentprofile.book1 and flag[0]:
                t.update(book1=book_no)
                flag[0] = False
            elif not request.user.studentprofile.book2 and flag[1]:
                t.update(book2=book_no)
                flag[1] = False
            elif not request.user.studentprofile.book3 and flag[2]:
                t.update(book3=book_no)
                flag[2] = False
            elif not request.user.studentprofile.book4 and flag[3]:
                t.update(book4=book_no)
                flag[3] = False
            
        g_i_book = []
        subject = 'IIITL Library Checkouts'
        message = message + 'Circulation Desk | Library IIIT Lucknow.'
        recepient = request.user.email
        print(message)
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)

    return user_login_success(request)


@login_required
def issue_book(request):
    message=''
    global count_book
    print('count'+str(count_book))
    if count_book < 4:
        if request.method == 'POST':
            book_no = request.POST.get('book_no')
            # print(book_no)
            try:
                user_book_info = Add_No.objects.get(book_no=book_no)
            except ObjectDoesNotExist:
                print("Object does not exist.")
                message="Please input a valid book number."
                return user_login_success(request,g_i_book,message)
                
            if user_book_info.availability == 'I':
                message = 'Book is already Issued.'
            else:
                i_book = []
                i_book.append(book_no)
                i_book.append(user_book_info.book_name)
                if i_book in g_i_book:
                    message = 'Cannot add duplicate entry.'
                else:
                    g_i_book.append(i_book)
                count_book = len(g_i_book)
    else:
        count_book = len(g_i_book)
        message = 'You cannot add more than 4 books.'
    return user_login_success(request,g_i_book,message)


# ------------------------------------------------------------------------------------

# ADMIN OPERATIONS

@login_required
def get_book_info(user_book):
    res = []
    global count_book
    usr_books = [user_book.book1,user_book.book2,user_book.book3,user_book.book4]
    for usr_book in usr_books:
        if usr_book:
            count_book+=1
            b_no = usr_book
            user_book_info = Add_No.objects.get(book_no=b_no)
            day_diff = date.today() - user_book_info.issued_on
            day_left = issue_day_limit - day_diff.days
            lst = []
            lst.append(usr_book)
            lst.append(user_book_info.book_name)
            lst.append(day_left)
            fine=''
            if day_left<0:
                fine = abs(day_left)*per_day_fine
            lst.append(fine)
            reissue_count=''
            if user_book_info.reissue_cycle < 4:
                reissue_count = user_book_info.reissue_cycle
            print(reissue_count)
            lst.append(reissue_count)
            res.append(lst)

    return res

# ----------------------------------------------------------------------------------

# RETURN BOOK

@login_required
def return_book(request):
    message_failure =''
    message_success =''
    if request.method == 'POST':
        book_no = request.POST.get('book_no')
        try:
            book_info = Add_No.objects.get(book_no=book_no)
        except ObjectDoesNotExist:
            message_failure = "Please Enter a valid book number."
            print("Return Object do not exist.")
            return render(request,'adminpage.html',{'message_success':message_success,'message_failure':message_failure})

        if not book_info.assigned_to:
            return HttpResponse('The book is not issued to anyone')

        day_diff = date.today() - book_info.issued_on
        day_left = issue_day_limit - day_diff.days

        if day_left<0:
            fine = abs(day_left)*per_day_fine
            message_failure = "User have fine of Rs."+str(fine)+" on this book."

        user_having = book_info.assigned_to
        book_info.availability = 'A'
        book_info.assigned_to = None
        book_info.reissue_cycle = 1
        book_info.save()
        if user_having.book1 == book_no:
            user_having.book1=''
            user_having.save()
        elif user_having.book2 == book_no:
            user_having.book2=''
            user_having.save()
        elif user_having.book3 == book_no:
            user_having.book3=''
            user_having.save()
        elif user_having.book3 == book_no:
            user_having.book3=''
            user_having.save()
        else:
            return HttpResponse('Invalid Operation')
        message_success = "The book has been returned successfully."
        message = user_having.user.first_name +" "+ user_having.user.last_name + " ("+user_having.user.username+") \n\n"
        message = message + "Following book has been Returned: \n\n"
        message = message + "Returned Date: "+str(date.today()) +" | Book No: "+book_no+" | Title: "+book_info.book_name.title+" | Author: "+book_info.book_name.author+".\n\n"
        subject = 'IIITL Library Return'
        message = message + 'Circulation Desk | Library IIIT Lucknow.'
        recepient = user_having.user.email
        print(message)
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    return render(request,'adminpage.html',{'message_success':message_success,'message_failure':message_failure})


def get_all_user(request):
    all_user = StudentProfile.objects.all()
    fine=[]
    print(all_user)
    for usr in all_user:
        if usr.user.is_superuser:
            continue
        l = []
        l.append(usr.user.username)
        total_fine = 0
        c = 0
        b_l =[]
        usr_book = [usr.book1,usr.book2,usr.book3,usr.book4]
        for usr_b in usr_book:
            if usr_b:
                c+=1
                b_list = []
                b_list.append(usr_b)
                b_no = Add_No.objects.get(book_no = usr_b)
                day_diff = date.today() - b_no.issued_on
                day_left = issue_day_limit - day_diff.days
                f = 0
                if day_left<0:
                    f = abs(day_left)*per_day_fine
                b_list.append(f)
                b_l.append(b_list)
                total_fine += f

        l.append(b_l)
        l.append(total_fine)
        l.append(c)
        if c!=0:
            fine.append(l)
        # if total_fine != 0:
        #     fine.append(l)
    print(fine)
    return admin_login_success(request,fine)
# ---------------------------------------------------------------------------

# ADMIN LOGIN
@login_required
def admin_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def admin_login_success(request,t_fine=[]):
    user = request.user
    print(user.is_superuser)
    return render(request,'adminpage.html',{'user':user,'fine':t_fine})

def superuser_login(request):
    if request.method == 'POST':
        username = request.POST.get('admin_username')
        password = request.POST.get('admin_password')
        admin = authenticate(username=username,password=password)
        if admin:
            if admin.is_active and admin.is_superuser:
                login(request,admin)
                print("Superuser")
                return HttpResponseRedirect(reverse('admin_login'))
            else:
                print("Not a superuser")
                return HttpResponse('You are not Superuser.')
        else:
            print("Failed to login")
            return HttpResponse("Invalid admin login detail")
    else:
        return render(request,'home.html')

# -------------------------------------------------------------------

def recommended_book(r_book):
    isbns = [r_book.book1_isbn,r_book.book2_isbn,r_book.book3_isbn,r_book.book4_isbn,r_book.book5_isbn,r_book.book6_isbn,r_book.book7_isbn,r_book.book8_isbn,r_book.book9_isbn,r_book.book10_isbn,r_book.book11_isbn,r_book.book12_isbn,]
    lst = []
    r_lst = []
    count=0
    for isbn in isbns:
        count+=1
        if isbn:
            try:
                book_url = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + str(isbn)
                response = requests.get(book_url)
                result = json.loads(response.text)
            except:
                return HttpResponse("Connection error.")
            if result['totalItems']:
                book = result['items'][0]['volumeInfo']
                b_imagelink = book['imageLinks']['thumbnail']
                lst.append([isbn,b_imagelink])
                if count%6 == 0:
                    r_lst.append(lst)
                    lst = []
    return r_lst


# STUDENT LOGIN
@login_required
def user_login_success(request,i_book=[],message=''):
    
    user = request.user
    user_book = StudentProfile.objects.get(user=user)
    if not i_book:
        global g_i_book
        g_i_book=[]
        global count_book
        count_book=0

    book_info = get_book_info(user_book)
    roll_no = user.username
    curr_year = date.today().year
    curr_month = date.today().month
    find_sem = (curr_year - int(roll_no[3:7]))*2
    if curr_month>6:
        find_sem = find_sem+1
    r_book = Semester_Book.objects.get(semester = 'Semester-'+str(find_sem))
    b_recommend = recommended_book(r_book)
    if message:
        print(message)
    return render(request,'loggeduser.html',{'user':user,'curr_sem':find_sem,'book_info':book_info,'i_book':i_book,'b_recommend':b_recommend,'message':message})

@login_required
def std_logout(request):
    logout(request)
    global g_i_book
    g_i_book = []
    return HttpResponseRedirect(reverse('home'))

def std_login(request):
    if request.method == 'POST':
        roll_no = request.POST.get('roll_no')
        alpha = roll_no[:3].upper()
        numeric = roll_no[3:]
        normalized_roll_no = alpha + numeric
        password = request.POST.get('password')
        print("Roll No : {} Password: {}".format(normalized_roll_no,password))
        
        std = authenticate(username = normalized_roll_no, password=password)
        if std:
            print("Logged in")
            if std.is_active:
                login(request,std)
                return HttpResponseRedirect(reverse('user_login'))
            else:
                HttpResponse("Account not active")
        else:
            print("Failed to logging")
            return HttpResponse("Invalid login detail")
    else:
        return render(request,'home.html')

# --------------------------------------------------------------------

# STUDENT REGISTRATION

def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        std_profile_form = StudentProfileForm(request.POST)
        if user_form.is_valid() and std_profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            std_profile = std_profile_form.save(commit=False)
            std_profile.user = user
            std_profile.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse("User already exist.")
    else:
        user_form = UserForm()
        std_profile_form = StudentProfileForm()
    return render(request, 'home.html', {'user_form': user_form,'std_profile_form':std_profile_form})

# ----------------------------------------------------------------------

# SEARCH SECTION

def normalize_query(query_string, findterms=re.compile(r'"([^"]+)"|(\S+)').findall, normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, field_name):
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        q = Q(**{"%s__icontains" % field_name: term})
        if or_query is None:
            or_query = q
        else:
            or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def search_book(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        search_by = request.GET['search-by']

        entry_query = get_query(query_string, search_by)

        b_list= Book.objects.filter(entry_query)
        book_list =[]
        if b_list:
            for i in b_list:
                print(i.isbn)
                q = Q(**{"%s__icontains" % 'book_name__isbn' : i.isbn})
                book_info = Add_No.objects.filter(q)
                for j in book_info:
                    lst = []
                    lst.append(i)
                    lst.append(j)
                    print(j.availability)
                    book_list.append(lst)
        

    return render(request,'book_list.html',{'book_list':book_list})

def book_detail(request):
    if 'isbn_no' in request.GET:
        isbn_no = request.GET['isbn_no']
        print("isbn_no"+str(isbn_no))
        try:
            book_url = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + str(isbn_no)
            response = requests.get(book_url)
            result = json.loads(response.text)
        except:
            return HttpResponse("Connection error.")
        b_details = []
        if result['totalItems']:
            book = result['items'][0]['volumeInfo']
            b_title = book['title']
            b_authors = book['authors']
            b_description = book['description']
            b_isbn = [book['industryIdentifiers'][0]['identifier'],book['industryIdentifiers'][1]['identifier']]
            b_categories = book['categories']
            b_imagelink = book['imageLinks']['thumbnail']
            b_language = book['language']
            b_details = [b_imagelink,b_title,b_authors,b_isbn,b_categories,b_language,b_description]
    return render(request,'book_detail.html',{'b_details':b_details})


# ---------------------------------------------------------------------------------
