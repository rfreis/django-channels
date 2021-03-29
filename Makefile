local-bash:
	docker exec -it django-chat /bin/bash

logs:
	docker logs --follow django-chat

start-local:
	docker-compose up -d

stop:
	docker stop django-chat
	docker stop django-chat-db
