# Shop - Catalog Api
A fictional online shop product catalog api

## What is this?

This is the product catalog api of the shopping website. The api uses the following technologies
- Python
- Flask
- Postgres Database (Docker Container)

The Api is used to retrieve product list by category and product details by sku

## How does this work?

Get Products By Category
```
GET /products/{category_name}
```

Get Product Details By Sku
```
GET /products/{sku_id}/details
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

### Install Kubernetes / Minikube
Installing minikube - https://kubernetes.io/docs/tasks/tools/install-minikube/

#### Install VirtualBox
https://download.virtualbox.org/virtualbox/6.1.12/VirtualBox-6.1.12-139181-OSX.dmg

#### Install Minikube
Check if virtualization is supported
```shell script
sysctl -a | grep -E --color 'machdep.cpu.features|VMX'
```

Install minikube
```shell script
brew install minikube
```

Start minikube using virtualbox
https://minikube.sigs.k8s.io/docs/drivers/virtualbox/

```shell script
minikube start --driver=virtualbox
```

Minikube IP
```shell script
minikube ip
```

### Deploy to minikube


### Configure Istio
