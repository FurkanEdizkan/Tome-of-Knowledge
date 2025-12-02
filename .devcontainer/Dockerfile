# .devcontainer/Dockerfile
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

# Create a non-root user
ARG USERNAME=devuser
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Install basic dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    build-essential \
    ca-certificates \
    gnupg \
    lsb-release \
    software-properties-common \
    vim \
    nano \
    htop \
    btop \
    tree \
    jq \
    ripgrep \
    unzip \
    zip \
    zsh \
    && rm -rf /var/lib/apt/lists/*

# Copy installation scripts
COPY dependencies/ /tmp/dependencies/
COPY setup-user.sh /tmp/setup-user.sh

# Make scripts executable
RUN chmod +x /tmp/dependencies/*.sh \
    && chmod +x /tmp/setup-user.sh

# Install zsh
RUN /tmp/dependencies/install_zsh.sh

# Switch to non-root user for installations
USER $USERNAME
WORKDIR /home/$USERNAME

# Run user setup (installs languages, oh-my-zsh, etc.)
RUN /tmp/setup-user.sh

# Switch back to root for final setup
USER root

# Set zsh as default shell for user
RUN chsh -s /bin/zsh $USERNAME

# Configure zsh
COPY config/.zshrc /home/$USERNAME/.zshrc
COPY config/.p10k.zsh /home/$USERNAME/.p10k.zsh
RUN chown $USERNAME:$USERNAME /home/$USERNAME/.zshrc \
    && chown $USERNAME:$USERNAME /home/$USERNAME/.p10k.zsh

# Clean up
RUN rm -rf /tmp/dependencies /tmp/setup-user.sh

# Set working directory
WORKDIR /workspace
