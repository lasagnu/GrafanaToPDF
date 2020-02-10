#!/usr/bin/env bash
wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz                            && \
unxz wkhtmltox-0.12.4_linux-generic-amd64.tar.xz                                                                                                && \
tar -xvf wkhtmltox-0.12.4_linux-generic-amd64.tar                                                                                               && \
rm -f /wkhtmltox-0.12.4_linux-generic-amd64.tar.xz                                                                                              && \
rm -f wkhtmltox-0.12.4_linux-generic-amd64.tar                                                                                                  && \
echo "wkhtmltopdf installation finished"
