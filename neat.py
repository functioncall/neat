#!/usr/bin/env python
# coding: utf-8
from core.app_runner import app_runner as ar
from core.app.neat.neat import Neat


app_runner = ar.AppRunner(Neat())


def main():
    app_runner.run_application()


if __name__ == '__main__':
    main()
