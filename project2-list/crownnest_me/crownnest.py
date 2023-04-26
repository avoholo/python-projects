import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Program to put a or an.')
    parser.add_argument('-n', '--name', metavar='name',
                    default='John', help='Give Random Name.')
    return parser.parse_args()

def main():
    pre = 'a'
    args = get_args()
    if args.name[0] in ['a', 'e', 'i', 'o' , 'u']:
        pre = 'an'
    print(f"Ahoy, Captain, {pre} {args.name} off the larboard bow!")
    
if __name__=='__main__':
    main()