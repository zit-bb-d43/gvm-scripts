from argparse import Namespace
from gvm.protocols.gmp import Gmp
//from gvmtools.helper import Table


def main(gmp: Gmp, args: Namespace) -> None:
  targets = gmp.get_tasks().xpath('target')
  for task in tasks:
    print('id: '.join(task.xpath('./@id')))
    print('name: '.join(task.xpath('name/text()')))
    print('hosts: '.join(task.xpath('hosts/text()')))
    print('in_use: '.join(task.xpath('in_use/text()')))
    #config id (full and fast ...)  id="daba56c8-73ec-11df-a475-002264764cea">
    print('config_id: '.join(task.xpath('config/@id')))
    print('config_name: '.join(task.xpath('config/name/text()')))
    # target_id
    print('target_id: '.join(task.xpath('target/@id')))
    print('target_name: '.join(task.xpath('target/name/text()')))
    # scanner id (ZIT OpenVAS Scanner, ...)  id="27ebc4c1-62ab-43f2-8f25-a0bddc41811b"
    print('scanner_id: '.join(task.xpath('scanner/@id')))
    print('scanner_name: '.join(task.xpath('scanner/name/text()')))
    # status (running, done, ...)
    print('status: '.join(task.xpath('status/text()'))))
    # alert severity_gt_5_zit id="dccd853a-998a-4612-bcf5-7f46bda08096"
    print('alert_id: '.join(task.xpath(alert/@id)))
    print('alert_name: '.join(task.xpath('alert/name/text()')))
    # report_count finished (durchgelaufene Tasks)
    print('finished_count: '.join(task.xpath('report_count/finished/text()')))
    print('last_run: '.join(task.xpath('/last_report/report/scan_end/text()')))

if __name__ == '__gmp__':
    main(gmp, args)


"""
 wenn wir in running tasks die Werte für max_hosts und max_checks raus kriegen, könnten wir unsere Checks intelligenter starten
 <preferences>
      <preference>
        <name>Maximum concurrently executed NVTs per host</name>
        <scanner_name>max_checks</scanner_name>
        <value>2</value>
      </preference>
      <preference>
        <name>Maximum concurrently scanned hosts</name>
        <scanner_name>max_hosts</scanner_name>
        <value>1</value>
      </preference>
"""
