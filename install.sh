#!/bin/bash

# Define the folder name and permissions
folder_name="bin"
file_name="Ursa_Major_Ask"
permission="755"
requirements="requirements.txt"
repo_url="https://github.com/UCR-Research-Computing/ursa_major_ask.git"

# Clone the repository
git clone "$repo_url"

# Change directory into the cloned repository
cd ursa_major_ask

# Create the directory if it doesn't exist
mkdir -p ~/"$folder_name"

# Copy the script to the folder
cp "$file_name" ~/bin/

# Change the permissions of the script file
chmod "$permission" ~/bin/"$file_name"

# Check if the folder is already in the PATH
if [[ ":$PATH:" != *":$HOME/$folder_name:"* ]]; then
    # Add the directory to the PATH in .bashrc
    echo 'export PATH="$PATH:$HOME/'"$folder_name"'"' >> ~/.bashrc

    # Load bashrc
    source ~/.bashrc
fi

# Install requirements
pip install -r "$requirements"
