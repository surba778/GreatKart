import os

os.environ["DATABASE_URL"] = "postgres://seqpjplrxblhjx:c60ed82730a965cf2ab0ec98e59b8a61eb10d4a50b5e075d0eb3699a725383a1@ec2-54-246-185-161.eu-west-1.compute.amazonaws.com:5432/da4456msaspsor"
os.environ["SECRET_KEY"] = "R2IQsZl2Lw"
os.environ["DEVELOPMENT"] = "True"
os.environ["USE_AWS"] = "True"
os.environ["DISABLE_COLLECTSTATIC"] = "1"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = "True"
