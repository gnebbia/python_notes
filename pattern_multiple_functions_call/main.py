import modules


modules_list = [
        modules.google,
        modules.youtube,
        modules.linkedin,
        ]


def main():
    username = 'pippo'
    print(modules_list[0](username))
    print(modules_list[1](username))


main()
