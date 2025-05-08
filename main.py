from stats import print_header
from stats import print_footer
from stats import sort_dict

def main():
    sorted_chars_dict = sort_dict()

    print_header()
    for char, count in sorted_chars_dict.items():
        print(f"{char}: {count}")
    print_footer()

main()