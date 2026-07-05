# System Design Notes

> Template based on *System Design Interview — An Insider's Guide* by Alex Xu (Volumes 1 & 2).
> Fill in each section as you study. Delete placeholder prompts when you add your own notes.

---

## Table of Contents

### Volume 1 — Fundamentals

- [1. Scale From Zero To Millions Of Users](#1-scale-from-zero-to-millions-of-users)
- [2. Back-of-the-envelope Estimation](#2-back-of-the-envelope-estimation)
- [3. A Framework For System Design Interviews](#3-a-framework-for-system-design-interviews)

### Volume 1 — Design Problems

- [4. Design A Rate Limiter](#4-design-a-rate-limiter)
- [5. Design Consistent Hashing](#5-design-consistent-hashing)
- [6. Design A Key-value Store](#6-design-a-key-value-store)
- [7. Design A Unique ID Generator In Distributed Systems](#7-design-a-unique-id-generator-in-distributed-systems)
- [8. Design A URL Shortener](#8-design-a-url-shortener)
- [9. Design A Web Crawler](#9-design-a-web-crawler)
- [10. Design A Notification System](#10-design-a-notification-system)
- [11. Design A News Feed System](#11-design-a-news-feed-system)
- [12. Design A Chat System](#12-design-a-chat-system)
- [13. Design A Search Autocomplete System](#13-design-a-search-autocomplete-system)
- [14. Design YouTube](#14-design-youtube)
- [15. Design Google Drive](#15-design-google-drive)
- [16. The Learning Continues](#16-the-learning-continues)

### Volume 2 — Design Problems

- [1. Proximity Service](#1-proximity-service)
- [2. Nearby Friends](#2-nearby-friends)
- [3. Google Maps](#3-google-maps)
- [4. Distributed Message Queue](#4-distributed-message-queue)
- [5. Metrics Monitoring](#5-metrics-monitoring)
- [6. Ad Click Event Aggregation](#6-ad-click-event-aggregation)
- [7. Hotel Reservation](#7-hotel-reservation)
- [8. Distributed Email Service](#8-distributed-email-service)
- [9. S3-like Object Storage](#9-s3-like-object-storage)
- [10. Real-time Gaming Leaderboard](#10-real-time-gaming-leaderboard)
- [11. Payment System](#11-payment-system)
- [12. Digital Wallet](#12-digital-wallet)
- [13. Stock Exchange](#13-stock-exchange)

---

## Reusable Section Template

Use this structure for each design problem chapter:

```markdown
### Summary
<!-- One-paragraph overview of the system and key ideas -->

### Requirements
#### Functional
-

#### Non-functional
-

### Back-of-the-envelope Estimation
<!-- Traffic, storage, bandwidth, QPS -->

### High-level Design
<!-- Main components, APIs, data flow -->

### Deep Dive
<!-- Bottlenecks, scaling, trade-offs -->

### Trade-offs & Alternatives
-

### Key Takeaways
-

### Open Questions
-
```

---

## Volume 1 — Fundamentals

### 1. Scale From Zero To Millions Of Users

#### Summary

#### Key Concepts

- Single server setup
- Database separation
- Vertical vs horizontal scaling
- Load balancer
- Database replication
- Database partitioning (sharding)
- Caching
- CDN
- Stateless vs stateful architecture
- Data centers
- Message queue
- Microservices
- Auto-scaling

#### Notes

#### Key Takeaways

---

### 2. Back-of-the-envelope Estimation

#### Summary

#### Key Concepts

- Power of two
- Latency numbers every programmer should know
- Availability numbers
- Example estimations (Twitter QPS, storage, etc.)

#### Practice Estimations

| System | QPS | Storage | Bandwidth | Notes |
| ------ | --- | ------- | --------- | ----- |
|        |     |         |           |       |

#### Key Takeaways

---

### 3. A Framework For System Design Interviews

#### Summary

#### The 4-Step Process

1. **Understand the problem and establish design scope**
   - Clarifying questions
   - Assumptions
   - Requirements (functional & non-functional)

2. **Propose high-level design and get buy-in**
   - Sketch main components
   - Validate with interviewer

3. **Design deep dive**
   - Focus on critical components
   - Address bottlenecks and trade-offs

4. **Wrap up**
   - Summarize design
   - Identify remaining issues
   - Discuss monitoring, fault tolerance, etc.

#### Clarifying Questions Checklist

- [ ] Who are the users?
- [ ] What features are in scope?
- [ ] Scale (DAU, QPS, data size)?
- [ ] Latency / availability requirements?
- [ ] Consistency vs availability trade-offs?

#### Key Takeaways

---

## Volume 1 — Design Problems

### 4. Design A Rate Limiter

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 5. Design Consistent Hashing

#### Summary

#### Requirements

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 6. Design A Key-value Store

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 7. Design A Unique ID Generator In Distributed Systems

#### Summary

#### Requirements

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 8. Design A URL Shortener

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 9. Design A Web Crawler

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 10. Design A Notification System

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 11. Design A News Feed System

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 12. Design A Chat System

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 13. Design A Search Autocomplete System

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 14. Design YouTube

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 15. Design Google Drive

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 16. The Learning Continues

#### Summary

#### Follow-up Topics

-

#### Resources

-

#### Key Takeaways

---

## Volume 2 — Design Problems

### 1. Proximity Service

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 2. Nearby Friends

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 3. Google Maps

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 4. Distributed Message Queue

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 5. Metrics Monitoring

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 6. Ad Click Event Aggregation

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 7. Hotel Reservation

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 8. Distributed Email Service

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 9. S3-like Object Storage

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 10. Real-time Gaming Leaderboard

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 11. Payment System

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 12. Digital Wallet

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---

### 13. Stock Exchange

#### Summary

#### Requirements

#### Back-of-the-envelope Estimation

#### High-level Design

#### Deep Dive

#### Trade-offs & Alternatives

#### Key Takeaways

---
