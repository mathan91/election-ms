#! /bin/bash

echo "Deleting all pods in dashboard-cluster"
kubectl config set-context  --current --namespace=dashboard-cluster
kubectl delete all
kubectl delete ns dashboard-cluster