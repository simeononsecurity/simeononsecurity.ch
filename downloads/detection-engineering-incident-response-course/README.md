# Detection and Incident Response Sample Data

This synthetic dataset supports the SimeonOnSecurity Detection Engineering and Incident Response Course.

All names, domains, addresses, hashes, devices, and events are fictional. The IP ranges come from documentation ranges in RFC 5737. The `.test` domain is reserved for testing.

Files:

- [auth-events.jsonl](/downloads/detection-engineering-incident-response-course/auth-events.jsonl) records sign-ins, a mailbox rule, and an OAuth consent event.
- [endpoint-events.jsonl](/downloads/detection-engineering-incident-response-course/endpoint-events.jsonl) records file, process, task, and network activity.
- [dns-events.csv](/downloads/detection-engineering-incident-response-course/dns-events.csv) records DNS requests from two endpoints.
- [rule-test-events.jsonl](/downloads/detection-engineering-incident-response-course/rule-test-events.jsonl) holds five isolated process cases for Lesson 3.
- [check_rule_cases.py](/downloads/detection-engineering-incident-response-course/check_rule_cases.py) checks the three rule selections offline. It does not execute Sigma YAML or a SIEM query.

Use UTC for every timeline entry. Preserve each source event and place analyst notes in a separate file.
