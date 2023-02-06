# Python Anywhere

---

## ALLOWED HOSTS

```python
ALLOWED_HOSTS='USER.pythonanywhere.com'
```

---

## Banco de dados

### MySQL

#### Dependências

###### Arch Linux

```bash
sudo pacman -S \
python-mysqlclient
```

###### Fedora

```bash
sudo dnf install \
python3-devel \
mysql-devel
```

##### Ubuntu

```bash
sudo apt install \
python3-dev \
default-libmysqlclient-dev \
build-essential
```

Instalar dentro do ambiente virtual o pacote `mysqlclient`:

```bash
pip install mysqlclient
```

> `poetry add mysqlclient`.

#### Django environ

Variável de ambiente ou arquivo .env:

```env
DATABASE_URL='mysql://USER:SENHA@USER.mysql.pythonanywhere-services.com:3306/DATABASE-NAME'
```

Arquivo `settings.py`:

```python
DATABASES = {
    'default': env.db(),
    'OPTIONS': {
        'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"',
        'charset': 'utf8mb4',
    },
}
```

#### Django

Arquivo `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'USER$DATABASE-NAME',
        'USER': 'USER',
        'PASSWORD': 'PASSWORD',
        'HOST': 'USER.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    },
    'OPTIONS': {
        'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"',
        'charset': 'utf8mb4',
    },
}
```

---

## Tab WEB

![Python Anywhere tab WEB](./images/pythonanywhere.webp "Python Anywhere tab WEB")

---
