
Scalable Web Cluster with Load Balancing and Monitoring
This project implements a high-availability web cluster using Nginx as a load balancer, multiple FastAPI application replicas, and a complete monitoring stack.

Architecture Components
Load Balancer: Nginx (Round Robin strategy)

Application: FastAPI (3 replicas)

Database: PostgreSQL

Monitoring: Prometheus, cAdvisor, and Grafana

Load Testing: Locust

Prerequisites
Docker

Docker Compose

Installation and Execution
Clone the repository using the specific branch:

Bash
git clone -b features_nginx https://github.com/24024102/my-first-pipeline.git
Navigate to the project directory:

Bash
cd my-first-pipeline
Start all services:

Bash
docker-compose up -d
Service Access
Service	URL	Note
Web Application	http://localhost:80	Use ?name=yourname to write to DB
Locust	http://localhost:8089	Interface for load testing
Grafana	http://localhost:3000	Credentials: admin / admin
Prometheus	http://localhost:9090	Metrics database
cAdvisor	http://localhost:8080	Container resource statistics
Monitoring Setup
Log in to Grafana (port 3000).

Add Prometheus as a Data Source with the URL http://prometheus:9090.

Import Dashboard ID 14282 to visualize container resource usage.

Load Testing
Access the Locust interface (port 8089).

Set the Number of Users and Spawn Rate.

Set the Host to http://nginx.

Start the swarm and observe resource consumption in Grafana.