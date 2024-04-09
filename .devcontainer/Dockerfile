# FROM cat-docker.artifacts.cat.com/cat_brazil-jfrog/dotnetcore/sdk-3.1.426-focal:1.0.0
FROM lzocateli/python:3.12.2-bookworm

# ARG PathApp=/workspaces

# RUN apt update -y \
#     && apt upgrade -y \
#     && apt install -y \
#     net-tools \
#     iputils-ping \
#     telnet 

ARG TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ >/etc/timezone
