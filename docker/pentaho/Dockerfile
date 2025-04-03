FROM openjdk:8-jre-slim

RUN apt-get update && \
    apt-get install -y wget unzip python3 python3-pip && \
    apt-get clean

ENV PENTAHO_HOME=/opt/pdi
RUN mkdir -p $PENTAHO_HOME
WORKDIR $PENTAHO_HOME

RUN wget https://downloads.sourceforge.net/project/pentaho/Data%20Integration/9.4/pdi-ce-9.4.0.0-343.zip && \
    unzip pdi-ce-9.4.0.0-343.zip && \
    rm pdi-ce-9.4.0.0-343.zip

ENV PATH="${PENTAHO_HOME}/data-integration:${PATH}"

RUN mkdir -p /scripts /logs /data
WORKDIR /jobs

ENTRYPOINT ["/bin/bash"]
