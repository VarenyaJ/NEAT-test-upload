import click
import os.path

# no caps

@click.command()
@click.option('--file_path', required=True, show_default=True, help='Path to reference fasta', type=click.Path(exists=True))
@click.option('--read_length', required=True, default=100, show_default=True, help='The desired read length') #try to test is < this is within a certain range (50,300)
@click.option('--output_path', default="H1N1.test-run", show_default=True, help='output_prefix')
@click.option('--bam', default=False, is_flag=True, show_default=True, help='output golden BAM file')
###
#@click.option('--n', default=1, show_default=True)
#@click.option("--gr", is_flag=True, show_default=True, default=False, help="Greet the world.")
#@click.option("--br", is_flag=True, show_default=True, default=True, help="Add a thematic break")
################################<TASK BELOW>################################
#try validating that the file directory exists (/home/suvinit)
def hello(file_path, read_length, output_path, bam):

	click.echo(f'\nHello, the input path the a reference fasta is: {file_path}' + f'\nHello, the read length is: {read_length}' + f'\nHello, the output path is: {output_path}')
	click.echo("\nCongrats Varenya! This code actually compiles!")
	click.echo("(with a --file_path followed by an actual filepath, like /home/suvinit/NEAT-data/H1N1/H1N1.fa)")

#	click.echo(f'\noutput bam test line:\n {bam}')
	###
#	if gr:
#		click.echo('Hello world!')
#		click.echo('\n')
#		click.echo('.' * n)
#	if br:
#		click.echo('\n')
#		click.echo('-' * n)
	try:
		with open('config.txt', 'w') as f:
			f.write("Created/overwrote a config file")
	except FileNotFoundError:
			print("The directory does not exist")
	print("\nHi Josh!")


if __name__ == '__main__':
	hello()
