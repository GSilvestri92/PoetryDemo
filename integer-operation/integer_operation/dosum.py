import click
import mathoperator.sumoperator as op

@click.command()
@click.option('--nums',
              nargs=2,
              required=True,
              type=int,
              help='Two integer numbers to sum.')
def main(nums):
    a,b=nums
    oper=op.SumOperator()
    print(oper.operation([a,b]))


if __name__ == "__main__":
    main()