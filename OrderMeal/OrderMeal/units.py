import jwt
import time
from django.http import JsonResponse


JWT_TOKEN_EXPIRE_TIME = 3600 * 2  # token有效時間
JWT_SECRET = 'abc'
JWT_ALGORITHM = 'HS256'


def generate_jwt_token(user_id: int) -> str:
    payload = {'user_id': user_id, 'exp': int(time.time()) + JWT_TOKEN_EXPIRE_TIME}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token


def verify_jwt(func):
    def wrap(request, *args, **kwargs):
        auth = request.headers["Authorization"]
        token = auth.split(" ")[1]
        _payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user_id = _payload.get("user_id", None)
        exp = int(_payload.pop('exp'))
        if time.time() > exp:
            return JsonResponse({"status" : 404})
        return func(request, user_id=user_id, *args, **kwargs)
    return wrap
