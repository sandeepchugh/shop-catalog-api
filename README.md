# Shop - Catalog Api
A fictional online shop product catalog api

## What is this?

This is the product catalog api of the shopping website. The api uses the following technologies
- Python
- Flask
- Postgres Database (Docker Container)
- Kubernetes/Minikube
- Istio

The Api is used to retrieve product list by category and product details by sku

## How does this work?
Get all products in catalog
```
GET /api/v1/catalog/products
```


Get Product Details By Id
```
GET /api/v1/catalog/products/{product_id}
```

## How is this run in a development environment?
The api is build using flask

```shell script
cd web

# set the flask app
export FLASK_APP=src/app.py

# run the dev server
python manage.py run

# call the web
curl  http://127.0.0.1:5000/api/v1/catalog/products
# response is collection of products
```

or run using docker compose
```shell script
docker-compose build
docker-compose up -d
```
and to shut down 
```shell script
docker-compose down 
```

## How is this deployed?

### Build the image
```shell script
# Docker file is in web folder so use context
# as ./web instead of .
docker build -t shop-catalog-api ./web 
```

### Deploy to minikube
#### Install Minikube
Installing minikube - https://kubernetes.io/docs/tasks/tools/install-minikube/

#### Install VirtualBox
https://download.virtualbox.org/virtualbox/6.1.12/VirtualBox-6.1.12-139181-OSX.dmg

#### Start minikube using virtualbox

https://minikube.sigs.k8s.io/docs/drivers/virtualbox/

```shell script
minikube start --driver=virtualbox
```

#### Install and configure Istio
https://istio.io/latest/docs/setup/getting-started/


## References
https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/
https://dredd.org/en/latest/
https://docs.traefik.io
https://docs.traefik.io/user-guides/docker-compose/acme-tls/