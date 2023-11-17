from argparse import ArgumentParser


BASE_URL = 'http://127.0.0.1:8000'


def main():
    parser = ArgumentParser(
        prog='client',
        description='CLI-клиент для сервиса',
        add_help=True,
    )
    parser.add_argument('--base_url', default=None, help='Базовый URL сервиса')
    subparsers = parser.add_subparsers(dest='subparser_name')

    get_parser = subparsers.add_parser('get', add_help=True)
    get_parser.add_argument('--id', required=False, default=None,
                            help='ObjectId объекта')

    create_parser = subparsers.add_parser('create', add_help=True)
    create_parser.add_argument('--json', required=True, help='Данные шаблона')

    delete_parser = subparsers.add_parser('delete', add_help=True)
    delete_parser.add_argument('--id', required=True, help='ObjectId объекта')

    get_form_parser = subparsers.add_parser('get_form', add_help=True)
    get_form_parser.add_argument('--json', required=True,
                                 help='Данные полей для запроса /get_form')

    args = parser.parse_args()
    base_url = args.base_url if args.base_url else BASE_URL

    match args.subparser_name:
        case 'get':
            ...

        case 'create':
            ...

        case 'delete':
            ...

        case 'get_from':
            ...


if __name__ == '__main__':
    main()
