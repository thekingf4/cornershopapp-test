import jwt
from datetime import timedelta
from django.conf import settings
from django.utils import timezone


class Generator:
    @staticmethod
    def gen_token(data: dict, type: str, time: timedelta):
        payload = {
            'type': type
        }

        payload.update(data)

        if time:
            exp_date = timezone.now() + time
            payload.update({
                'exp': int(exp_date.timestamp())
            })

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return token
