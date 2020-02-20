import re
import subprocess
import sys

def git_apply(dir, patch):
    print "patching project " + dir
    # open subprocess which stdin connected to pipe to fed up patch
    cmd = ['git','apply','--directory',dir,'-']
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    proc.stdin.write(patch)
    proc.stdin.close()
    proc.wait()

rexp = '^project\s+([^\n]+)\n' + '((?:(?!^project)[^\n]*\n)*)'
map((lambda (d, p): git_apply(d, p)), re.findall(rexp, sys.stdin.read(), re.M))
print "DONE"
