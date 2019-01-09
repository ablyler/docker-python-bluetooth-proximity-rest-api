FROM python:3-alpine

RUN apk upgrade --no-cache

WORKDIR /usr/src/app

COPY . .
COPY requirements.txt ./

RUN apk add --no-cache bluez bluez-dev \
	&& apk add --no-cache --virtual build-dependencies build-base \
	&& pip install --no-cache-dir -r requirements.txt \
	&& apk del build-dependencies

CMD [ "flask", "run", "--host=0.0.0.0" ]
