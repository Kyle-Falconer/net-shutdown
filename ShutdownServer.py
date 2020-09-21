from flask import Flask
import os, errno

app = Flask(__name__)

DEBUG = False


def check_root():
    # from https://stackoverflow.com/a/2806932/940217
    try:
        os.rename('/etc/foo', '/etc/bar')
        return True
    except IOError as e:
        if e.args[0] == errno.EPERM:
            return False


def exec_shutdown():
    if check_root():
        print("sending shutdown command")
        if DEBUG:
            os.system('sudo whoami')
        else:
            os.system('shutdown now')
    else:
        print("no root permissions, trying to shutdown with \'sudo\'")
        if DEBUG:
            os.system('sudo whoami')
        else:
            os.system('shutdown now')


@app.route('/')
def listen_for_shutdown():
    print("got a request to shut down")
    exec_shutdown()
    return "ok"


if __name__ == "__main__":
    if check_root():
        print("root permissions OK")
    else:
        print("we do not have root permissions!")
    app.run()
