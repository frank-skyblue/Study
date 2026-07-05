# Databases

[← Back to System Design Index](../index.md)

Database choices shape consistency, query flexibility, operational complexity, and scaling strategy.

Related notes: [Caching](./caching.md), [Load Balancing](./load_balancing.md), [URL Shortener](../case-studies/url_shortener.md), [Instagram](../case-studies/instagram.md)

## SQL vs NoSQL

| Choice | Strengths | Trade-Offs |
| --- | --- | --- |
| Relational / SQL | Strong consistency, joins, transactions, mature tooling. | Horizontal scaling can be harder. |
| Key-value | Very fast lookups by key. | Limited query flexibility. |
| Document | Flexible schema, nested data. | Consistency and joins vary by system. |
| Wide-column | High write throughput and large scale. | Data model must match query patterns. |
| Graph | Relationship-heavy queries. | Specialized operational model. |

## Core Concepts

- **Indexing:** speeds reads by maintaining extra lookup structures.
- **Replication:** copies data to improve read scale and availability.
- **Sharding:** partitions data across nodes to increase write/storage capacity.
- **Transactions:** group operations with atomicity and consistency guarantees.
- **Consistency models:** define what reads can observe after writes.

## Scaling Patterns

| Pattern | Helps With | Watch For |
| --- | --- | --- |
| Read replicas | Read-heavy workloads. | Replica lag. |
| Partitioning / sharding | Write throughput and storage growth. | Hot shards and cross-shard queries. |
| Denormalization | Query speed. | Duplicate data and harder updates. |
| CQRS | Different read/write access patterns. | More moving parts and eventual consistency. |

## Design Checklist

- What are the main access patterns?
- Which fields need indexes?
- What consistency does each workflow require?
- How large will the data get?
- What is the backup and restore strategy?

## Key Takeaways

- Start with the query patterns before picking the database.
- Indexes speed reads but slow writes and consume storage.
- Replication improves availability, while sharding increases capacity.
