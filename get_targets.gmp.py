from argparse import Namespace
from gvm.protocols.gmp import Gmp
//from gvmtools.helper import Table


def main(gmp: Gmp, args: Namespace) -> None:
  targets = gmp.get_targets().xpath('target')
  for target in targets:
    print('id: '.join(target.xpath('./@id')))
    print('name: '.join(target.xpath('name/text()')))
    print('hosts: '.join(target.xpath('hosts/text()')))
    print('in_use: '.join(target.xpath('in_use/text()')))

if __name__ == '__gmp__':
    main(gmp, args)
