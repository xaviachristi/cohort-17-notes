provider "aws" {
    region = var.AWS_REGION
    access_key = var.AWS_ACCESS_KEY
    secret_key = var.AWS_SECRET_KEY
}

data "aws_vpc" "current-vpc" {
    id = "vpc-00b3f6b2893c390f2"
}

data "aws_db_subnet_group" "subnet-group" {
    name = "c17-public-subnet-group"
}

resource "aws_instance" "example" {
  ami           = "ami-0dfe0f1abee59c78d"
  instance_type = "t2.nano"
  subnet_id     = data.aws_db_subnet_group.subnet-group.id

  cpu_options {
    core_count       = 1
    threads_per_core = 1
  }

  tags = {
    Name = "ec2-example"
  }
}