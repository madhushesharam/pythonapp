Create an image
At your command line or shell, in the app/app.py directory, build the image with the following command:
docker build -f app/Dockerfile -t sample-python:latest .



Running in Docker in local
Run the following command to have Docker run the application in a container and map it to port 5001:

docker run -p 5001:5000 sample-python:latest
Now navigate to http://localhost:5001, and you should see the “message"


Running in Kubernetes
As we have a web application,  will create a service and a deployment to run

kubectl apply -f k8/deployment.yaml

http://localhost:8081/



Kubernetes   v1.21.2
kubectl version
Client Version: version.Info{Major:"1", Minor:"21", GitVersion:"v1.21.2", GitCommit:"092fbfbf53427de67cac1e9fa54aaa09a28371d7", GitTreeState:"clean", BuildDate:"2021-06-16T12:59:11Z", GoVersion:"go1.16.5", Compiler:"gc", Platform:"darwin/amd64"}