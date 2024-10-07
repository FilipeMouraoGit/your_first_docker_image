#Sets the base image for the python 3.8.16
FROM python:3.8.16

# Copy all files to your docker image
COPY . .

# install requested libs
RUN pip3 install -r requirements.txt

# Tell your container to listen on the specified network port runtime (streamlit default)
EXPOSE 8501

# Tells docker how to check if container is still working (try to listen streamlit default port)
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run the following entry point as executable
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]