<h1>Infomania</h1>

<p>Get updates about events from various websites.</p>

<h2>Installation</h2>

```
pip install git+git://github.com/arrrlo/lsbranch@master
```

<h2>Usage</h2>

<p>Sends result to e-mail:</p>

```
> infomania "__from_email_addr__" "__to_email_addr__" "__smtp_host__" "__smtp_uname__" "__smtp__pass__" all
```

<p>or:</p>

```
> export INFOMANIA_MAIL_FROM=__from_email_addr__
> export INFOMANIA_MAIL_TO=__to_email_addr__
> export INFOMANIA_SMTP_SERVER=__smtp_host__
> export INFOMANIA_SMTP_USERNAME=__smtp_uname__
> export INFOMANIA_SMTP_PASSWORD=__smtp__pass__
>
> infomania all
```

<p>Output result to terminal:</p>

```
> infomania all
```

<p>All cli commands:</p>

```
> infomania klinfo # fetch upcomming events from www.klinfo.hr
> infomania tehnickimuzej # fetch upcomming events from www.tehnickimuzej.hr
> infomania dollarkuna # fetch dollar - kuna exchange rate from www.pbz.hr
> infomania all # fetch all of the above
```