# ReunificationBot

To start app using docker, from project root, run:

```python3
docker build -t reunification:latest .
docker run -d -p 5000:5000 --env-file env_variables reunification:latest
```