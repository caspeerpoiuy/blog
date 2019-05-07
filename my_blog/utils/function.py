from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from my_blog import settings


def generate_verify_email_url(id, email):
    serializer = Serializer(settings.SECRET_KEY, 3600)
    token = serializer.dumps(
        {
            "user_id": id,
            "email": email
        }
    )
    verify_url = "127.0.0.1:8000/verify_email.html?token=" + token.decode()
    return verify_url

