# Django

Exemplo de como iniciar um projeto com a linguagem de programação Python e o framework web Django.

---

## fixtures

### Dumpdata

```bash
python manage.py \
dumpdata \
nome-do-app.nome-do-model \
--indent 4 > nome-do-app/fixtures/data.json
```

### Loaddata

```bash
python manage.py \
loaddata \
nome-do-app/fixtures/data.json
```

---

## Internacionalização

Gerar arquivos de tradução (`*.po`):

```bash
django-admin makemessages --all --ignore=env
```

Compilar arquivos de tradução:

```bash
django-admin compilemessages --ignore=env
```

---
