# Django及びDjangoRESTframeworkにおけるシンプルな非同期処理

#### OS: Linux

## パッケージの起動 (Celery beatもインストールすれば使用可能)

#### 仮想環境下で以下を実行

Celery worker

```bash
$ celery -A config worker -l info --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo
```

## 非同期処理の実行

```bash
$ python manage.py runserver
```
