import logging
import inspect
import threading

#配置日志
logging.basicConfig(level=logging.DEBUG , format="%(asctime)s.%(msecs)03d %(name)s %(levelname)-8s  %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")

def get_current_thread_id_short():
    # 获取当前线程对象
    current_thread = threading.current_thread()
    # 获取当前线程的标识符（线程 ID）并转换为字符串
    thread_id_str = str(hex(current_thread.ident))
    # 获取字符串的前几位作为线程 ID 的短表示
    thread_id_short = thread_id_str[len(thread_id_str)-8:]
    return thread_id_short


class Logger:
    def __init__(self) -> None:
        #fmt= logging.Formatter("%(asctime)s %(name)s %(levelname)-8s  %(message)s")
        fmt= logging.Formatter("%(asctime)s %(levelname)8s %(message)s")
        stream_h = logging.StreamHandler()
        stream_h.setLevel(logging.DEBUG)
        stream_h.setFormatter(fmt)
        log = logging.getLogger(__name__)
        log.addHandler(stream_h)

        file_h = logging.FileHandler("hbb.log")
        file_h.setLevel(logging.INFO)
        file_h.setFormatter(fmt)
        log.addHandler(file_h)
        log.propagate = False

        self._logger=log

    def log(self, level, message):
        frame_info = inspect.stack()[2]
        file_name = frame_info.filename
        line_number = frame_info.lineno
        tid = get_current_thread_id_short()
        msg_prefix = f"{tid} {file_name}:{line_number} "
        if(level == logging.critical):
            self._logger.critical(f"{msg_prefix}{message}",exc_info=True)
        else:
            self._logger.log(level, f"{msg_prefix}{message}")

    def debug(self, message):
        self.log(logging.DEBUG, message)

    def info(self, message):
        self.log(logging.INFO, message)

    def warning(self, message):
        self.log(logging.WARNING, message)

    def error(self, message):
        self.log(logging.ERROR, message)

    def critical(self, message):
        self.log(logging.critical,message)
