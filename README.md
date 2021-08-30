# Python3-Ping-Utility 
   This illustrates the use of ping command 

## [Ping]
   The ping command is a very common method for troubleshooting the accessibility of devices. It uses a series of Internet Control Message Protocol (ICMP) Echo messages to determine.
• Whether a remote host is active or inactive <br/>
• The round-trip delay in communicating with the host  <br/>
• Packet loss   <br/>
   The ping command first sends an echo request packet to an address, then waits for a reply. The ping is successful only if,
• the echo request gets to the destination, and <br/>
• the destination is able to get an echo reply back to the source within a predetermined time called a timeout. <br/>
         
      The TTL value of a ping packet cannot be changed <br/>

#### ARTICLE 

https://jadhusan-s.medium.com/testing-connectivity-on-a-network-ping-utility-6f3139f5b3c0

[![LinkedIN](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jadhusan24/)


### _TESTED WITH_
![WinVer](./Screenshots/1.JPG) ![WinVer](./Screenshots/2.JPG)

-----------------------------------
###       W I N D O W S
-----------------------------------
Excute this program using WSL
- open CMD
- navigate to  file path
- type the following command
>python ping.py www.google.com  <br/>
>python ping.py 8.8.8.8 <br/>
-----------------------------------
###         L I N U X
-----------------------------------
- open terminal
- navigate to file path
- type the following command
>sudo python3 ping.py www.google.com  <br/>
>sudo python3 ping.py 8.8.8.8 <br/>

### NOTE
- Run using **Sudo** privilege              - **LINUX**
- Run using **Administration** privilege        - **WINDOWS**
- Use **-h** for help

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

### Output

 - domain 

![result](./Screenshots/result1.jpg)

 - Ip Address

![result](./Screenshots/result2.jpg)

 - root permission

![error](./Screenshots/err.jpg)

 - Help

![help](./Screenshots/help.jpg)

