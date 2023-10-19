////////////////////////////
Requirements:
Python 3.10 or above
Follow this link if you don't have python
https://www.python.org/downloads/release/python-3105/
////////////////////////////

Install python and pip.

Test your python in cmd by typing python --version
The version should be the one you installed.

//////////////////////////
Creating environment:
Make sure your repo has the requirements.txt located in 
backend/requirements.txt

Create environment by doing
cd backend
python -m venv autobahn

start your environment by running the activate file located in either

.\autobahn\Scripts\activate
or
.\autobahn\bin\activate

You will know it is activated if the environment name now comes before the file path in cmd.
Ex: (autobahn) C:\

Once environment is started we will now install packages using requirements.txt

pip install -r requriements.txt

All Python packages we use for this project will be located here

