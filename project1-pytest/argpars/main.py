import hello

def main():
    args = hello.get_args()
    print('Hello, ' + args.name + '!')

if __name__=='__main__':
    main()
