#!/bin/bash

# Install TA-Lib 
echo "installing TA-Lib"
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzvf ta-lib-0.4.0-src.tar.gz
cd ta-lib
./configure --prefix=/usr
make
make install
cd ..  # Return to project directory after TA-Lib installation


# Activate virtual environment
echo "setting up the virtual environment"
pip install virtualenv
virtualenv .venv
source .venv/bin/activate

# Installing dependencies
echo "installing dependencies"
pip install -r requirements.txt

# Start the FastAPI application
python -B -m uvicorn main:app --reload
