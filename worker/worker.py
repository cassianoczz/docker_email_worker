from email import message_from_binary_file
import queue
import redis
import json
import os
from time import sleep
from random import randint

if __name__ == '__main__':
    redis_host = os.getenv('REDIS_HOST')
    r = redis.Redis(host=redis_host, port=6379, db=0 )
    print('Aguardando recebimento de Emails...')
    while True:
        mensagem = json.loads(r.blpop('sender')[1])
        print('Enviando o email', mensagem['assunto'])
        sleep(randint(15,45))
        print('Email', mensagem['assunto'], 'enviada')