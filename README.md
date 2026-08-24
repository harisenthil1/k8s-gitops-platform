# Kubernetes GitOps Platform

A lightweight Kubernetes delivery platform demonstrating GitOps deployments, CI/CD security, autoscaling, and observability.

## Stack

**Kubernetes · Helm · Argo CD · GitHub Actions · Docker · Trivy · GHCR · Prometheus · Grafana · Alertmanager**

## Architecture

```text
Git Push
   ↓
GitHub Actions
   ├─ Tests
   ├─ Docker Build
   ├─ Trivy Scan
   └─ GHCR Push
        ↓
Helm image tag updated in Git
        ↓
Argo CD
        ↓
Kubernetes Deployment
        ↓
Prometheus → Grafana
        ↓
Alertmanager
```

## Features

* Helm-based Kubernetes deployments managed by Argo CD with automated sync, self-healing, rolling updates, and Git-based rollback.
* GitHub Actions pipeline for tests, Docker builds, Trivy vulnerability scans, GHCR publishing, and GitOps deployment updates.
* Liveness/readiness probes, resource requests and limits, HPA, RBAC, ServiceAccounts, Secrets, NetworkPolicies, and non-root containers.
* Prometheus metrics for request traffic, latency, errors, pod health, CPU, and memory with Grafana visualization and Alertmanager alerts.

## Validation

Tested:

* Pod deletion and automatic recovery
* HPA scale-out under CPU load
* Rolling deployments
* Git revert rollback through Argo CD
* Prometheus application scraping
* Alert firing through Alertmanager

## Run Locally

```cmd
k3d cluster create gitops
kubectl get nodes
```

Application health:

```text
/health
/ready
/metrics
```
