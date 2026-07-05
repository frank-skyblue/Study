# Load Balanced App Diagram

[← Back to Diagram Index](./index.md)

Related notes: [Load Balancing](../../system-design/fundamentals/load_balancing.md), [Caching](../../system-design/fundamentals/caching.md), [Databases](../../system-design/fundamentals/databases.md)

```mermaid
flowchart TD
    Client[User Browser]
    Gateway[API Gateway / Load Balancer]
    AuthService[Auth Microservice]
    CoreApp[Core Application API]
    MainDB[(Primary MySQL DB)]
    Cache[(Redis Cache)]

    Client -->|1. HTTPS Request| Gateway
    Gateway -->|2. Validate Token| AuthService
    Gateway -->|3. Route Request| CoreApp

    CoreApp -->|4a. Cache Miss / Write| MainDB
    CoreApp -->|4b. Quick Read| Cache
```
