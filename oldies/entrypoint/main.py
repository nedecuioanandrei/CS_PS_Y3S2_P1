import sys
from oldies.core.ui.main_app import OldiesApp


def main(argv=None):
    app = OldiesApp()
    app.mainloop()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
