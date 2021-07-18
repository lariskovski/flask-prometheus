# How to Setup Prometheus on K8s

## Nginx Ingress

helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
helm install ingress-nginx ingress-nginx/ingress-nginx

## Prometheus

~~~~
kubectl create namespace prometheus

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts


helm install prometheus prometheus-community/prometheus-operator --namespace prometheus

kubectl apply -f ingress.yaml
~~~~

### Access

Add the ingress load balancer to your machine's host. Then navigate to: https://prometheus.domain.com/graph

## Grafana

Get grafana user and password:

~~~~
kubectl get secret --namespace prometheus prometheus-grafana -o yaml
~~~~

Access https://grafana.domain.com

## Source

https://kubernetes.github.io/ingress-nginx/deploy/

https://www.magalix.com/blog/monitoring-of-kubernetes-cluster-through-prometheus-and-grafana
