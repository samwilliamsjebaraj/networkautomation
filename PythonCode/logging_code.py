import logging
# my_file=open("my_file.txt")
logging.basicConfig(level=logging.DEBUG,
                    filename="output.log",
                    filemode="w")
logging.info("starting execution of logging code")
try:
    my_file=open("my_file.txt")
except IOError:
    logging.error("Unable to Open File, File not Found in the location specified")
except:
    logging.error("UnSpecified Error Occured, Please check the file and file path for any issues")

logging.info("execution of logging code is complete.")