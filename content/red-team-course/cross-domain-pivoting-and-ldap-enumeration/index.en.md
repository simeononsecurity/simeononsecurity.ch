---
title: "Module 18: Cross-Domain Pivoting and LDAP Enumeration"
date: 2026-09-12
toc: true
draft: false
description: "Query Active Directory quietly with ldapsearch, map trust relationships, and pivot across domains with a fully specified distinguished name."
genre: ["Red Team", "Offensive Security", "Active Directory", "LDAP"]
tags: ["red team", "ldapsearch", "LDAP", "trusts", "trustdirection", "flatname", "cross-domain", "red team course"]
cover: "/img/cover/ldap-enumeration-cross-domain-pivoting-illustration.webp"
coverAlt: "A digital illustration showing a computer interface with flowing data streams and network nodes. The design features vibrant colors against a dark background, representing Active Directory enumeration and cross-domain queries."
coverCaption: "Module 18: read the directory and follow the trust out."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**ldapsearch is how you enumerate Active Directory objects from inside Beacon memory, with nothing on disk and no collector process.** Active Directory willingly answers questions about users, groups, computers, and trusts, and this tool asks quietly.

*This module takes about 16 minutes.*

> **Why it matters:** Active Directory answers whatever you ask. Name the distinguished name, and the directory becomes your map across trusts.

______

## Key Terms

| Term | Plain meaning |
|------|---------------|
| **ldapsearch** | the in-memory BOF querying Active Directory |
| **Filter** | the parenthesized condition selecting objects |
| **Trust** | a relationship letting one domain authenticate to another |
| **`trustdirection`** | the integer naming which way auth flows |
| **Distinguished name** | the `DC=` path to a domain |
______

## The Basic Query

```text
ldapsearch "(objectclass=user)" --attributes * --count 2
```

Three pieces do the work:

- `(objectclass=user)` is the filter, always in parentheses.
- `--attributes *` names the fields to return. `*` means all of them.
- `--count 2` caps the result at two objects.

Leaving off `--attributes` defaults to every attribute, and leaving off `--count` means no limit. A lazy query dumps every attribute of hundreds of objects down your C2 channel.

______

## Combining Filters

```text
ldapsearch "(&(objectclass=user)(name=*smith*))" --attributes * --count 2
```

The `&` means both conditions must hold. The `*` inside a value is a wildcard, so `*smith*` matches anything with `smith` in the name.

______

## The --attributes Discipline

Specify the fields you want:

```text
ldapsearch "(objectclass=user)" --attributes name,samaccountname,description
```

To learn what fields exist, pull one full record first, then query for real with those names:

```text
ldapsearch "(objectclass=user)" --attributes * --count 1
```

______

## Enumerate Trusts

A trust is a configured relationship which lets principals in one domain authenticate into another. Query them:

```text
ldapsearch "(objectclass=trusteddomain)" --attributes flatname,trustdirection
```

- `flatname` is the short NetBIOS name of the remote domain.
- `trustdirection` tells you which way authentication flows, always relative to your domain:

| Value | Meaning |
|-------|---------|
| `1` | you have access to their domain |
| `2` | they have access to your domain |
| `3` | both directions trusted |

A `1` or `3` is a live path out. A `2` is worth noting for the report, not your immediate exit.

______

## Pivot Across the Trust

Point `ldapsearch` at the remote domain with `--dn`:

```text
ldapsearch "(objectclass=user)" --attributes * --count 2 --dn DC=child,DC=corp,DC=local
```

Format the distinguished name as one `DC=` per label. `child.corp.local` becomes `DC=child,DC=corp,DC=local`.

______

## Always Name the DN

You query as whatever token you hold. If you do not specify `--dn`, ldapsearch tries to infer the server from your current token, and the resolution breaks under pass-the-hash or `steal_token`. Name the DN every time. Do not let the tool guess.

______

## Object Classes to Know

| Object class | Useful attributes |
|--------------|-------------------|
| `computer` | `description`, `samaccountname`, `operatingsystem`, `dnshostname` |
| `user` | `description`, `samaccountname`, `name` |
| `trusteddomain` | `flatname`, `trustdirection` |
| `group` | `description`, `samaccountname`, `name`, `member` |
| SID lookups | `objectSID` |

> **Operator takeaway:** enumerate trusts, act on any `1` or `3`, and re-run ldapsearch against the remote domain with a fully specified `--dn`. Name the DN every time, because letting the tool infer it from your token is where cross-domain queries silently break.

______

## Follow the Trust

Map a domain trust and pivot across it:

1. Which object class do you query for trusts?
2. What two attributes tell you the remote name and direction?
3. Which direction values are your exit path?
4. How do you point the next query at the remote domain?

Answer from memory first. The explanations are in the Answer Key at the end.
______

## Why Trust Enumeration Matters

A trust is a relationship, not automatic permission. LDAP reveals names, groups, and trust direction, while access still depends on SID filtering, selective authentication, and delegated rights. A two-domain lab with synthetic groups makes the difference visible. **Query only the directory objects listed in the scope.**

______

## Common Mistakes

- Querying without `--attributes` and flooding your callback.
- Omitting `--dn` and letting ldapsearch infer the server from your token.
- Reading a trustdirection `2` as your exit when it points the wrong way.
- Treating a lazy wildcard query as free when it returns a wall of data.

______

## Self-Check

1. What are the three parts of an ldapsearch query?
2. What does the `&` operator do?
3. What does `trustdirection` value `1` mean?
4. How do you format a distinguished name for a child domain?

______

## Answer Key

**Self-Check**

1. **Filter, `--attributes`, and `--count`.** The parenthesized filter, the fields returned, and the result cap.
2. **It requires both conditions.** The `&` wraps two filters so both must match.
3. **You have access to their domain.** The remote domain trusts you.
4. **One `DC=` per label.** `child.corp.local` becomes `DC=child,DC=corp,DC=local`.

**Exercise**

1. **`(objectclass=trusteddomain)`.** The class holding trust objects.
2. **`flatname` and `trustdirection`.** The short name and the direction.
3. **`1` or `3`.** A path into the remote domain.
4. **`--dn`** with the remote domain's distinguished name.
______

## Next Steps

You have mapped the trusts and pivoted across. Next, spread quiet, redundant access so no single discovery ends the operation.

**[→ Module 19: Fortifying Access and Operator Discipline](/red-team-course/fortifying-access-and-operator-discipline/)**

Or return to the hub: **[Red Team Course](/red-team-course-start/)**
