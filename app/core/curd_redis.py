#
# class CurdRedis:
#     def __init__(self, redis_cli, base_key):
#         self.conn = redis_cli
#         self.base_key = base_key
#
#     async def set(self, key, val):
#         return await self.conn.set(f'{self.base_key}:{key}', val)
#
#     async def get(self, key):
#         rv = await self.conn.get(f'{self.base_key}:{key}')
#         return rv
#
#     async def delete(self, key):
#         return await self.conn.delete(f'{self.base_key}:{key}')
#
#     async def exists(self, key):
#         """
#         :param key:
#         :return:
#         """
#         return self.conn.exists(f'{self.base_key}:{key}')


async def auth_set_token(redis_cli, user_id, access_token):
    await redis_cli.set(f'account:token:{user_id}', access_token)


async def auth_get_token(redis_cli, user_id):
    token = None
    rv = await redis_cli.exists(f'account:token:{user_id}')
    if rv:
        token = await redis_cli.get(f'account:token:{user_id}')
    return token


async def auth_del_token(redis_cli, user_id):
    rv = await redis_cli.exists(f'account:token:{user_id}')
    if rv:
        await redis_cli.delete(f'account:token:{user_id}')
