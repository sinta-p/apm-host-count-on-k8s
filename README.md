# APM Host Count Script
## About 
Purpose of the scripts is to calculate the unique number of APM host based off outputs from kubectl commands  
![alt text](https://github.com/sinta-p/apm-host-count-on-k8s/blob/main/img/apm-host-count-architecture.png)
## How to use

1. Make use of `kubectl` commands to get a filtered list of application pods in the cluster 
2. You might only run it once or multiple time (to get 1 or multiple csv output files)
3. Run the above scripts in the same directory as the the csv file(s) to do a unique host count based on all the pods which are application-based in nature
	1. Use `simple_count_apm_host.csv` if there is only one file 
	2. Use `multifile_count_apm_host.csv` is there is more than one file
## Kubectl Cheat Sheet for Pod extraction 
```
#grep all by wide 
kubectl get pods -o wide --all-namespaces | tr -s ' ' ',' > pods.csv

# Base: get all the pod name
kubectl get pods -o custom-columns="POD:metadata.name,NODE:spec.nodeName" --all-namespaces | tr -s ' ' ',' > pods.csv

# Filter by label 
kubectl get pods \
	-l "app=adservice" \
	-o custom-columns="POD:metadata.name,NODE:spec.nodeName,APP:metadata.labels.app" --all-namespaces \
| tr -s ' ' ',' > pods.csv

# Filter by grep (eg. for image )
kubectl get pods \
	-o custom-columns="POD:metadata.name,NODE:spec.nodeName,APP:metadata.labels.app,IMAGE:spec.containers[*].image" --all-namespaces \
| grep ecr.il-central-1.amazonaws.com/tracker-app \
| tr -s ' ' ',' > pods.csv
```




