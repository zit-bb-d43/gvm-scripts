# gvm-scripts
gvm scripts to create targets and tasks for the Greenbone Vulnerability scanner (GVM) and automate tasks execution


### Usage:

```bash
# install
git clone https://github.com/zit-bb-d43/gvm-scripts.git
cd gvm-scripts
/usr/bin/python3 -m pip install --user gvm-tools
pip3 install -r requirements.txt

# read urllist
gvm-script socket create_target_and_task.gmp.py urllist

# start task
/opt/gvm/.local/bin/gvm-script socket /opt/gvm/gvm-scripts/start_task.gmp.py

```
