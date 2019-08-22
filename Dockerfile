FROM python:3.6.9-slim-stretch 
WORKDIR app
ADD . .  
EXPOSE 5000
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt  
CMD [ "python", "./main.py"] 
