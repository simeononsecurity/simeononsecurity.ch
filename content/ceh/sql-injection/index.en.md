---
title: "CEH v13: SQL Injection"
date: 2025-01-01
toc: true
draft: false
description: "Master SQL injection for the EC-Council Certified Ethical Hacker (CEH v13) exam. Learn in-band, blind, and out-of-band injection, SQLMap, authentication bypass, and parameterized query defenses."
genre: ["EC-Council CEH Course", "Ethical Hacking", "Penetration Testing", "Offensive Security", "Cybersecurity", "Network Security", "Security Testing", "Hacking Techniques", "CEH Certification", "Information Security"]
tags: ["CEH", "CEH v13", "ethical hacking", "EC-Council", "penetration testing", "sql injection", "offensive security", "cybersecurity", "hacking", "security testing"]
cover: "/img/cover/ceh-v13-sql-injection-exploitation-techniques.webp"
coverAlt: "An illustration showing a database with color-coded tables and arrows representing SQL injection attacks, set against a dark background with vibrant colors."
coverCaption: "Master SQL Injection for the CEH v13 Exam"
---

#### [Click Here to Return To the Certified Ethical Hacker (CEH v13) Course Page](/ceh-start/)

**SQL Injection** is a dedicated module in the **EC-Council CEH v13** course. This module covers injecting database commands through application input and the defenses that stop it. *Test injection only against applications inside your authorized scope.*

SQL injection happens when an application builds a database query from user input without sanitizing it. You insert SQL that the database runs as part of the query, which exposes or alters data.

## Types of SQL Injection

| Type | How you get results |
|------|---------------------|
| **In-band** | Results return in the page (UNION, error-based) |
| **Blind** | No direct output, you infer from true/false or time |
| **Out-of-band** | Data leaves through DNS or HTTP channels |

**Error-based** injection reads database errors. **UNION-based** injection appends a second query to merge attacker data into the result.

## Authentication Bypass

A login form that builds a query from input is a classic target.

```sql
-- Input that turns the WHERE clause always true
' OR '1'='1' --
```

When the application inserts this into a login query, the condition is always true and the comment sequence `--` ignores the rest, which logs you in without a valid password.

## Automating with SQLMap

You confirm and exploit injection points quickly with **SQLMap**.

```bash
# Detect injection and enumerate databases
sqlmap -u "http://target.example/item?id=1" --dbs
sqlmap -u "http://target.example/item?id=1" -D appdb --tables
```

SQLMap fingerprints the database, extracts schemas and tables, and dumps credentials when a parameter is vulnerable.

## Defenses

You stop injection at the code level.

- **Parameterized queries (prepared statements)** separate code from data.
- **Stored procedures** with bound parameters reduce risk.
- **Input validation** rejects unexpected characters.
- **Least privilege** limits what a compromised query reaches.

*Parameterized queries are the definitive fix, because the database never treats input as code.*

## Next Steps

Move off the wire and into the air with [Hacking Wireless Networks](/ceh/hacking-wireless-networks/). Revisit the broader application surface in [Hacking Web Applications](/ceh/hacking-web-applications/). Return to the [Certified Ethical Hacker (CEH v13) Course](/ceh-start/).
