# Flask Blog Application

- [Flask Blog Application](#flask-blog-application)
  - [Introduction](#introduction)
  - [Secret Generation](#secret-generation)

## Introduction

This repository contains code for building a basic blog application using Flask.

## Secret Generation

You can leverage the `secrets` library to generate a secret.

```bash
echo -e "import secrets\nprint(secrets.token_hex(16))" | python
6f303dff8c5bc7c4c32870f598d2dfe9
```
