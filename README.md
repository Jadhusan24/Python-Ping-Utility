# Ping Utility 
  Created Ping Tool Using Python-3. Networking utility

### [What is it About?](https://en.wikipedia.org/wiki/Ping_(networking_utility))
    Ping is a computer network administration software utility used to test the 
    reachability of a host on an Internet Protocol (IP) network..

### TESTED WITH
![WinVer](./Screenshots/1.JPG) ![WinVer](./Screenshots/2.JPG)

-----------------------------------
###       W I N D O W S
-----------------------------------
Excute this program using WSL
- open WSL Terminal
- navigate to  file path
- type the following command
>python ping.py www.github.com  <br/>
>python ping.py 8.8.8.8 <br/>
-----------------------------------
###         L I N U X
-----------------------------------
- open terminal
- navigate to file path
- type the following command
>sudo python3 ping.py www.github.com  <br/>
>sudo python3 ping.py 8.8.8.8 <br/>

### NOTE
- Run using SUDO privilege              - LINUX
- Run using Administration privilege    - WINDOWS
- Use "-h" for help

| ICMP Type     | Literal                                                          |
| :------------ |:---------------------------------------------------------------: | 
| 0             | echo-reply                                                       |
| 3             | destination unreachable code 0 = net unreachable 1 = host unreachable 2 = protocol unreachable 3 = port unreachable 4 = fragmentation needed and DF set 5 = source route failed                                                                |
| 4             | source-quencht                                                   |
| 5             | redirect code 0 = redirect datagrams for the network 1 = redirect datagrams for the host 2 = redirect datagrams for the type of service and network 3 = redirect datagrams for the type of service and host                                |
| 6             | alternate-address                                                |
| 8             | echo                                                             |
| 9             | router-advertisement                                             |
| 10            | router-solicitation                                              |
| 11            | time-exceeded code 0 = time to live exceeded in transit 1 = fragment reassembly time exceeded   |
| 12            | parameter-problem                                                |
| 13            | timestamp-request                                                |
| 14            | timestamp-reply                                                  |
| 15            | information-request                                              |
| 16            | information-reply                                                |
| 17            | mask-request                                                     |
| 18            | mask-reply                                                       |
| 31            | conversion-error                                                 |
| 32            | mobile-redirect                                                  |
