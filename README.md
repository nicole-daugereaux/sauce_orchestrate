# Simple Sauce Sauce Orchestrate Example


# Running locally for benchmark times:
While in the SauceOrchestrateDemo directory, run:

```
pip3 install -r requirements.txt
```

Run command:

```
python3 puppySearch.py
```

# To run with Sauce Orchestrate, see docs (which will tell you how to create registries, build docker images, etc) at https://docs.saucelabs.com/orchestrate/

#Or if you're on a Mac like me, follow the steps below!

1. Make sure you’re in the SauceOrchestrateDemo directory. If it’s on your Desktop, you could just do the following commands in your terminal:
```
cd desktop
cd SauceOrchestrateDemo
```

2. Make sure Docker is running by typing ```docker info``` in your terminal and hitting enter. You should get info back if it’s running; otherwise, go open it.
3. Make sure you’re in the SauceOrchestrateDemo directory. If it’s on your Desktop, you could just do the following commands in your terminal:
```
cd desktop
cd SauceOrchestrateDemo
```

4. In your terminal, type and run the following command:

```
Docker build . --platform linux/amd64
```
5. Login to hub.docker.com (or create an account if you haven’t done so already) , go to Repositories → Create Repository
 
6. Name your repository ```sauce_orchestrate``` and leave it public

7. Now rebuild your image using your account and repository name
```
docker build -t <your-docker-username>/sauce_orchestrate:latest . --platform linux/amd64
```

8. Then run the following commands to login to Docker hub and push the image up to your repo:
```
docker login
docker push <docker-username>/sauce_orchestrate:latest
```

9. While in the SauceOrchestrateDemo directory in Finder, make sure your hidden files are visible by pressing ```cmd+shift+```.   Then go into the ```.sauce``` directory and open the ```config.yml``` (this is what tells saucectl to run the image). Edit it to match your info; your Docker username should be all that's needed.

10. Type & run the command ```saucectl run ``` from the main SauceOrchestrateDemo directory that we’ve been working in & you should be good to go! 🎉
