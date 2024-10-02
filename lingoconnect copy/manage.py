import os
import sys
import threading

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

venv_site_packages = os.path.join(os.path.dirname(__file__), 'venv', 'lib', 'python3.11', 'site-packages')
if venv_site_packages not in sys.path:
    sys.path.insert(0, venv_site_packages)

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lingoconnect.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        
    #Increase recursion limit
    threading.stack_size(2 * 1024 * 1024)
    sys.setrecursionlimit(1500)
    
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
