# Uber's Real-Time Push Platform

[← Back to System Design Index](../../index.md)

Source: [Uber's Real-Time Push Platform](https://www.uber.com/ca/en/blog/real-time-push-platform/)

## Polling for updates

Participating entities:

- Riders
- Drivers

> These entities need to stay up-to-date with the backend systems and each other as the trip progresses

### Problems with polling from mobile apps

## Eliminating polling, introducing RAMEN

### Deciding to generate a message

### Generating the message payload

### Metadata for push message payloads

### Message Delivery

#### RAMEN delivery protocol

#### Device context storage

#### Message storage

### Implementation Details

## Scaling RAMEN globally

## The future of push infrastructure with gRPC

## Final thoughts
