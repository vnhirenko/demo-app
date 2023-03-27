## Build and push docker
docker login
docker build . -t vkmellon/demo_app:1.0.0
docker push vkmellon/demo_app:1.0.0

## install demo app
helm upgrade -i demo-app helm/demo-app/ -f values.yaml