import datetime
import os


class logger:
    def __init__(self, filepath=None):
        if not filepath:
            if not os.path.isdir("".join([os.getcwd(), os.path.sep, "logs"])):
                os.mkdir("".join([os.getcwd(), os.path.sep, "logs"]))
            self.filepath = "".join(
                [
                    os.getcwd(),
                    os.path.sep,
                    "logs",
                    os.path.sep,
                    str(self._get_date()),
                    "-log-file.txt",
                ]
            )
        else:
            self.filepath = filepath

    def _get_date(self):
        return str(datetime.datetime.now().date())

    def _get_time(self):
        now = datetime.datetime.now()
        time = "[{:2d}:{:2d}:{:2d}]".format(now.hour, now.minute, now.second)
        return time

    def _err_severity(self, s):
        if s == "w" or s == "W":
            return "[WARN]"
        elif s == "e" or s == "E":
            return "[ERR]"
        elif s == "i" or s == "I":
            return "[INFO]"
        else:
            return "[LOG]"

    def start(self):
        self.file = open(self.filepath, "r+") if os.path.isfile(self.filepath) else open(self.filepath, 'w+')
        if not self.file.read():
            self.file.write(f"DATE: {self._get_date()} LOGFILE\n")
            self.file.seek(0,2)
        else:
            self.file.seek(0,2)

    def write(self, err_msg, severity="i"):
        self.file.write(
            f"{self._get_time()}: {self._err_severity(severity)} {err_msg} \n"
        )

    def stop(self):
        self.file.close()

    if __name__ == "__main__":
        print("Log directory:")
        print("".join([os.getcwd(), os.path.sep, "logs"]))
