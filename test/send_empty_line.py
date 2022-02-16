# SPDX-FileCopyrightText: Copyright (c) 2022 Neradoc
# SPDX-License-Identifier: MIT
#
# pylint: skip-file
"""
Test sending an empty line to a server (issue #5)
"""
import click
import socket


@click.command()
@click.argument(
    "address",
    required=True,
)
def main(address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((address, 80))
    s.send(b"\r\n")


main()
