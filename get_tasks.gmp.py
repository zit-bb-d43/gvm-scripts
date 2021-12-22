from argparse import Namespace
from gvm.protocols.gmp import Gmp
#from gvmtools.helper import Table


def main(gmp: Gmp, args: Namespace) -> None:
  tasks = gmp.get_tasks(filter_string="name~zit_ rows=-1").xpath('task')
  for task in tasks:
    print('id: '.join(task.xpath('./@id')))
    print('name: '.join(task.xpath('name/text()')))
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
    print('status: '.join(task.xpath('status/text()')))
    # alert severity_gt_5_zit id="dccd853a-998a-4612-bcf5-7f46bda08096"
    print('alert_id: '.join(task.xpath('alert/@id')))
    print('alert_name: '.join(task.xpath('alert/name/text()')))
    # report_count finished (durchgelaufene Tasks)
    print('finished_count: '.join(task.xpath('report_count/finished/text()')))
    print('last_run: '.join(task.xpath('last_report/report/scan_end/text()')))
    # max_checks and max_hosts
    print('max_checks: '.join(task.xpath('preferences/preference/scanner_name[contains(., "max_checks")]/../value/text()')))
    print('max_checks: '.join(task.xpath('preferences/preference/scanner_name[contains(., "max_hosts")]/../value/text()')))

if __name__ == '__gmp__':
    main(gmp, args)


"""
    Values der selben ebene einsammeln:
    title = root.xpath("//h1[contains(., 'SomeBeans')]")
    print("Another way to get the title is to select by element text content: '{}'".format(title[0].text.strip()))

    subtitle = root.xpath('//h1[contains(@class,"header_title")]/../h2')
    print("We can use the .. operator is select the subtitle: '{}'".format(subtitle[0].text.strip()))

    subtitle = root.xpath('//h1[contains(@class,"header_title")]/following-sibling::h2')
    print("Or we can use following-sibling to same effect: '{}'".format(subtitle[0].text.strip()))
"""
