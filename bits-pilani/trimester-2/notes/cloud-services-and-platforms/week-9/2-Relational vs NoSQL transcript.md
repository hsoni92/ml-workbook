# Relational vs NoSQL Databases

## Relational strengths
- Structured schema with tables, rows, columns, constraints, and joins.
- ACID transactions protect correctness for multi-step business operations.
- SQL supports flexible querying and reporting.

## NoSQL strengths
- Schema flexibility and horizontal scaling for specific access patterns.
- Key-value/document models work well for sessions, profiles, events, and catalog lookups.
- Denormalization is common to avoid joins at scale.

## Exam decision rule
- Choose relational for transactions, joins, referential integrity, and complex SQL.
- Choose NoSQL for predictable key access, massive scale, low latency, and flexible schema.
- Do not choose NoSQL just because data is large; analytics may need warehouse/lake services.
