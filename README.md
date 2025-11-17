# AWS EKS Multi-Tier Application

Production-grade Kubernetes deployment on AWS EKS featuring a 3-tier architecture with Flask API, Redis caching, and Nginx frontend.

## 🏗Architecture:
Internet → AWS ALB → Frontend (Nginx) → Backend API (Flask) → Redis Cache
↓              ↓                ↓               ↓
K8s Service    K8s Service      K8s Service    K8s Pod
LoadBalancer   ClusterIP        ClusterIP      Deployment

## Components:

### Frontend (Nginx)
- **Replicas:** 2 (auto-scales 2-4 with HPA)
- **Exposure:** LoadBalancer Service (AWS ALB)
- **Features:** 
  - Modern responsive UI
  - Real-time API status monitoring
  - Visit counter with Redis persistence
  - Pod hostname display (shows load balancing)

### Backend (Flask API):
- **Replicas:** 2 (auto-scales 2-5 with HPA)
- **Endpoints:**
  - `GET /` - Service info & health
  - `GET /api/counter` - Get visit count
  - `POST /api/counter` - Increment counter
  - `GET /health` - Liveness/Readiness probe
- **Features:**
  - Redis integration
  - Health checks
  - Resource limits
  - Auto-scaling on CPU usage

### Redis Cache:
- **Replicas:** 1 (StatefulSet-ready)
- **Purpose:** Session persistence, visit counter storage
- **Exposure:** ClusterIP (internal only)

## Tech Stack:

- **Cloud:** AWS EKS (Kubernetes 1.28)
- **Container Registry:** AWS ECR
- **CI/CD:** GitHub Actions
- **Networking:** VPC, NAT Gateway, ALB
- **Languages:** Python (Flask), HTML/CSS/JS
- **Caching:** Redis
- **Web Server:** Nginx
- **Orchestration:** Kubernetes (kubectl, eksctl)

## Prerequisites:

- AWS Account with EKS permissions
- AWS CLI configured
- kubectl installed
- eksctl installed
- Docker (for local builds)


## Features Demonstrated:

✅ **EKS Cluster Management**
- Multi-node cluster with managed node groups
- VPC networking with public/private subnets
- IAM roles for service accounts

✅ **Container Orchestration**
- Multi-container application deployment
- Service discovery (ClusterIP, LoadBalancer)
- Pod-to-pod communication

✅ **Auto-Scaling**
- Horizontal Pod Autoscaler (HPA)
- CPU-based scaling policies
- Dynamic replica management

✅ **High Availability**
- Multiple replicas for each tier
- Load balancing across pods
- Health checks (liveness/readiness probes)

✅ **CI/CD Pipeline**
- GitHub Actions automation
- Automated Docker builds
- ECR image registry

✅ **Resource Management**
- CPU/Memory requests and limits
- Efficient resource allocation
- Cost optimization

## Kubernetes Resources:

| Resource | Type | Replicas | Scaling |
|----------|------|----------|---------|
| Frontend | Deployment | 2 | 2-4 (HPA) |
| Backend | Deployment | 2 | 2-5 (HPA) |
| Redis | Deployment | 1 | Fixed |
| Frontend Service | LoadBalancer | - | - |
| Backend Service | ClusterIP | - | - |
| Redis Service | ClusterIP | - | - |

## Cost Breakdown

**EKS Control Plane:** $0.10/hour = $2.40/day = $72/month  
**Worker Nodes (2x t3.small):** $0.0208/hour each = $0.998/day = ~$30/month  
**NAT Gateway:** $0.045/hour = $1.08/day = $32.40/month  
**LoadBalancer:** $0.0225/hour = $0.54/day = $16.20/month  
**Data Transfer:** Variable  

**Estimated Total:** ~$150-170/month for continuous running

## Learning Outcomes

- ✅ EKS cluster creation and management
- ✅ Kubernetes deployments, services, and scaling
- ✅ Container orchestration and networking
- ✅ Load balancing and service discovery
- ✅ Auto-scaling with HPA
- ✅ CI/CD with GitHub Actions and ECR
- ✅ Resource management and optimization
- ✅ Production-grade architecture patterns

## References

- [AWS EKS Documentation](https://docs.aws.amazon.com/eks/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [eksctl Documentation](https://eksctl.io/)
- [Docker Documentation](https://docs.docker.com/)

