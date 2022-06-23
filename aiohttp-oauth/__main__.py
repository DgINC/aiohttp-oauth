import time

from cryptography.fernet import Fernet
from aiohttp import web
from aiohttp_session import get_session, setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage


async def handler(request):
    session = await get_session(request)
    session['last_visit'] = time.time()
    return web.Response(text='OK')


def init():
    app = web.Application()
    key: bytes = Fernet.generate_key()
    f = Fernet(key)
    setup(app, EncryptedCookieStorage(f))
    app.router.add_route('GET', '/', handler)
    return app


web.run_app(init(), host='127.0.0.1', port='8080')
