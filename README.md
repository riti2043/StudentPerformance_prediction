# StudentPerformance_prediction

## Software And Tools Requirements

1.[Github Account]()
2.[VS Code IDE]
3.[HerokuAccount]()
4.[GitCLI]()

Create a new environment

'''
conda create -p venv python==37 -y
'''

Activate
'''
conda activate venv/
'''

create requirement.txt with necessary libraries
'''
pip install -r requirement.txt
'''

in order to push our changes here to github repo we need to configure gitCLI
'''
git config --global user.name "  "
git config --global user.email "  " #github email id
'''
To push to repo git command 
'''
git add requirement.txt
git add. # add all files
git commit -m "commit_message" # to push from local to staging
git push origin main
'''

