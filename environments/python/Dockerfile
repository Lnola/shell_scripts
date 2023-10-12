# Use an Ubuntu 20.04 base image
FROM ubuntu:20.04

# Install SSH server
RUN apt-get update && apt-get install -y openssh-server

# Create the privilege separation directory
RUN mkdir -p /run/sshd
RUN chmod 755 /run/sshd

# Install Python 3.8
RUN apt-get update && apt-get install -y python3.8

# Expose SSH port
EXPOSE 22

# Create a new user (replace 'eedev' with your desired username)
ARG SSH_PUBLIC_KEY
RUN useradd -m -d /home/eedev -s /bin/bash eedev

# Copy the SSH public key into the container
RUN mkdir /home/eedev/.ssh
RUN echo "$SSH_PUBLIC_KEY" > /home/eedev/.ssh/authorized_keys
RUN chown -R eedev:eedev /home/eedev/.ssh
RUN chmod 700 /home/eedev/.ssh
RUN chmod 600 /home/eedev/.ssh/authorized_keys

# Start the SSH server
CMD ["/usr/sbin/sshd", "-D"]
