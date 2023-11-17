from argparse import ArgumentParser
from json import loads

import httpx


BASE_URL = 'http://127.0.0.1:8000'


def main():
    parser = ArgumentParser(
        prog='client',
        description='CLI-клиент для сервиса',
        add_help=True,
    )
    parser.add_argument('--base_url', default=None, help='Базовый URL сервиса')
    subparsers = parser.add_subparsers(dest='subparser_name', required=True)

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

    # По-хорошему здесь должно быть match-case
    # Убрал, чтобы можно было тестировать на < 3.10
    if args.subparser_name == 'get':
        id_section = f'/{args.id}' if args.id else ''
        response = httpx.get(f'{base_url}/template{id_section}')
        print(f'Status code: {response.status_code} Response:')
        print(response.json())

    elif args.subparser_name == 'create':
        parsed_json = loads(args.json)
        response = httpx.post(f'{base_url}/template', json=parsed_json)
        print(f'Status code: {response.status_code} Response:')
        print(response.json())

    elif args.subparser_name == 'delete':
        response = httpx.delete(f'{base_url}/template/{args.id}')
        print(f'Status code: {response.status_code}')

    elif args.subparser_name == 'get_form':
        parsed_json = loads(args.json)
        response = httpx.post(f'{base_url}/get_form', json=parsed_json)
        print(f'Status code: {response.status_code} Response:')
        print(response.json())


if __name__ == '__main__':
    main()
