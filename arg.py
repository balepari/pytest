import argparse
import os.path

def CheckExt(choices):
    class Act(argparse.Action):
        def __call__(self,parser,namespace,fname,option_string=None):
            ext = os.path.splitext(fname)[1][1:]
            if ext not in choices:
                option_string = '({})'.format(option_string) if option_string else ''
                parser.error("configfile doesn't end with one of {}{}".format(choices,option_string))
            else:
                setattr(namespace,self.dest,fname)

    return Act



parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-c', '--config', help='Load config from <configfile>', action='store_true')
parser.add_argument('configfile', help='Configuration file', type=str, action=CheckExt({'py'}))
group.add_argument('-s', '--setup', help='Generate config file', action='store_true')


args = parser.parse_args()
ext = os.path.splitext(args.configfile)[1][1:]
print('Config: ' + str(args.config))
print('Configfile: ' + args.configfile)
print('Setup: ' + str(args.setup))
print('ext: ' + ext)

