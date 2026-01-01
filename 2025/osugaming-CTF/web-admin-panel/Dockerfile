FROM php:7.2-apache

COPY *.php /var/www/html/
COPY uploads /var/www/html/uploads
COPY flag.txt /flag.txt

EXPOSE 80

RUN chown -R www-data:www-data /var/www/html/uploads

CMD ["apache2-foreground"]