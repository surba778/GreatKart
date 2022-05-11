import os

os.environ["DATABASE_URL"] = "postgres://fwzdbsstqlirbn:6b3cd8b429d72e4fcb04f2f061c9e2f91d784b6d21c3b29012c363b6c68ccae9@ec2-99-80-170-190.eu-west-1.compute.amazonaws.com:5432/d9erhijfve6vbi"
os.environ["SECRET_KEY"] = "randomSecretKey2023"
os.environ["DEVELOPMENT"] = "True"
os.environ["USE_AWS"] = "True"
os.environ["DISABLE_COLLECTSTATIC"] = "1"
