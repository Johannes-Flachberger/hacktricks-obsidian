# HackTricks

![](images/hacktricks.gif)

_Hacktricks logos & motion design by_ [_@ppieranacho_](https://www.instagram.com/ppieranacho/)_._

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

Your local copy of HackTricks will be **available at [http://localhost:3337](http://localhost:3337)** after <5 minutes (it needs to build the book, be patient).

## Corporate Sponsors

### [STM Cyber](https://www.stmcyber.com)

![](images/stm (1).png)

[**STM Cyber**](https://www.stmcyber.com) is a great cybersecurity company whose slogan is **HACK THE UNHACKABLE**. They perform their own research and develop their own hacking tools to **offer several valuable cybersecurity services** like pentesting, Red teams and training.

You can check their **blog** in [**https://blog.stmcyber.com**](https://blog.stmcyber.com)

**STM Cyber** also support cybersecurity open source projects like HackTricks :)

---

### [RootedCON](https://www.rootedcon.com/)

![](images/image (45).png)

[**RootedCON**](https://www.rootedcon.com) is the most relevant cybersecurity event in **Spain** and one of the most important in **Europe**. With **the mission of promoting technical knowledge**, this congress is a boiling meeting point for technology and cybersecurity professionals in every discipline.

[[https://www.rootedcon.com/]]

---

### [Intigriti](https://www.intigriti.com)

![](images/image (47).png)

**Intigriti** is the **Europe's #1** ethical hacking and **bug bounty platform.**

**Bug bounty tip**: **sign up** for **Intigriti**, a premium **bug bounty platform created by hackers, for hackers**! Join us at [**https://go.intigriti.com/hacktricks**](https://go.intigriti.com/hacktricks) today, and start earning bounties up to **$100,000**!

[[https://go.intigriti.com/hacktricks]]

---

### [Trickest](https://trickest.com/?utm_campaign=hacktrics&utm_medium=banner&utm_source=hacktricks)

![](images/image (48).png)

\
Use [**Trickest**](https://trickest.com/?utm_campaign=hacktrics&utm_medium=banner&utm_source=hacktricks) to easily build and **automate workflows** powered by the world's **most advanced** community tools.

Get Access Today:

[[https://trickest.com/?utm_campaign=hacktrics&utm_medium=banner&utm_source=hacktricks]]

---

### [HACKENPROOF](https://bit.ly/3xrrDrL)

![](images/image (3).png)

Join [**HackenProof Discord**](https://discord.com/invite/N3FrSbmwdy) server to communicate with experienced hackers and bug bounty hunters!

- **Hacking Insights:** Engage with content that delves into the thrill and challenges of hacking
- **Real-Time Hack News:** Keep up-to-date with fast-paced hacking world through real-time news and insights
- **Latest Announcements:** Stay informed with the newest bug bounties launching and crucial platform updates

**Join us on** [**Discord**](https://discord.com/invite/N3FrSbmwdy) and start collaborating with top hackers today!

---

### [Modern Security – AI & Application Security Training Platform](https://modernsecurity.io/)

![Modern Security](images/modern_security_logo.png)

Modern Security delivers **practical AI Security training** with an **engineering-first, hands-on lab approach**. Our courses are built for security engineers, AppSec professionals, and developers who want to **build, break, and secure real AI/LLM-powered applications**.

The **AI Security Certification** focuses on real-world skills, including:
- Securing LLM and AI-powered applications  
- Threat modeling for AI systems  
- Embeddings, vector databases, and RAG security  
- LLM attacks, abuse scenarios, and practical defenses  
- Secure design patterns and deployment considerations  

All courses are **on-demand**, **lab-driven**, and designed around **real-world security tradeoffs**, not just theory.

👉 More details on the AI Security course:  
https://www.modernsecurity.io/courses/ai-security-certification

[[https://modernsecurity.io/]]

---

### [SerpApi](https://serpapi.com/)

![](images/image (1254).png)

**SerpApi** offers fast and easy real-time APIs to **access search engine results**. They scrape search engines, handle proxies, solve captchas, and parse all rich structured data for you.

A subscription to one of SerpApi’s plans includes access to over 50 different APIs for scraping different search engines, including Google, Bing, Baidu, Yahoo, Yandex, and more.\
Unlike other providers, **SerpApi doesn’t just scrape organic results**. SerpApi responses consistently include all ads, inline images and videos, knowledge graphs, and other elements and features present in the search results.

Current SerpApi customers include **Apple, Shopify, and GrubHub**.\
For more information check out their [**blog**](https://serpapi.com/blog/)**,** or try an example in their [**playground**](https://serpapi.com/playground)**.**\
You can **create a free account** [**here**](https://serpapi.com/users/sign_up)**.**

---

### [8kSec Academy – In-Depth Mobile Security Courses](https://academy.8ksec.io/)

![](images/image (2).png)

Learn the technologies and skills required to perform vulnerability research, penetration testing, and reverse engineering to protect mobile applications and devices. **Master iOS and Android security** through our on-demand courses and **get certified**:

[[https://academy.8ksec.io/]]

---

### [WebSec](https://websec.net/)

![](images/websec (1).svg)

[**WebSec**](https://websec.net) is a professional cybersecurity company based in **Amsterdam** which helps **protecting** businesses **all over the world** against the latest cybersecurity threats by providing **offensive-security services** with a **modern** approach.

WebSec is an intenational security company with offices in Amsterdam and Wyoming. They offer **all-in-one security services** which means they do it all; Pentesting, **Security** Audits, Awareness Trainings, Phishing Campagnes, Code Review, Exploit Development, Security Experts Outsourcing and much more.

Another cool thing about WebSec is that unlike the industry average WebSec is **very confident in their skills**, to such an extent that they **guarantee the best quality results**, it states on their website "**If we can't hack it, You don't pay it!**". For more info take a look at their [**website**](https://websec.net/en/) and [**blog**](https://websec.net/blog/)!

In addition to the above WebSec is also a **committed supporter of HackTricks.**

[[https://www.youtube.com/watch?v=Zq2JycGDCPM]]

---

### [CyberHelmets](https://cyberhelmets.com/courses/?ref=hacktricks)

![cyberhelmets logo](images/cyberhelmets-logo.png)

**Built for the field. Built around you.**\
[**Cyber Helmets**](https://cyberhelmets.com/?ref=hacktricks) develops and delivers effective cybersecurity training built and led by
industry experts. Their programs go beyond theory to equip teams with deep
understanding and actionable skills, using custom environments that reflect real-world
threats. For custom training inquiries, reach out to us [**here**](https://cyberhelmets.com/tailor-made-training/?ref=hacktricks).

**What sets their training apart:**
* Custom-built content and labs
* Backed by top-tier tools and platforms
* Designed and taught by practitioners

[[https://cyberhelmets.com/courses/?ref=hacktricks]]

---

### [Last Tower Solutions](https://www.lasttowersolutions.com/)

![lasttower logo](images/lasttower.png)

Last Tower Solutions delivers specialized cybersecurity services for **Education** and **FinTech**
institutions, with a focus on **penetration testing, cloud security assessments**, and
**compliance readiness** (SOC 2, PCI-DSS, NIST). Our team includes **OSCP and CISSP
certified professionals**, bringing deep technical expertise and industry-standard insight to
every engagement.

We go beyond automated scans with **manual, intelligence-driven testing** tailored to
high-stakes environments. From securing student records to protecting financial transactions,
we help organizations defend what matters most.

_“A quality defense requires knowing the offense, we provide security through understanding.”_

Stay informed and up to date with the latest in cybersecurity by visiting our [**blog**](https://www.lasttowersolutions.com/blog).

[[https://www.lasttowersolutions.com/]]

---

### [K8Studio - The Smarter GUI to Manage Kubernetes.](https://k8studio.io/)

![k8studio logo](images/k8studio.png)

K8Studio IDE empowers DevOps, DevSecOps, and developers to manage, monitor, and secure Kubernetes clusters efficiently. Leverage our AI-driven insights, advanced security framework, and intuitive CloudMaps GUI to visualize your clusters, understand their state, and act with confidence.

Moreover, K8Studio is **compatible with all major kubernetes distributions** (AWS, GCP, Azure, DO, Rancher, K3s, Openshift and more).

[[https://k8studio.io/]]

---

## License & Disclaimer

Check them in:

[[welcome/hacktricks-values-and-faq.md]]

## Github Stats

![HackTricks Github Stats](https://repobeats.axiom.co/api/embed/68f8746802bcf1c8462e889e6e9302d4384f164b.svg)

