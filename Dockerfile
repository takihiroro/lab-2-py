FROM mysql:8.0
EXPOSE 3306
ADD ./db_init.sql /db_init.sql
ADD ./init.sh /init.sh
RUN chmod +x /init.sh

CMD ["/init.sh"]
