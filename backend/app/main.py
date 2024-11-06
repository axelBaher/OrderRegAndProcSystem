import uvicorn
from backend.app import app
from backend.core.config import SSL_KEY_PASSWORD_PATH, SSL_KEY_PATH, SSL_CERT_PATH
import backend.app.models


def read_ssl_key_password() -> str:
    with open(SSL_KEY_PASSWORD_PATH, "r") as f:
        key_password = f.read().strip()
    return key_password


def main():
    uvicorn.run("backend.app:app",
                host="127.0.0.1",
                port=8000,
                ssl_keyfile=SSL_KEY_PATH,
                ssl_certfile=SSL_CERT_PATH,
                ssl_keyfile_password=read_ssl_key_password())


if __name__ == "__main__":
    main()
