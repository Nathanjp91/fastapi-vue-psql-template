import subprocess

# initialize git repo
subprocess.call(['git', 'init'])

# copy .env file to backend: Single source of truth
subprocess.call(['cp', '.env', 'backend/app/.env'])