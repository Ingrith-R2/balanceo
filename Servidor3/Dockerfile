From python:latest
#crear un directorio de trabajo
WORKDIR /Servidor3

COPY servidor3.py .


#Intalar las dependencias
RUN pip install flask
#ejecutar la aplicacion 
CMD [ "python", "servidor3.py" ]
EXPOSE 5000