From python:latest
#crear un directorio de trabajo
WORKDIR /Servidor2
COPY servidor2.py .


#Intalar las dependencias
RUN pip install flask
#ejecutar la aplicacion 
CMD [ "python", "servidor2.py" ]
EXPOSE 5000