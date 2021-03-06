from argparse import Namespace
from gvm.protocols.gmp import Gmp
from gvm.xml import pretty_print
#from gvmtools.helper import Table
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
  next_new_task_id = gmp.get_tasks(filter_string=(f"status=New and name~{prefix_task} rows=1")).xpath('task/@id')[0]
  print(f"starte Task {next_new_task_id}")
  gmp.start_task(next_new_task_id)
  sys.exit(0)

def start_oldest_task():
  """
  Find the autogenerated task with status »Done« that has not run for the longest time and start it.
  """
  # we use pandas for the nice dataframes and only, then we need it
  import pandas as pd
  
  done_tasks = pd.DataFrame(columns=['id','last_run'])
  
  # fill the dataframe
  for task in gmp.get_tasks(filter_string=(f"status=Done and name~{prefix_task} rows=-1")).xpath('task'):
    id = ''.join(task.xpath('./@id'))
    last_run = ''.join(task.xpath('last_report/report/scan_end/text()'))
    done_tasks = done_tasks.append({'id': id, 'last_run': last_run}, ignore_index=True)
  
  # get oldes done task and start it
  oldest_task_id = done_tasks.loc[done_tasks['last_run'] == min(done_tasks['last_run']), 'id'].values[0]
  print(f"starte Task {oldest_task_id}")
  gmp.start_task(oldest_task_id)
  sys.exit(0)
  
  
if __name__ == '__gmp__':
  # check number of args
  check_running_tasks()
  if(gmp.get_tasks(filter_string=(f"status=New and name~{prefix_task} rows=-1")).xpath('count(./task)')>0):
    start_new_task_if_exists()
  if (gmp.get_tasks(filter_string=(f"status=Done and name~{prefix_task} rows=-1")).xpath('count(./task)')>1):
    start_oldest_task()
  else:
    print("Nothing to do")
  
  sys.exit(0)
