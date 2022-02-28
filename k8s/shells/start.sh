#! /bin/bash

echo Checking if dashboard-cluster exist
array=($(kubectl get namespaces))
namespaceExist=false;
for namespace in array
do
    if [[ namespace == "dashboard-cluster" ]]
        then
            namespaceExist=true
    fi
done
if [[ namespaceExist == "false" ]]
    then
        kubectl create namespace "dashboard-cluster" 
fi
echo Setting namespace to dashboard-cluster
kubectl config set-context  --current --namespace=dashboard-cluster