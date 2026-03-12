# Scalable Web Cluster with Load Balancing and Monitoring

This project implements a high-availability web cluster using Nginx as a load balancer, multiple FastAPI application replicas, and a complete monitoring stack.

* **Load Balancer:** Nginx (Round Robin strategy)
* **Application:** FastAPI (3 replicas)
* **Database:** PostgreSQL
* **Monitoring:** Prometheus, cAdvisor, and Grafana
* **Load Testing:** Locust



---

| Service | URL | Note |
| :--- | :--- | :--- |
| **Web Application** | `http://<your-ip>:80` | Use `?name=yourname` to write to DB |
| **Locust** | `http://<your-ip>:8089` | Interface for load testing |
| **Grafana** | `http://<your-ip>:3000` | Credentials: `admin` / `admin` |
| **Prometheus** | `http://<your-ip>:9090` | Metrics database |
| **cAdvisor** | `http://<your-ip>:8080` | Container resource statistics |

---

During the CI/CD implementation on AWS, several critical production issues were addressed:

### 1. Database Connectivity & Race Conditions
**Issue:** The Python application would crash if it started before PostgreSQL was ready to accept connections.
**Solution:** * Implemented `restart: always` policy in `docker-compose.yml`.
* The application container now automatically retries connection until the database is fully initialized.

### 2. Configuration Mount Errors
**Issue:** Error `not a directory` when mounting `nginx.conf` or `prometheus.yml`.
**Root Cause:** If the config file is missing on the host, Docker creates a directory with that name by default.
**Solution:** Ensure all configuration files (`nginx.conf`, `prometheus.yml`) are present in the project directory before running `docker-compose up`.

### 3. Port Conflicts
**Issue:** `Bind for 0.0.0.0:80 failed: port is already allocated`.
**Solution:** * Use `docker stop $(docker ps -aq)` to clear hanging containers.
* Disable host-level services if necessary: `sudo systemctl stop nginx`.

---

## 📈 Monitoring & Load Testing
1. **Grafana Setup:** * Add Prometheus as a Data Source: `http://prometheus:9090`.
   * Import **Dashboard ID: 14282** for container resource visualization.
2. **Locust Test:**
   * Set Host to `http://nginx`.
   * Observe how the Round Robin strategy distributes load across the 3 replicas in Grafana.

---



# Clone the specific branch
git clone -b feature/cicd [https://github.com/24024102/my-first-pipeline.git](https://github.com/24024102/my-first-pipeline.git)

# Navigate and start
cd my-first-pipeline
docker-compose up -d
