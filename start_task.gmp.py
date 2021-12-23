from argparse import Namespace
from gvm.protocols.gmp import Gmp
from gvm.xml import pretty_print
#from gvmtools.helper import Table
# we use pandas for the nice dataframes
import pandas as pd
import sys

# vars
prefix_task = "@@@_"

def check_running_tasks():
  """
  checks for running or requested tasks. If there is any, exit
  """
  running_tasks = gmp.get_tasks(filter_string="status=Running rows=-1").xpath('count(./task)')
  requested_tasks = gmp.get_tasks(filter_string="status=Requested rows=-1").xpath('count(./task)')
  if(running_tasks>0 or requested_tasks>0):
    print("there are running tasks. Exit")
    sys.exit(0)

def start_new_task_if_exists():
  """
  if there is a new autgenerated task, start it
  """
  count_new_tasks = gmp.get_tasks(filter_string=(f"status=New and name~{prefix_task} rows=-1")).xpath('count(./task)')
  if(count_new_tasks>0):
    next_new_task_id = gmp.get_tasks(filter_string=(f"status=New and name~{prefix_task} rows=1")).xpath('task/@id')[0]
    print(f"starte Task {next_new_task_id}")
    gmp.start_task(next_new_task_id)
    sys.exit(0)



if __name__ == '__gmp__':
  # check number of args
  check_running_tasks()
  start_new_task_if_exists()
  sys.exit(0)
