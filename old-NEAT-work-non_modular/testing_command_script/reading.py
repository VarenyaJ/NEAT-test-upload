import /home/suvinit/NEAT/testing_command_script/test_command
#from test_command.py import file_path
#from test_command.py import read_length
#from test_command.py import output_path
#import click
#@click.command()
#@click.option('--file_path', required=True, show_default=True, help='Path to reference fasta', type=click.Path(exists=True))
#@click.option('--read_length', required=True, default=100, show_default=True, help='The desired read length') #try to test is < this is within a certain range (50,300)
#@click.option('--output_path', default="/home/suvinit/NEAT/testing_command_script/H1N1.test-run", show_default=True, help='output_prefix')
#@click.option('--bam', default=False, is_flag=True, show_default=True, help='output golden BAM file')
def HelloThereGeneralKenobi():
    try:
        #with open('config.txt', 'r') as f:
            #f.seek(0)
            '''
            print("Does this work? #1\n")
            print("The config file contains the following:\n")
            #to print out the array of all lines with brackets, use: print(f.readline())
            #to print out every line print(f.readline())
            print(f.read())
            #print()
            #f.seek(0)
            '''
            r = file_path
            R = read_length
            o = output_path
            print('the value of r is %s\n' % str(r))
            print('the value of R is %s\n' % int(R))
            print('the value of o is %s\n' % str(o))
            #

    except FileNotFoundError:
            print("There is a FileNotFoundError\n")
    print("\nHi Josh!")

if __name__ == '__main__':
	HelloThereGeneralKenobi()
