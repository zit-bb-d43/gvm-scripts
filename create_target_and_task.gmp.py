from argparse import Namespace
from gvm.protocols.gmp import Gmp
from gvmtools.helper import Table


def main(gmp: Gmp, args: Namespace) -> None:
  response_xml = gmp.get_targets()
  #tasks_xml = response_xml.xpath('task')

  #for task in tasks_xml:
  #  name = ''.join(task.xpath('name/text()'))
  #  task_id = task.get('id')
  #  severity = ''.join(task.xpath('last_report/report/severity/text()'))

  print(response_xml)


if __name__ == '__gmp__':
    main(gmp, args)
