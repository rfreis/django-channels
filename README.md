# Django Channels

Tutorial using Django with channels from [channels documentation](https://channels.readthedocs.io/en/stable/tutorial/part_1.html).

## Requirements

To make this run you must have installed:

* docker
* docker-compose

## Running application

```bash
make start-local
```

## Stopping application

```bash
make stop
```

## Local bash

```bash
make local-bash
```

## Logs

```bash
make logs
```

## Opening the chat

The chat will be available on the routes bellow:

- `localhost:8000/chat/`
- `localhost:8000/chat/<room_name>`
