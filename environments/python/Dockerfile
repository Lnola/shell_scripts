# Use an Ubuntu 20.04 base image
FROM ubuntu:20.04

# Install SSH server
RUN apt-get update && apt-get install -y openssh-server

# Create the privilege separation directory
RUN mkdir -p /run/sshd
RUN chmod 755 /run/sshd

# Install Python 3.8 and Git
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y python3.8 git
ENV DEBIAN_FRONTEND=

# Expose SSH port
EXPOSE 22

# Create a new user
RUN useradd -m -d /home/eedev -s /bin/bash eedev

# Start the SSH server
CMD ["/usr/sbin/sshd", "-D"]
