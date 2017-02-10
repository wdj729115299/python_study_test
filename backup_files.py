import os
import time

source = ['/usr/bin', '/home']
target_dir = '/home/backup'
target = target_dir + time.strftime('%y-%m-%d-%H-%M-%S') + '.tar'
tar_command = "tar cvf '%s' %s " % (target, ' '.join(source))

if os.system(tar_command) == 0:
    print 'Successful backup to', target
else:
    print 'backup failed'


