app.build:
	docker build --tag 'to-do-app' . 

app.run:
	docker run -it to-do-app 

app.code_style:
	docker run -it to-do-app pylint main.py
