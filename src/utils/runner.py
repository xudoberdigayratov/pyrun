import pwd
import subprocess
import traceback
import os
import logging


class BubbleRunner(object):
    result: str = ""
    errors: str = ""
    stats: str = ""
    cwd: str = "/home"

    def __init__(self, timeout: int = 7, bufsize: int = 1):
        self.bufsize = bufsize
        self.timeout = timeout

    @staticmethod
    def demote(user_uid, user_gid):

        def set_ids():
            os.setgid(user_gid)
            os.setuid(user_uid)

        return set_ids

    def run(self, code, inp: str = ""):
        try:
            args = ["python", "-c", code]
            username = "mistruz"
            pw_record = pwd.getpwnam(username)
            user_uid = pw_record.pw_uid
            user_gid = pw_record.pw_gid
            env = os.environ.copy()
            env.update({'HOME': self.cwd, 'LOGNAME': username, 'PWD': self.cwd, 'USER': username})
            proc = subprocess.Popen(
                args=args,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=self.cwd,
                bufsize=self.bufsize,
                preexec_fn=BubbleRunner.demote(user_uid, user_gid),
                env=env
            )
            proc.stdin.write(inp)
            try:
                self.result, self.errors = proc.communicate(timeout=self.timeout)
            except subprocess.TimeoutExpired:
                self.result, self.errors = "", "The program was stopped because it took too long"
        except PermissionError:
            self.result, self.errors = "", "An illegal command was used"
        except:
            logging.error(traceback.format_exc())
            self.errors = "Unexpected error"
        self.result = self.result or ""
        self.errors = self.errors or ""
        return {'result': self.result, 'errors': self.errors, 'stats': self.stats}


# BubbleRunner copyright by : https://github.com/JasurbekNURBOYEV/hops/blob/master/bubbler/ocean/runner.py