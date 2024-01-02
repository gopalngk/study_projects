from robot import run, rebot
from robot.api import ExecutionResult, ResultVisitor

GLOBAL_NAME=globals()

def run_test():
    suite='/home/ute/gopal/sample_test/sample_robot.robot'
    output_dir='/home/ute/gopal/sample_test/robot_log/'
    output_dir1='/home/ute/gopal/sample_test/robot_log1/'
    variablefile='/home/ute/gopal/sample_test/var_file.py'
    print(GLOBAL_NAME)
    run(suite, loglevel='TRACE', consolecolors='ansi', outputdir=output_dir, variablefile=variablefile)
    print(GLOBAL_NAME)
    run(suite, loglevel='TRACE', consolecolors='ansi', include='second', outputdir=output_dir1, variablefile=variablefile)
    print(GLOBAL_NAME)


if __name__ == '__main__':
    run_test()
