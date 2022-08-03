import os

os.environ["DATABASE_URL"] = "postgres://okaqqdsybzkziq:0ac79d21ffb4465b49d1afe9b7a5c61e6d0ef78d8a45eca72351fdd78652708d@ec2-3-248-121-12.eu-west-1.compute.amazonaws.com:5432/d9kpdir1i6cpej"
os.environ["SECRET_KEY"] = "randomSecretKey2023"
os.environ["DEVELOPMENT"] = "True"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = "True"
