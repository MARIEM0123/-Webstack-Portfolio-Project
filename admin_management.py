#!/usr/bin/env python
"""Django's command-line to access to the applicatoion for administration management"""
import os
import sys


def main():
    """Run administrative tasks from gjango framework"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elearning.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Make sure to INSALL Django on your computer "
            "Make sure of having a work environment on your computer "
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
