FROM tensorflow/tensorflow:2.4.1
#RUN pip install --upgrade mkl
RUN pip install transformers==4.4.0
WORKDIR /vol