from django.db import connection

def dump_sql():
    '''SQL文をprintする'''
    for sql in map((lambda r: r['sql']), connection.queries[-1:]):
        print(sql)

def dump_pk(model):
    '''modelのpkを表示する'''
    [print('pk:{0.pk}'.format(x)) for x in model]
