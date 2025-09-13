# HackTricks

![[images/hacktricks.gif|]]


_Hacktricks logos & motion design by_ [[https://www.instagram.com/ppieranacho/|_@ppieranacho_]]_._

### Run HackTricks Locally

```bash
# Download latest version of hacktricks
git clone https://github.com/HackTricks-wiki/hacktricks

# Select the language you want to use
export LANG="master" # Leave master for english
# "af" for Afrikaans
# "de" for German
# "el" for Greek
# "es" for Spanish
# "fr" for French
# "hi" for HindiP
# "it" for Italian
# "ja" for Japanese
# "ko" for Korean
# "pl" for Polish
# "pt" for Portuguese
# "sr" for Serbian
# "sw" for Swahili
# "tr" for Turkish
# "uk" for Ukrainian
# "zh" for Chinese

# Run the docker container indicating the path to the hacktricks folder
docker run -d --rm --platform linux/amd64 -p 3337:3000 --name hacktricks -v $(pwd)/hacktricks:/app ghcr.io/hacktricks-wiki/hacktricks-cloud/translator-image bash -c "mkdir -p ~/.ssh && ssh-keyscan -H github.com >> ~/.ssh/known_hosts && cd /app && git config --global --add safe.directory /app && git checkout $LANG && git pull && MDBOOK_PREPROCESSOR__HACKTRICKS__ENV=dev mdbook serve --hostname 0.0.0.0"
```
```
Your local copy of HackTricks will be **available at [[http://localhost:3337)** after <5 minutes (it needs to build the book, be patient|http://localhost:3337]].

## Corporate Sponsors

### [[https://www.stmcyber.com|STM Cyber]]

![[images/stm (1).png|]]


[[https://www.stmcyber.com|**STM Cyber**]] is a great cybersecurity company whose slogan is **HACK THE UNHACKABLE**. They perform their own research and develop their own hacking tools to **offer several valuable cybersecurity services** like pentesting, Red teams and training.

You can check their **blog** in [[https://blog.stmcyber.com|**https://blog.stmcyber.com**]]

**STM Cyber** also support cybersecurity open source projects like HackTricks :)

---

### [[https://www.rootedcon.com/|RootedCON]]

![[images/image (45).png|]]


[[https://www.rootedcon.com|**RootedCON**]] is the most relevant cybersecurity event in **Spain** and one of the most important in **Europe**. With **the mission of promoting technical knowledge**, this congress is a boiling meeting point for technology and cybersecurity professionals in every discipline.

[[https://www.rootedcon.com/]]

---

### [[https://www.intigriti.com|Intigriti]]

![[images/image (47).png|]]


**Intigriti** is the **Europe's #1** ethical hacking and **bug bounty platform.**

**Bug bounty tip**: **sign up** for **Intigriti**, a premium **bug bounty platform created by hackers, for hackers**! Join us at [[https://go.intigriti.com/hacktricks|**https://go.intigriti.com/hacktricks**]] today, and start earning bounties up to **$100,000**!

[[https://go.intigriti.com/hacktricks]]

---

### [[https://trickest.com/?utm_campaign=hacktrics&utm_medium=banner&utm_source=hacktricks|Trickest]]

![[images/image (48).png|]]


\
Use [[https://trickest.com/?utm_campaign=hacktrics&utm_medium=banner&utm_source=hacktricks|**Trickest**]] to easily build and **automate workflows** powered by the world's **most advanced** community tools.

Get Access Today:

[[https://trickest.com/?utm_campaign=hacktrics&utm_medium=banner&utm_source=hacktricks]]

---

### [[https://bit.ly/3xrrDrL|HACKENPROOF]]

![[images/image (3).png|]]


Join [[https://discord.com/invite/N3FrSbmwdy|**HackenProof Discord**]] server to communicate with experienced hackers and bug bounty hunters!

- **Hacking Insights:** Engage with content that delves into the thrill and challenges of hacking
- **Real-Time Hack News:** Keep up-to-date with fast-paced hacking world through real-time news and insights
- **Latest Announcements:** Stay informed with the newest bug bounties launching and crucial platform updates

**Join us on** [[https://discord.com/invite/N3FrSbmwdy|**Discord**]] and start collaborating with top hackers today!

---

### [[https://pentest-tools.com/?utm_term=jul2024&utm_medium=link&utm_source=hacktricks&utm_campaign=spons|Pentest-Tools.com]] - The essential penetration testing toolkit

![[images/pentest-tools.svg|]]


**Get a hacker's perspective on your web apps, network, and cloud**

**Find and report critical, exploitable vulnerabilities with real business impact.** Use our 20+ custom tools to map the attack surface, find security issues that let you escalate privileges, and use automated exploits to collect essential evidence, turning your hard work into persuasive reports.

[[https://pentest-tools.com/?utm_term=jul2024&utm_medium=link&utm_source=hacktricks&utm_campaign=spons]]

---

### [[https://serpapi.com/|SerpApi]]

![[images/image (1254).png|]]


**SerpApi** offers fast and easy real-time APIs to **access search engine results**. They scrape search engines, handle proxies, solve captchas, and parse all rich structured data for you.

A subscription to one of SerpApi’s plans includes access to over 50 different APIs for scraping different search engines, including Google, Bing, Baidu, Yahoo, Yandex, and more.\
Unlike other providers, **SerpApi doesn’t just scrape organic results**. SerpApi responses consistently include all ads, inline images and videos, knowledge graphs, and other elements and features present in the search results.

Current SerpApi customers include **Apple, Shopify, and GrubHub**.\
For more information check out their [[https://serpapi.com/blog/)**,** or try an example in their [**playground**](https://serpapi.com/playground|**blog**]]**.**\
You can **create a free account** [[https://serpapi.com/users/sign_up|**here**]]**.**

---

### [[https://academy.8ksec.io/|8kSec Academy – In-Depth Mobile Security Courses]]

![[images/image (2).png|]]


Learn the technologies and skills required to perform vulnerability research, penetration testing, and reverse engineering to protect mobile applications and devices. **Master iOS and Android security** through our on-demand courses and **get certified**:

[[https://academy.8ksec.io/]]

---

### [[https://websec.net/|WebSec]]

![[images/websec (1).svg|]]


[[https://websec.net|**WebSec**]] is a professional cybersecurity company based in **Amsterdam** which helps **protecting** businesses **all over the world** against the latest cybersecurity threats by providing **offensive-security services** with a **modern** approach.

WebSec is an intenational security company with offices in Amsterdam and Wyoming. They offer **all-in-one security services** which means they do it all; Pentesting, **Security** Audits, Awareness Trainings, Phishing Campagnes, Code Review, Exploit Development, Security Experts Outsourcing and much more.

Another cool thing about WebSec is that unlike the industry average WebSec is **very confident in their skills**, to such an extent that they **guarantee the best quality results**, it states on their website "**If we can't hack it, You don't pay it!**". For more info take a look at their [[https://websec.net/en/) and [**blog**](https://websec.net/blog/|**website**]]!

In addition to the above WebSec is also a **committed supporter of HackTricks.**

[[https://www.youtube.com/watch?v=Zq2JycGDCPM]]

---

### [[https://venacus.com/?utm_medium=link&utm_source=hacktricks&utm_campaign=spons|Venacus]]

![[images/venacus-logo.svg|venacus logo]]


[[https://venacus.com/?utm_medium=link&utm_source=hacktricks&utm_campaign=spons) is a data breach (leak|**Venacus**]] search engine. \
We provide random string search (like google) over all types of data leaks big and small --not only the big ones-- over data from multiple sources. \
People search, AI search, organization search, API (OpenAPI) access, theHarvester integration, all features a pentester needs.\
**HackTricks continues to be a great learning platform for us all and we're proud to be sponsoring it!**

[[https://venacus.com/?utm_medium=link&utm_source=hacktricks&utm_campaign=spons]]

---

### [[https://cyberhelmets.com/courses/?ref=hacktricks|CyberHelmets]]

![[images/cyberhelmets-logo.png|cyberhelmets logo]]



**Built for the field. Built around you.**\
[[https://cyberhelmets.com/?ref=hacktricks|**Cyber Helmets**]] develops and delivers effective cybersecurity training built and led by
industry experts. Their programs go beyond theory to equip teams with deep
understanding and actionable skills, using custom environments that reflect real-world
threats. For custom training inquiries, reach out to us [[https://cyberhelmets.com/tailor-made-training/?ref=hacktricks|**here**]].

**What sets their training apart:**
* Custom-built content and labs
* Backed by top-tier tools and platforms
* Designed and taught by practitioners

[[https://cyberhelmets.com/courses/?ref=hacktricks]]

---

### [[https://www.lasttowersolutions.com/|Last Tower Solutions]]

![[images/lasttower.png|lasttower logo]]


Last Tower Solutions delivers specialized cybersecurity services for **Education** and **FinTech**
institutions, with a focus on **penetration testing, cloud security assessments**, and
**compliance readiness** (SOC 2, PCI-DSS, NIST). Our team includes **OSCP and CISSP
certified professionals**, bringing deep technical expertise and industry-standard insight to
every engagement.

We go beyond automated scans with **manual, intelligence-driven testing** tailored to
high-stakes environments. From securing student records to protecting financial transactions,
we help organizations defend what matters most.

_“A quality defense requires knowing the offense, we provide security through understanding.”_

Stay informed and up to date with the latest in cybersecurity by visiting our [[https://www.lasttowersolutions.com/blog|**blog**]].

[[https://www.lasttowersolutions.com/]]

---

## License & Disclaimer

Check them in:

[[welcome/hacktricks-values-and-faq.md]]

## Github Stats

![[https://repobeats.axiom.co/api/embed/68f8746802bcf1c8462e889e6e9302d4384f164b.svg|HackTricks Github Stats]]


