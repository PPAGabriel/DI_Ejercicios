import sqlite3 as dbapi
'''
print(dbapi.apilevel)
print(dbapi.threadsafety)
print(dbapi.paramstyle)
'''

bbdd=dbapi.connect("baseDatos.dat")
#print(bbdd)
c=bbdd.cursor()
#print(c)

'''
try:
    c.execute("""create table usuarios(dni text,nome text,edade integer)""")

except dbapi.DataBaseError as e:
    print("Error creando tabla usuarios: "+e)
'''

'''
try:
    c.execute("""insert into usuarios values('3333-a',"Ana Perez",19)""")
    c.execute("""insert into usuarios values('2222-b',"Roque Diaz",56)""")
    c.execute("""insert into usuarios values('1111-c',"Fiz Vidal",37)""")
except dbapi.DatabaseError as e:
    print("Error al insertar usuarios "+e)
'''

try:
    consulta: c.execute("""select dni, nome from alumnos""")
except dbapi.OperationalError as e:
    print("Error en la consulta de usuarios: "+str(e))




