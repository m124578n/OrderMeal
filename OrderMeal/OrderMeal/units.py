import jwt
import time
from django.http import JsonResponse


JWT_TOKEN_EXPIRE_TIME = 3600 * 2  # token有效时间 2小时
JWT_SECRET = 'abc'   # 加解密密钥
JWT_ALGORITHM = 'HS256'  # 加解密算法


def generate_jwt_token(user_id: int) -> str:
    payload = {'user_id': user_id, 'exp': int(time.time()) + JWT_TOKEN_EXPIRE_TIME}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token


def verify_jwt(func):
    def wrap(request, *args, **kwargs):
        try:
            auth = request.headers["Authorization"]
            token = auth.split(" ")[1]
            _payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            user_id = _payload.get("user_id")
            exp = int(_payload.pop('exp'))
            if time.time() > exp:
                raise
            return func(request, user_id, *args, **kwargs)
        except:
            return JsonResponse({"status" : 404})
    return wrap
