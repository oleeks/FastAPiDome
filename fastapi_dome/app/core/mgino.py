from gino.ext.starlette import Gino as _Gino

class Gino(_Gino):
    async def set_bind(self, bind, loop=None, **kwargs):
        kwargs.setdefault("strategy", "starlette")

        if bind.drivername.startswith('mysql'):
            kwargs.pop("min_size")
            kwargs.pop("max_size")
            kwargs.setdefault("autocommit", True)
        return await super().set_bind(bind, loop=loop, **kwargs)
