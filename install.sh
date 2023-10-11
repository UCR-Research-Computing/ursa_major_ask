#!/bin/bash

# Determine OS type and distribution
if [[ -f /etc/os-release ]]; then
    . /etc/os-release
    os_name=$NAME
else
    echo "Unsupported OS, exiting."
    exit 1
fi

# Define the folder name and permissions
folder_name="bin"
file_name="Ursa_Major_Ask"
permission="755"
requirements="requirements.txt"
repo_url="https://github.com/UCR-Research-Computing/ursa_major_ask.git"

# Create a temporary directory
temp_dir=$(mktemp -d)

# Clone the repository into the temporary directory
git clone "$repo_url" "$temp_dir"

# Change directory into the cloned repository
cd "$temp_dir"

# Create the directory if it doesn't exist
mkdir -p ~/"$folder_name"

# Copy the script and prompts.py to the folder
cp "$file_name" ~/bin/
cp "prompts.py" ~/"$folder_name"/

# Change the permissions of the script file
chmod "$permission" ~/bin/"$file_name"

# Check if config.py already exists and has an API key
config_file=~/"$folder_name"/config.py
if [[ -f $config_file ]] && grep -q 'OPENAI_API_KEY' $config_file; then
    api_key=$(grep 'OPENAI_API_KEY' $config_file | cut -d'"' -f2)
else
    # Ask the user for the OpenAI API key
    read -p "Enter your OpenAI API key (or press enter to use the default): " api_key

    # If the user didn't enter anything, use the default
    if [ -z "$api_key" ]; then
        api_key="..."
    fi
fi

# Write the API key to the config.py file
echo "OPENAI_API_KEY = \"$api_key\"" > $config_file

# Check if the folder is already in the PATH
if [[ ":$PATH:" != *":$HOME/$folder_name:"* ]]; then
    # Add the directory to the PATH in .bashrc
    echo 'export PATH="$PATH:$HOME/'"$folder_name"'"' >> ~/.bashrc

    # Load bashrc
    source ~/.bashrc
fi

# Check if pip is installed
if ! command -v pip &> /dev/null
then
    echo "pip could not be found, installing pip..."
    if [[ "$os_name" == "Ubuntu" ]] || [[ "$os_name" == "Debian GNU/Linux" ]]; then
        sudo apt-get update
        sudo apt-get install -y python3-pip
    elif [[ "$os_name" == "CentOS Linux" ]]; then
        sudo yum install -y python3-pip
    else
        echo "Unsupported OS, please install pip manually."
        exit 1
    fi
fi

# Upgrade markupsafe and jinja2
pip install --upgrade markupsafe jinja2

# Install requirements
pip install -r "$requirements"

# Remove the temporary directory
rm -rf "$temp_dir"

