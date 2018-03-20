# Задание для практического занятия по теме DNS



**Гинзбург Лиза КН-202**

2.  ​

   Работая с nslookup в режиме одного запроса, выясните адреса серверов имён (NS) для:

   -  urfu.ru

     ```
     > set type=ns
     > urfu.ru
     ╤хЁтхЁ:  UnKnown
     Address:  192.168.0.1

     Не заслуживающий доверия ответ:
     urfu.ru nameserver = ns1.urfu.ru
     urfu.ru nameserver = ns3.urfu.ru
     urfu.ru nameserver = ns2.urfu.ru

     ns1.urfu.ru     internet address = 212.193.66.21
     ns2.urfu.ru     internet address = 212.193.82.21
     ns3.urfu.ru     internet address = 212.193.72.21
     >
     ```

     ​

   - msu.ru

     ```
     > set type=ns
     > msu.ru
     ╤хЁтхЁ:  UnKnown
     Address:  192.168.0.1

     Не заслуживающий доверия ответ:
     msu.ru  nameserver = ns1.orc.ru
     msu.ru  nameserver = ns.msu.ru
     msu.ru  nameserver = ns3.nic.fr
     msu.ru  nameserver = ns.msu.net

     ns.msu.ru       internet address = 93.180.0.1
     >
     ```

   Выясните ip-адреса хостов для символьных имён

   - urfu.ru

     ```
     > nslookup urfu.ru
     ╤хЁтхЁ:  urfu.ru
     Address:  212.193.82.20
     >
     ```

     ​

   - rbc.ru

     ```
     > nslookup rbc.ru
     ╤хЁтхЁ:  rbc.ru
     Addresses:  185.72.229.9
               80.68.253.9
     >
     ```


   

   3.Перейти в режим командной строки nslookup. Выяснить имя и адрес dns-сервера, которому
      будут отправляться запросы: 

        ​```
        > set type=srv
        > msu.ru
        ╤хЁтхЁ:  A.ROOT-SERVERS.NET
        Addresses:  2001:503:ba3e::2:30
                  198.41.0.4
    
        ru      nameserver = a.dns.ripn.net
        ru      nameserver = b.dns.ripn.net
        ru      nameserver = d.dns.ripn.net
        ru      nameserver = e.dns.ripn.net
        ru      nameserver = f.dns.ripn.net
        a.dns.ripn.net  internet address = 193.232.128.6
        b.dns.ripn.net  internet address = 194.85.252.62
        d.dns.ripn.net  internet address = 194.190.124.17
        e.dns.ripn.net  internet address = 193.232.142.17
        f.dns.ripn.net  internet address = 193.232.156.17
        a.dns.ripn.net  AAAA IPv6 address = 2001:678:17:0:193:232:128:6
        b.dns.ripn.net  AAAA IPv6 address = 2001:678:16:0:194:85:252:62
        d.dns.ripn.net  AAAA IPv6 address = 2001:678:18:0:194:190:124:17
        e.dns.ripn.net  AAAA IPv6 address = 2001:678:15:0:193:232:142:17
        f.dns.ripn.net  AAAA IPv6 address = 2001:678:14:0:193:232:156:17
        >
        ​```

4. Изучить команды перехода между серверами – server, lserver и root.

   Перейти на использование сервера с адресом 194.226.235.1 (команда server), затем – с
   адресом ns1.urfu.ru.

   ```
   ​```
   > server 194.226.235.1
   ╤хЁтхЁ яю єьюыўрэш■:  [194.226.235.1]
   Address:  194.226.235.1
    
   > server ns1.urfu.ru
   DNS request timed out.
       timeout was 2 seconds.
   DNS request timed out.
       timeout was 2 seconds.
   DNS request timed out.
       timeout was 2 seconds.
   DNS request timed out.
       timeout was 2 seconds.
   *** Не найден адрес для сервера ns1.urfu.ru: Timed out
   ​```
   ```

   После того, как мы установили сервер "194.226.235.1" как сервер по умолчанию, мы не сможем установить другой сервер с помощью команды *server*, в том числе "ns1.urfu.ru" как сервер по умолчанию, поскольку мы пытаемся получить ip нового сервера у назначенного несуществующего. Но используя команду *lserver* мы увидем положительный результат - поскольку обращаемся к первоначальному серверу.

   ```
     > lserver ns1.urfu.ru
     ╤хЁтхЁ яю єьюыўрэш■:  ns1.urfu.ru
     Address:  212.193.66.21
   ```

   Снова перейти к несуществующему серверу 194.226.235.1 и затем перейти к корневому
   серверу (команда root). Обратить внимание на то, что адрес корневого сервера известен,
   несмотря на то, что он задан символьным именем.

   ```
     > server 194.226.235.1
     ╤хЁтхЁ яю єьюыўрэш■:  [194.226.235.1
     Address:  194.226.235.1
    
     > root
     ╤хЁтхЁ яю єьюыўрэш■:  A.ROOT-SERVERS.NET
     Addresses:  2001:503:ba3e::2:30
                 198.41.0.4

     >
   ```

   ​
5. Перейти в режим запроса записей NS (set q=ns или set type=ns), выяснить адреса серверов
  имён для доменов верхнего уровня (и их общее количество):

  - com (13)

    ```
    > set type=ns
    > com.
    ╤хЁтхЁ:  UnKnown
    Address:  192.168.0.1

    Не заслуживающий доверия ответ:
    com     nameserver = d.gtld-servers.net
    com     nameserver = h.gtld-servers.net
    com     nameserver = m.gtld-servers.net
    com     nameserver = f.gtld-servers.net
    com     nameserver = g.gtld-servers.net
    com     nameserver = e.gtld-servers.net
    com     nameserver = c.gtld-servers.net
    com     nameserver = k.gtld-servers.net
    com     nameserver = a.gtld-servers.net
    com     nameserver = l.gtld-servers.net
    com     nameserver = j.gtld-servers.net
    com     nameserver = b.gtld-servers.net
    com     nameserver = i.gtld-servers.net
    >
    ```

    ​

  - org  (6)

    ```
    > set type=ns
    > org.
    ╤хЁтхЁ:  UnKnown
    Address:  192.168.0.1

    Не заслуживающий доверия ответ:
    org     nameserver = a0.org.afilias-nst.info
    org     nameserver = a2.org.afilias-nst.info
    org     nameserver = b0.org.afilias-nst.org
    org     nameserver = b2.org.afilias-nst.org
    org     nameserver = c0.org.afilias-nst.info
    org     nameserver = d0.org.afilias-nst.org
    >
    ```

    ​

  - ru (5)

    ```
    > set type=ns
    > ru.
    ╤хЁтхЁ:  UnKnown
    Address:  192.168.0.1

    Не заслуживающий доверия ответ:
    ru      nameserver = f.dns.ripn.net
    ru      nameserver = d.dns.ripn.net
    ru      nameserver = a.dns.ripn.net
    ru      nameserver = b.dns.ripn.net
    ru      nameserver = e.dns.ripn.net
    >
    ```

6.Пройти по цепочке серверов имён от корня и, по необходимости меняя в запросе тип
записей (set q=…), найти ip-адрес для символьного имени и записать промежуточные
данные в виде цепочки результатов запросов

=======================================================================================

7. Изучить способы получения с сервера всех записей (команда ls). Подключиться к нужному

серверу, вывести на экран и сохранить в файл записи для:

```
> ls -d edu.ru > edu_ru.txt
[A.ROOT-SERVERS.NET]
Received 0 records.
*** Can't list domain edu.ru: BAD ERROR VALUE
DNS-сервер отклонил передачу зоны edu.ru на данный компьютер. Если это
ошибка, проверьте параметры безопасности передачи зоны для edu.ru на DNS-
сервере по IP-адресу 2001:503:ba3e::2:30.
```

Аналогично со всеми остальными серверами

8.Получить «начальную запись зоны» (SOA – start of authority), выяснить вероятную дату

​   последнего обновления зоны, время жизни записей в промежуточных кеширующих
   серверах и прочую информацию для:

  - ya.ru

    ```
    > set type=SOA
    > ya.ru
    ╤хЁтхЁ:  UnKnown
    Address:  192.168.0.1

    Не заслуживающий доверия ответ:
    ya.ru
            primary name server = ns1.yandex.ru
            responsible mail addr = sysadmin.yandex.ru
            serial  = 2018031600
            refresh = 900 (15 mins)
            retry   = 600 (10 mins)
            expire  = 2592000 (30 days)
            default TTL = 900 (15 mins)

    ya.ru   nameserver = ns2.yandex.ru
    ya.ru   nameserver = ns1.yandex.ru
    >
    ```

    ​

  - urfu.ru

    ```
    > set type=SOA
    > urfu.ru
    ╤хЁтхЁ:  UnKnown
    Address:  192.168.0.1

    Не заслуживающий доверия ответ:
    urfu.ru
            primary name server = ns1.urfu.ru
            responsible mail addr = hostmaster.urfu.ru
            serial  = 2012091861
            refresh = 3600 (1 hour)
            retry   = 1800 (30 mins)
            expire  = 2419200 (28 days)
            default TTL = 3600 (1 hour)

    urfu.ru nameserver = ns1.urfu.ru
    urfu.ru nameserver = ns2.urfu.ru
    urfu.ru nameserver = ns3.urfu.ru
    ns1.urfu.ru     internet address = 212.193.66.21
    ns2.urfu.ru     internet address = 212.193.82.21
    ns3.urfu.ru     internet address = 212.193.72.21
    >
    ```

    ​

  - mail.ru

    ```
    > set type=SOA
    > mail.ru
    ╤хЁтхЁ:  UnKnown
    Address:  192.168.0.1

    Не заслуживающий доверия ответ:
    mail.ru
            primary name server = ns1.mail.ru
            responsible mail addr = hostmaster.mail.ru
            serial  = 3312752717
            refresh = 900 (15 mins)
            retry   = 900 (15 mins)
            expire  = 604800 (7 days)
            default TTL = 60 (1 min)

    mail.ru nameserver = ns3.mail.ru
    mail.ru nameserver = ns2.mail.ru
    mail.ru nameserver = ns1.mail.ru
    ns2.mail.ru     internet address = 94.100.180.138
    ns2.mail.ru     AAAA IPv6 address = 2a00:1148:db00::1
    ns1.mail.ru     internet address = 217.69.139.112
    ns1.mail.ru     AAAA IPv6 address = 2a00:1148:db00::2
    ns3.mail.ru     internet address = 185.30.176.202
    ns3.mail.ru     AAAA IPv6 address = 2a00:1148:db00::2
    >
    ```

    ​

​	