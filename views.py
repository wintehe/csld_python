import tornado.ioloop
import tornado.web
from api.member_csld import MemberApi
from api.product_csld import ProductApi

def make_app():

    return tornado.web.Application([
        (r"/info",MemberApi),
        (r"/product", ProductApi),
    ])