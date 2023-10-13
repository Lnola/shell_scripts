# Use an Ubuntu 20.04 base image
FROM ubuntu:20.04

# Install SSH server
RUN apt-get update && apt-get install -y openssh-server

# Create the privilege separation directory
RUN mkdir -p /run/sshd
RUN chmod 755 /run/sshd

# Install Python 3.8, Git, Zsh, Curl and Pip
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y python3.8 git zsh curl python3-pip
ENV DEBIAN_FRONTEND=

# Install python required libs
RUN pip install scipy
RUN pip install -U scikit-learn
RUN pip install jupyterlab

# Set Zsh as the default shell for the root user
RUN chsh -s /usr/bin/zsh root

# Install Oh My Zsh
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
# Install Powerlevel10k for Zsh
RUN git clone --depth=1 https://github.com/romkatv/powerlevel10k.git /root/.oh-my-zsh/custom/themes/powerlevel10k
# Install zsh-syntax-highlighting
RUN git clone https://github.com/zsh-users/zsh-syntax-highlighting.git /root/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
# Install zsh-autosuggestions
RUN git clone https://github.com/zsh-users/zsh-autosuggestions.git /root/.oh-my-zsh/custom/plugins/zsh-autosuggestions
# Copy the .zsh_config folder
COPY /.zsh_config /root/.zsh_config

# Add github keys
RUN mkdir /root/.ssh/
RUN touch /root/.ssh/known_hosts
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

# Start the SSH server
CMD ["/usr/sbin/sshd", "-D"]
