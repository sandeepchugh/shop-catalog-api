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

Get Products By Category
```
GET /api/v1/products/categories/{category_name}
```

Get Product Details By Id
```
GET /api/v1/products/{product_id}
```

## How is this run in a development environment?
The api is build using flask

```shell script
# set the flask app
export FLASK_APP=src/app.py

# run the dev server
python manage.py run

# call the api
curl  http://127.0.0.1:5000/api/v1/products/categories/test1
# response is [{"name": "my test product", "category": "test1"}]
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

Now that we have a Dockerfile, let’s verify it builds correctly:
```shell script
docker build -t shop-catalog-api:latest .
```

### Run the container
After the build completes, we can run the container:
```shell script
docker run -d -p 5000:5000 shop-catalog-api
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