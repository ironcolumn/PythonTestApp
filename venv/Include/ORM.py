import asyncio,logging,aiomysql


@asyncio.coroutine
def create_pool(loop,**kwargs):
    logging.info('create database connection pool')
    global __pool
    __pool=yield from aiomysql.create_pool(
        host=kwargs.get('host','localhost'),

    )
