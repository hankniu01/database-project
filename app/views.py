from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from app import models
from app.models import Review
from django.shortcuts import render
from django.http import HttpResponse   #通过url显示执行效果，则需要导入此模块
from django.db import connection

def time(request):
    print(connection.queries)
    a = connection.queries
    time = a.get(u'time')
    return render(request,'query.html',{"time":time})


 #插入函数
def insert(request):
    if request.method == "POST":
        reviewid= request.POST.get("reviewid",None)
        userid = request.POST.get("userid", None)
        businessid = request.POST.get("businessid", None)
        stars = request.POST.get("stars")
        date = request.POST.get("date", None)
        text = request.POST.get("text", None)

        twz = models.Review.objects.create(review_id =reviewid, user_id = userid, business_id=businessid,stars=stars,date=date,text=text)
        twz.save()
    review_list = models.Review.objects.all()
    return render(request, 'insert.html', {"review_list": review_list})
    # return render(request,'insert.html')


#定义展示函数
# def show(request):
#     review_list = models.Review.objects.all()
#     return render(request, 'insert.html', {"review_list":review_list})
#  & businessid & stars & date & text

def query(request):
    # if request.method == "POST":
    getreviewid= request.POST.get("reviewid", None)
    userid = request.POST.get("userid", None)
    businessid = request.POST.get("businessid", None)
    stars = request.POST.get("stars",None)
    date = request.POST.get("date", None)
    text = request.POST.get("text", None)
    # getreviewid = request.POST.get("code",None)
    # getreviewid = eval(getreviewid)
    print(connection.queries)
    a = connection.queries
    print(a)
    # time = a[len(a)-1].get(u'time')
    print(getreviewid)
    if getreviewid == None:
        review_list = models.Review.objects.all()
        return render(request, 'query.html', {"review_list": review_list},{"time": time})
    # if getreviewid:
    #     review_list = models.Review.objects.filter(review_id__icontains=getreviewid)
    #     return render(request, 'query.html', {'review_list': review_list})
    #     if userid:
    #         review_list = models.Review.objects.filter(Q(review_id__icontains=getreviewid) & Q(user_id__icontains=userid))
    #         return render(request, 'query.html', {'review_list': review_list})
    else:
        review_list = models.Review.objects.filter(review_id__icontains=getreviewid).filter(user_id__icontains=userid).filter(business_id__icontains=businessid).filter(stars__icontains=stars).filter(date__icontains=date).filter(text__icontains=text)
        return render(request,'query.html',{'review_list':review_list},{"time":time})



    # return render(request, 'query.html', {"time": time})


def delete(request):
    getreviewid = request.POST.get("reviewid", None)
    userid = request.POST.get("userid", None)
    businessid = request.POST.get("businessid", None)
    stars = request.POST.get("stars",None)
    date = request.POST.get("date", None)
    text = request.POST.get("text", None)
    print(stars)
    if getreviewid == None:
        review_list = models.Review.objects.all()
        return render(request, 'delete.html', {"review_list": review_list})
    else:
        models.Review.objects.filter(review_id__icontains=getreviewid).filter(user_id__icontains=userid).filter(business_id__icontains=businessid).filter(stars__icontains=stars).filter(date__icontains=date).filter(text__icontains=text).delete()
        review_list = models.Review.objects.all()
        return render(request, 'delete.html', {"review_list": review_list})
        # return render(request,'delete.html',{'review_list':review_list})

    #     models.Review.objects.filter(review_id=reviewid).delete()
    #     models.Review.objects.filter(review_id=reviewid).delete()
    #     models.Review.objects.filter(review_id=reviewid).delete()
    #     models.Review.objects.filter(review_id=reviewid).delete()
    #     models.Review.objects.filter(review_id=reviewid).delete()
    #     models.Review.objects.filter(review_id=reviewid).delete()
    #
    # review_list = models.Review.objects.all()
    # return render(request, 'delete.html', {"review_list": review_list})


def update(request):
    getreviewid = request.POST.get("reviewid", None)
    userid = request.POST.get("userid", None)
    businessid = request.POST.get("businessid", None)
    stars = request.POST.get("stars",None)
    date = request.POST.get("date", None)
    text = request.POST.get("text", None)
    getreviewid1 = request.POST.get("reviewid1", None)
    userid1 = request.POST.get("userid1", None)
    businessid1 = request.POST.get("businessid1", None)
    stars1 = request.POST.get("stars1", None)
    date1 = request.POST.get("date1", None)
    text1 = request.POST.get("text1", None)
    print(getreviewid)
    print(text1)
    if getreviewid == None:
        review_list = models.Review.objects.all()
        return render(request, 'update.html', {"review_list": review_list})
    else:
        list1 = [getreviewid1,userid1,businessid1,stars1,date1,text1]
        list2 = ['review_id','user_id','business_id','stars','date','text']
        i = 0
        review_list = models.Review.objects.all()
        isinstance(review_list, list)
        for value in list1:
            if value:
                keyword = list2[i]
                if keyword == 'review_id':
                    review_list = models.Review.objects.filter(review_id__icontains=getreviewid).filter(
                        user_id__icontains=userid).filter(business_id__icontains=businessid).filter(
                        stars__icontains=stars).filter(
                        date__icontains=date).filter(text__icontains=text).update(review_id=value)
                if keyword == 'user_id':
                    review_list = models.Review.objects.filter(review_id__icontains=getreviewid).filter(
                        user_id__icontains=userid).filter(business_id__icontains=businessid).filter(
                        stars__icontains=stars).filter(
                        date__icontains=date).filter(text__icontains=text).update(user_id=value)
                if keyword == 'business_id':
                    review_list = models.Review.objects.filter(review_id__icontains=getreviewid).filter(
                        user_id__icontains=userid).filter(business_id__icontains=businessid).filter(
                        stars__icontains=stars).filter(
                        date__icontains=date).filter(text__icontains=text).update(business_id=value)
                if keyword == 'stars':
                    review_list = models.Review.objects.filter(review_id__icontains=getreviewid).filter(
                        user_id__icontains=userid).filter(business_id__icontains=businessid).filter(
                        stars__icontains=stars).filter(
                        date__icontains=date).filter(text__icontains=text).update(stars=value)
                if keyword == 'date':
                    review_list = models.Review.objects.filter(review_id__icontains=getreviewid).filter(
                        user_id__icontains=userid).filter(business_id__icontains=businessid).filter(
                        stars__icontains=stars).filter(
                        date__icontains=date).filter(text__icontains=text).update(date=value)
                if keyword == 'text':
                    review_list = models.Review.objects.filter(review_id__icontains=getreviewid).filter(
                        user_id__icontains=userid).filter(business_id__icontains=businessid).filter(
                        stars__icontains=stars).filter(
                        date__icontains=date).filter(text__icontains=text).update(text=value)

            i += 1
        review_list = models.Review.objects.all()
        return render(request, 'update.html', {'review_list': review_list})
#     if request.method == "POST":

#         models.Review.objects.filter(review_id=reviewid).update(userid='')
#
#     review_list = models.Review.objects.all()
#     return render(request, 'update.html', {"review_list": review_list})