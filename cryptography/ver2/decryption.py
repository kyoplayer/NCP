import base64
import hmac
import hashlib

# コンテストで共通の秘密鍵をここに置く
secret = b"MY_SECRET_KEY"

code = input()

payload, sig = code.split(".")

payload += "="*(-len(payload)%4)
sig += "=" * (-len(sig)%4)

msg = base64.urlsafe_b64decode(payload)
recv_sig = base64.urlsafe_b64decode(sig)

calc_sig = hmac.new(secret,msg,hashlib.sha256).digest()

if not hmac.compare_digest(calc_sig, recv_sig):
    print("改ざんされています")
    exit()

dt,alphabet,P = msg.decode().split(":")

print(f"問題: {alphabet} \n 経過時間: {dt} \n 得点: {P}")
