FROM python:3.8

WORKDIR /converterapp

COPY ./ ./

VOLUME /tmp/.X11-unix:/tmp/.X11-unix

RUN pip install easygui
RUN pip install pyperclip
RUN pip install Pillow
RUN pip install tk


CMD ["python", "./window.py"]