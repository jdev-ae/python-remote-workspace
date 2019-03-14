import argparse


def csv_list(string):
    return [x.strip() for x in string.split(',') if x.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-l', '--list', required=False, type=csv_list, nargs='*')

    args = vars(ap.parse_args())

    jobs_to_update = args['list'][0] if args['list'] else None

    print(jobs_to_update)

    if args['list']:
        print(args['list'][0])
    else:
        print('nope!')


if __name__ == '__main__':
    main()
