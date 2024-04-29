from django.shortcuts import render
from django.http import HttpResponse
import pyodbc
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
import numpy as np
from datetime import datetime
import pytz
import uuid

def ads(request):
    return HttpResponse("Hello world!")