# AutoFileLog
AFL works by doing simple command, this is for doing automatic file logs, so it'll write every log on the file, if file doesnt exists, it will create a new one. But if you want to change file name, delete the old file log, you can choose format[txt, log].

# How can you code this?
simple, just do:
import (module) as (name)
(name).logger('log file info', 'log file name', 'format', 'your file name or you can use __name__(dont use strings for __name__)')
