from django.shortcuts import render
from django.http import JsonResponse
from staff.models import Staff

import jwt
import json
import time


def index(request):
    context = {}
    return render(request, 'index.html', context)


def login_page(request):
    return render(request, 'login.html')


def store(request):
    pass


def store_menu(request):
    pass


def group(request):
    pass


def login_api(request):
    body = request.body.decode("utf-8")
    body = json.loads(body)
    staff_id = body.get("userId", "")
    password = body.get("passwd", "")
    staff = Staff.objects.filter(staff_id=staff_id)
    if staff is None:
        return JsonResponse({"status" : 404})
    if staff[0].password != password:
        return JsonResponse({"status" : 404})
    token = generate_jwt_token(staff_id)
    return JsonResponse({"status" : 200 , "token" : token})
    

JWT_TOKEN_EXPIRE_TIME = 3600 * 2  # token有效时间 2小时
JWT_SECRET = 'abc'   # 加解密密钥
JWT_ALGORITHM = 'HS256'  # 加解密算法


def generate_jwt_token(user_id: int) -> str:
    payload = {'user_id': user_id, 'exp': int(time.time()) + JWT_TOKEN_EXPIRE_TIME}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

def verify_jwt_token(user_id: int, token: str) -> bool:
    payload = {'user_id': user_id}
    try:
        _payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except jwt.PyJWTError:
        print('token解析失败')
        return False
    else:
        print(_payload)
        exp = int(_payload.pop('exp'))
        if time.time() > exp:
            print('已失效')
            return False
        return payload == _payload