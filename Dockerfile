# using Alpine Edge
FROM /OnLyNovaBot:latest
#
# Clone repo and prepare working directory
#
RUN git clone -b main https://github.com/OnLyNova01/OnLyNovaBot /root/userbot
RUN mkdir /root/userbot/bin/
WORKDIR /root/userbot/

# Make open port TCP
EXPOSE 80 443

CMD ["python3","-m","userbot"]
