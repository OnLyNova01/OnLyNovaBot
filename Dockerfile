# using Alpine Edge
FROM onlynova01/onlynovabot:latest

#
# Clone repo and prepare working directory
#
RUN git clone -b main https://github.com/OnLyNova01/onlynovabot /root/userbot
RUN mkdir /root/userbot/bin/
WORKDIR /root/userbot/

# Make open port TCP
EXPOSE 80 443

CMD ["python3","-m","userbot"]
