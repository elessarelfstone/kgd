import sys
import constants as cnst


def main():
    try:
        from core import main
        exit_status = main()
        if exit_status == 2:
            print(cnst.NO_BINS)
        elif exit_status == 3:
            print(cnst.TOO_MANY_FAILS)
    except KeyboardInterrupt:
        from constants import ExitStatus
        exit_status = ExitStatus.ERROR_CTRL_C

    sys.exit(exit_status)


if __name__ == "__main__":
    main()
