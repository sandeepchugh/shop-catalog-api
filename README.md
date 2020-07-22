# Shop - Catalog Api
A fictional online shop product catalog api

## What is this?

This is a the product catalog api of the shopping website. The api uses the following technologies
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

The project uses terraform to deploy the resources and depencencies in AWS.

Install terraform in your local machine or build server using terraform cli https://www.terraform.io/downloads.html

Terraform uses the aws provider to interact with aws services. More details on the aws provider are available at https://www.terraform.io/docs/providers/aws/index.html

Note: Add ZoneId in terraform/*.tfvars

### IAC (Terraform)

DEVELOPMENT
```
terraform init -backend-config dev.tfbackend
terraform plan -var-file dev.tfvars
terraform apply -var-file dev.tfvars
```

PRODUCTION
```
terraform init -backend-config prod.tfbackend
terraform plan -var-file prod.tfvars
terraform apply -var-file prod.tfvars
```
