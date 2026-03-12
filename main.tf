provider "aws" {
  region = "eu-central-1"
}
resource "aws_key_pair" "my_key" {
    key_name = "devops-key"
    public_key = file("C:/Users/38066/.ssh/aws_key.pub")
}

resource "aws_security_group" "web_sg" {
    name  = "web-server-sg"
    description = "Allow HTT and SSH traffic"


ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
}

ingress {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
}
egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
}

}

data "aws_ami" "ubuntu" {
    most_recent = true
    owners   = ["099720109477"]

    filter {
        name = "name"
        values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
    }
}
resource "aws_instance" "web_server" {
    ami = data.aws_ami.ubuntu.id
    instance_type = "t3.micro"
    key_name = aws_key_pair.my_key.key_name
    vpc_security_group_ids = [aws_security_group.web_sg.id]
    user_data = <<-EQF
                #!/bin/bash
                apt-get update -y
                apt-get install -y docker.io docker-compose
                systemctl start docker
                systemctl enable docker
                usermod -aG docker ubuntu
                EQF
    tags = {
        Name = "My-Docker-serv"
    }
}
output "server_publick_ip" {
    value = aws_instance.web_server.public_ip
}


