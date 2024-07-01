From python:latest
#establece un directorio de trabajo rn la carpeta 
WORKDIR /Servidor1
##Copia el archivo de la aplicacion y los requisitos a
COPY  servidor1.py .


#Intalar las dependencias
RUN pip install flask
#ejecutar la aplicacion 
CMD [ "python", "servidor1.py" ]
EXPOSE 5000