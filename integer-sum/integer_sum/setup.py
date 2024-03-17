import click
import mathoperator.operator as op

@click.command()
@click.option('--nums',
              nargs=2,
              required=True,
              type=int,
              help='Two integer numbers to sum.')
def main(nums):
    a,b=nums
    my_instance=op.Operator(a,b)
    print(my_instance.get_sum())


if __name__ == "__main__":
    main()