# iButton

## Intro

iButton is a generic name for an electronic identification key packed in a **coin-shaped metal container**. It is also called **Dallas Touch** Memory or contact memory. Even though it is often wrongly referred to as a “magnetic” key, there is **nothing magnetic** in it. In fact, a full-fledged **microchip** operating on a digital protocol is hidden inside.

![](../../images/image (915).png)

### What is iButton? 

Usually, iButton implies the physical form of the key and reader - a round coin with two contacts. For the frame surrounding it, there are lots of variations from the most common plastic holder with a hole to rings, pendants, etc.

![](../../images/image (1078).png)

When the key reaches the reader, the **contacts come to touch** and the key is powered to **transmit** its ID. Sometimes the key is **not read** immediately because the **contact PSD of an intercom is larger** than it should be. So the outer contours of the key and the reader couldn't touch. If that's the case, you'll have to press the key over one of the walls of the reader.

![](../../images/image (290).png)

### **1-Wire protocol** 

Dallas keys exchange data using the 1-wire protocol. With only one contact for data transfer (!!) in both directions, from master to slave and vice versa. The 1-wire protocol works according to the Master-Slave model. In this topology, the Master always initiates communication and the Slave follows its instructions.

When the key (Slave) contacts the intercom (Master), the chip inside the key turns on, powered by the intercom, and the key is initialized. Following that the intercom requests the key ID. Next, we will look up this process in more detail.

Flipper can work both in Master and Slave modes. In the key reading mode, Flipper acts as a reader this is to say it works as a Master. And in the key emulation mode, the flipper pretends to be a key, it is in the Slave mode.

### Dallas, Cyfral & Metakom keys

For information about how these keys works check the page [https://blog.flipperzero.one/taming-ibutton/](https://blog.flipperzero.one/taming-ibutton/)

### Attacks

iButtons can be attacked with Flipper Zero:

[[flipper-zero/fz-ibutton.md]]

## References

- [https://blog.flipperzero.one/taming-ibutton/](https://blog.flipperzero.one/taming-ibutton/)

