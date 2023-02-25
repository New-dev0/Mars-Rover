FROM python:latest

# set timezone
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt upgrade -y
RUN  apt-get install -y \
   ffmpeg \
   neofetch \ 
   mediainfo \
   p7zip-full

COPY . .

RUN python3 fetch.py

# start the bot.
CMD ["bash", "run.sh"]
