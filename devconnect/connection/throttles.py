from rest_framework.throttling import ScopedRateThrottle

class PostCreateThrottle(ScopedRateThrottle):
    scope = 'post_create'


class LoginThrottle(ScopedRateThrottle):
    scope = 'login'