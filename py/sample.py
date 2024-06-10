import os

secret = os.environ.get("VALUE")
print(f"the env variable is {secret}")
