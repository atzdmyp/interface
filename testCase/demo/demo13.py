from cx_Freeze import setup, Executable

setup(name='test to exe',
      version='v1.0',
      description='test from py file to exe file',
      executables=[Executable("demo22.py")])

"""
将py文件生成可执行的.exe文件
"""