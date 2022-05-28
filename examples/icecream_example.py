from icecream import ic
import click

def func1(var1):
    ic()
    ic(var1)

def condition1(var2):
    print("We are inside condition1 function")
    if var2 > 0 :
        ic()
    else:
        ic()
        print("Its negative number")

@click.group(context_settings=dict(help_option_names=['-h', '--help']))
def ic_example():
    pass

@ic_example.command()
def ex1():
    a = 10
    ic(a)
    condition1(a)

@ic_example.command()
def enable_disable():
    a = 10
    b = -3
    func1(ic(a))
    ic.disable()
    condition1(b)
    ic.enable()
    condition1(a)

@ic_example.command()
@click.argument('status')
@option('--deafult_value', type=click.STRING, default="deafult", help='Example for string option input')
def ex3_context(status):
    ic.configureOutput(includeContext=True)
    ic.format(status)
    #print(ic.format(status))
    a = 10
    func1(a)

if __name__ == "__main__":
    ic_example()


