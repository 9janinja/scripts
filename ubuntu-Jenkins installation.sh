# Jenkins Installation And Setup In AWS EC2 Ubuntu Instance

# Update the repositories
sudo apt update -y

# Install Java
sudo apt install openjdk-11-jdk

# Verify Java installation
java -version

# Install Jenkins key
wget -q -O - https://pkg.jenkins.io/pubkey | sudo apt-key add -

# Add Jenkins repository
sudo sh -c 'echo deb https://pkg.jenkins.io/ubuntu-bionic binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list'

# Update package lists again
sudo apt update -y

# Install Jenkins
sudo apt install jenkins

# Start Jenkins service
sudo systemctl start jenkins

# Check Jenkins service status
systemctl status jenkins
