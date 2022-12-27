# Neuro Medvedev tg bot

Run without Docker

Firstly you need the model itself with the following naming convention `gpt3_medium_medved_{EPOCH}.pt`
Secondly you need `TG_TOKEN` env variable, that will be sent in person.
Also, it's better to use the virtual enviromental for python:

```bash
python -m venv env
source env/bin/activate
```
As soon you have everything just run the file:

```bash 
pip install -r requirements.txt
python bot-bot.py
```


To rebuild Docker image run the following command

```bash
docker build \
-t medved \
--build-arg token=YOUR_TOKEN \
.
```

Then to run Docker container run 

```bash
docker run -dit medved 
```

or 

```bash
docker run -ti medved python 20221217_neuro_medv_bot.py
```

You can also run it directly from DockerHub

```bash 
docker pull sergeychuvakin/medved:0.1

docker run -ti sergeychuvakin/medved:0.1 python 20221217_neuro_medv_bot.py
```

To update the image on DockerHub you can use the following commands

```bash 
docker login
docker tag medved <YOUR_USERNAME/medved:<NEW_TAG>
docker push <YOUR_USERNAME/medved:<NEW_TAG>
```


Note that in case you want to build image you need to have trained model in `models` folder with the following naming convention: `gpt3_medium_medved_{EPOCH}.pt`. Since the model added to folder, you need to check 'Dockerfile' if model name comply to model in folder. 