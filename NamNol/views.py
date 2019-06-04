from django.shortcuts import render
from rest_framework import viewsets
from NamNol.models import Post
from NamNol.serializers import PostSerializer

from django.http import HttpResponse, JsonResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def notice(request):
    chrome_options = ChromeOptions()
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    driver.implicitly_wait(3)
    driver.get('https://nsu.ac.kr/?m1=page%25&menu_id=186%25')
    # By.CSS_SELECTOR로 tr 태그의 notice 클래스가 로딩될때까지 기다린다
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "tr.notice"))
        )

    except TimeoutException:
        print("해당 페이지 오류 !!!")
   
 
    html = driver.page_soure
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select("tbody tr td.tit")
    writer = soup.select("tbody tr td:nth-child(4)")
    date = soup.select("tbody tr td:nth-child(5)")

    dic = {}
    data = {}
    pickup_records = []

    i = 0
    for _title in title:
        pickup_records.append({"title": _title.text, "writer": writer[i].text, "date": date[i].text})
        i+=1

    jsonString = json.dumps(pickup_records)
    
    print(type(jsonString))

    return HttpResponse(jsonString, content_type=('mimetype','application/json'))

# Create your views here.
