FROM registry.access.redhat.com/ubi9/python-39:1-117.1684741281

# By default, listen on port 8081
EXPOSE 8081/tcp
ENV FLASK_PORT=8081

# Update package lists
#RUN apt-get update

# Install Python 3 and pip
RUN dnf -y install python3 python3-pip

# Set the working directory in the container
WORKDIR /projects

# Copy the content of the local src directory to the working directory
COPY . .

# Install any dependencies
RUN \
  if [ -f requirements.txt ]; \
    then pip3 install -r requirements.txt; \
  elif [ `ls -1q *.txt | wc -l` == 1 ]; \
    then pip3 install -r *.txt; \
  fi

# Specify the command to run on container start
CMD [ "python3", "./app.py" ]
