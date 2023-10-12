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
# RUN useradd -m -d /home/eedev -s /bin/bash eedev
# # # # # # # # # RUN touch /home/eedev/.ssh/known_hosts
# # # # # # # # # # RUN ssh-keyscan github.com >> /home/eedev/.ssh/known_hosts

# # # # # # # # # # RUN git clone git@bitbucket.org:User/repo.git

# # # # # # # # # # Start the SSH server
# # # # # # # # # ENTRYPOINT touch /home/eedev/.ssh/known_hosts;ssh-keyscan github.com >> /home/eedev/.ssh/known_hosts;cd /home/eedev;git clone git@github.com:Lnola/College.git;/usr/sbin/sshd -D

# # # # # # # # # Install software 
# # # # # # # # # RUN apt-get install -y git
# # # # # # # # # Make ssh dir
RUN mkdir /root/.ssh/

# Copy over private key, and set permissions
# Warning! Anyone who gets their hands on this image will be able
# to retrieve this private key file from the corresponding image layer
ADD id_rsa /root/.ssh/id_rsa
ADD id_rsa.pub /root/.ssh/id_rsa.pub
ADD id_rsa.pub /root/.ssh/authorized_keys

# ADD id_rsa home/eedev/.ssh/id_rsa
# ADD id_rsa.pub home/eedev/.ssh/id_rsa.pub
# ADD id_rsa.pub home/eedev/.ssh/authorized_keys

# Create known_hosts
RUN touch /root/.ssh/known_hosts
RUN chmod 400 /root/.ssh/id_rsa
# Add bitbuckets key
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts
# RUN ssh-keyscan github.com >> /home/eedev/.ssh/known_hosts


# Clone the conf files into the docker container
# RUN (cd /home/eedev && git clone git@github.com:Lnola/College.git)
RUN (cd /root && git clone git@github.com:Lnola/College.git)
# RUN git config --global --add safe.directory /home/eedev/College

# Start the SSH server
CMD ["/usr/sbin/sshd", "-D"]
