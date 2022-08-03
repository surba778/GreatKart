import os

os.environ["DATABASE_URL"] = "postgres://yzdvvzihdserze:063d6ad09dd7d5aa757344e9ce5889919f4d7116ae8ca226e18601d1e7c5fa3b@ec2-176-34-215-248.eu-west-1.compute.amazonaws.com:5432/dak28k1vve1ht7"
os.environ["SECRET_KEY"] = "randomSecretKey2023"
os.environ["DEVELOPMENT"] = "True"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = "True"
