FROM arm32v7/debian:buster



COPY  blink.py ./
# RUN apt-get update -o Acquire::Check-Valid-Until=false && \
#     apt-get install -y python3 python3-pip python3-rpi.gpio libgpiod2

# RUN  apt update -y && apt upgrade -y && apt-get install -y python3 python3-pip python3-rpi.gpio libgpiod2 python-pip &&\
#      pip3 install --no-cache-dir rpi.gpio 

# RUN adduser $USER gpio

# run it like this 
# sudo docker run -it --device /dev/gpiomem  docker_blinker:v1 


CMD ["python3", "./blink.py"]
