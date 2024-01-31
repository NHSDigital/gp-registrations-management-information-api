#!/usr/bin/env python3
"""
set_temporary_instance.py
Reads an openapi spec on stdin and changes temporary instance to true,
then prints it on stdout.
"""
import sys
import yaml


def main():
    """Main entrypoint"""
    data = yaml.safe_load(sys.stdin.read())
    data["x-nhsd-apim"]["temporary"] = True
    sys.stdout.write(yaml.dump(data, indent=2))
    sys.stdout.close()


if __name__ == "__main__":
    main()