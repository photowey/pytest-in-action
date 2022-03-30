# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file encrypt_handler.py
# @description encrypt_handler
# @author WcJun
# @date 2021/07/22
# ---------------------------------------------


import os

import jpype


class EncryptHandler:

    def __init__(self):
        jar_path = os.path.abspath(os.path.join(os.getcwd(), '../../resources/encrypt/rsa-encryptor.jar'))
        # jdk version
        java_home = os.environ['JAVA_HOME']
        jpype.startJVM('{}/bin/server/jvm.dll'.format(java_home),
                       '-Djava.class.path={}'.format(jar_path), convertStrings=False)
        JClass = jpype.JClass('cn.org.opencharity.encrypt.Encryptor')
        self.instance = JClass()

    def encrypt(self, source):
        result = str(self.instance.encrypt(source))
        return result

    def decrypt(self, source):
        result = str(self.instance.decrypt(source))
        return result

    def shutdown(self):
        jpype.shutdownJVM()


if __name__ == "__main__":
    handler = EncryptHandler()
    encrypt_result = handler.encrypt('123456')
    # RQDOkImMU2vg2m9EJbaDgDzmzofpcqD2HTWl0Awlcn62czLgmJYlkPeX+v2JYn3lsPb3j5S0wAh/HSzUy3ltgtsrZtwYdvU+Mnw0XahqCZ+iXyRdWUGnT45bR3XzKxtg+vGfq2m/kLBsYt0DSZ9K5/k0owMPLauRNJFeL8xQIcwjLK/sTCtti8TFskooJ2n5i7B/KXBddzyOKTPd09lDbzErAgNuCPuo6z+R2c/FYnmnSJ6MlXrGfTP5I9c9snb8v5yttw3duhSSZGBe9zSDsvgWLEjtLlgPpZN112+2K8STOyxlg0pPKY4tv2670NmgER6hCxYfP7FGFmiUP6aSEg==
    decrypt_result = handler.decrypt(encrypt_result)
    assert decrypt_result == '123456'
    handler.shutdown()
