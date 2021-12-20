# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG OWNER=mnassrib
ARG BASE_CONTAINER=$OWNER/jupyter-pyspark
FROM $BASE_CONTAINER

LABEL maintainer="Baligh Mnassri <baligh.mnassri@gmail.com>"

USER ${NB_UID}

WORKDIR "${HOME}/work"
COPY ["notebooks/data/Online Retail.xlsx", "${HOME}/work/data/"]
COPY notebooks/test_report.ipynb .