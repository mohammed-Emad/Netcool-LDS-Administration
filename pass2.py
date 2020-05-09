import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import json


key_django = b'75oef^qajr2e+$!d-ssc0i5lcicx0_z$lof8*ek%@bh*c(2*t&'

#---------------------------------your edit-------------------------------------#
DATABASE=    b'GSMALDS'
USER    =    b'db2lds'
PASSWORD=    b'f2WN4k1nf2WN4k1n'
HOST    =    b'db2labserver'
PORT    =    b'60000'
#-------------------------------------------------------------------------------#

data  = b"khuhguktgchytdgtrdsexsrwewqe767565ecdhctrrgtrsxextgrd"
data2  = "khuhguktgchytdgtrdsexsrwewqe767565ecdhctrrgtrsxextgrd"
fileR = 'rrms.json'
def encrypt(key, source, encode=True):
    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    IV = Random.new().read(AES.block_size)  # generate IV
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size  # calculate needed padding
    source += bytes([padding]) * padding  # Python 2.x: source += chr(padding) * padding
    data = IV + encryptor.encrypt(source)  # store the IV at the beginning and encrypt
    return base64.b64encode(data).decode("latin-1") if encode else data




def jjeson(nam,ps,da_name,host,port,django_secret_key,data):
   jjs = {
    "Name": str(nam),
    "DB_PASSWORD": str(ps),
    "DB_Name":  str(da_name),
    "Host": str(host),
    "port": str(port),
    "SECRET_KEY": str(django_secret_key),
    "data_k": str(data)
   }
   return jjs


'''
Namee  = input("Enter user Name db2::")
passw  = input("Enter password db2::")
database_name  = input("Enter name your DATABASES  db2::")
host  = input("Enter your server or host  db2::")
port  = input("Enter your port database db2::")
django_secret_key = input("Enter your SECRET_KEY django or enter [y] to use [75oef^qajr2e+$!d-ssc0i5lcicx0_z$lof8*ek%@bh*c(2*t&]::")
if django_secret_key == 'y':
   django_secret_key = key_django 
'''

Namee = encrypt(data ,USER)
passw = encrypt(data ,PASSWORD)
database_name = encrypt(data ,DATABASE)
host = encrypt(data ,HOST)
port = encrypt(data ,PORT)
django_secret_key = encrypt(data ,key_django)

res = jjeson(Namee,passw,database_name,host,port,django_secret_key,data2)

with open(fileR, 'w') as fdd:
    json.dump(res, fdd)

print("hey encrypted done..")


