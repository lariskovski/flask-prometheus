# How to Setup Prometheus on K8s

## Nginx Ingress

~~~~
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
helm install ingress-nginx ingress-nginx/ingress-nginx
~~~~

## Prometheus

~~~~
kubectl create ns monitoring
git clone https://github.com/prometheus-operator/kube-prometheus
# Create the namespace and CRDs, and then wait for them to be available before creating the remaining resources
kubectl create -f kube-prometheus/manifests/setup
until kubectl get servicemonitors --all-namespaces ; do date; sleep 1; echo ""; done
kubectl create -f kube-prometheus/manifests/
kubectl apply -f ingress.yaml
~~~~

## Access Prometheus & Grafana

Add to your hosts file the ingress load balancer external IP pointing to both prometheus and grafana ingresses' hosts.

~~~~
$ kubectl get svc
NAME                                 TYPE           CLUSTER-IP      EXTERNAL-IP      PORT(S)                      AGE
ingress-nginx-controller             LoadBalancer   10.108.12.210   34.122.240.113   80:31377/TCP,443:31843/TCP   34m

$ kubectl get ing -n monitoring
NAME                 CLASS    HOSTS                                      ADDRESS          PORTS     AGE
prometheus-ingress   <none>   prometheus.domain.com,grafana.domain.com   34.122.240.113   80, 443   35m
~~~~

It should look like this:

~~~~
34.122.240.113 prometheus.domain.com
34.122.240.113 grafana.domain.com
~~~~

Then, navigate to http://prometheus.domain.com or to http://grafana.domain.com.

> Grafanas login user and pass are admin.

## Source

https://kubernetes.github.io/ingress-nginx/deploy/

https://github.com/prometheus-operator/kube-prometheus
