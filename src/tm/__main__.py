from tm.main import get_parser, add_arguments, handle_default_options

if __name__ == "__main__":
    parser = get_parser()
    parser = add_arguments(parser)
    options = parser.parse_args()
    handle_default_options(options)
