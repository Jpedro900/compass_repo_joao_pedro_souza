FROM amazonlinux:2.0.20200602.0
RUN yum update -y
RUN yum install -y \
    python3 \
    python3-pip \
    gcc \
    python3-devel \
    lapack-devel \
    blas-devel \
    atlas-devel \
    zip
RUN yum -y clean all
RUN python3.7 -m pip install --upgrade pip && \
    python3.7 -m pip install numpy