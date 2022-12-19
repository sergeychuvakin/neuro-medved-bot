# Neuro Medvedev tg bot

To rebuild Docker image run the following command

```bash
docker build \
-t medved \
--build-arg token=YOUR_TOKEN \
.
```

Then to run docker container run 

```bash
docker run -dit medved 
```

Note that in case you want to build image you need to have trained model in `models` folder with the following naming convention: `gpt3_medium_medved_{EPOCH}.pt`. Since the model added to folder, you need to check 'Dockerfile' if model name comply to model in folder. 