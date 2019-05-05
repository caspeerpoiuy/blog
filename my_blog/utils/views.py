from utils.function import md5_user_id


def jwt_response_payload_handler(token, user=None, request=None):
    user_id = md5_user_id(user.id)
    return {
        "token": token,
        "user_id": user_id,
        "username": user.username
    }