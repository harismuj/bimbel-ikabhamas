from flask import request

def get_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.environ['REMOTE_ADDR']
    else:
        # Jika menggunakan proxy atau load balancer
        return request.environ['HTTP_X_FORWARDED_FOR']

def is_active(endpoint):
    return 'active' if request.endpoint == endpoint else ''

def is_active_partial(endpoint_prefix):
    return 'active' if request.endpoint.startswith(endpoint_prefix) else ''