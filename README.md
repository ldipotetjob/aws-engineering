# AWS Engineering Patterns

A curated collection of AWS architecture patterns focused on cost optimization, scalability, and real-world engineering trade-offs.

This repository targets engineers with practical AWS experience. It focuses on patterns, not step-by-step tutorials.

> 💡 The goal is to provide minimal, production-relevant patterns that highlight architectural decisions and cost trade-offs.

---

## 🧠 Philosophy

- Focus on architecture over boilerplate
- Avoid unnecessary infrastructure provisioning
- Keep examples minimal and reproducible
- Highlight cost and operational trade-offs

---

## 📦 Patterns

| Pattern | Description |
|--------|------------|
| [lambda-private-rds-cost-optimization](patterns/lambda-private-rds-cost-optimization) | Access RDS without NAT Gateway or VPC Endpoint costs |

---

## 📁 Structure

Each pattern is structured as:

- **Pattern README** → architecture, problem, and trade-offs
- **Example implementation** → runnable setup demonstrating the pattern
- **Supporting assets** → scripts, IAM policies, and configuration

---

## ⚠️ Assumptions

Examples assume:

- Existing AWS infrastructure (Lambda, VPC, RDS)
- Familiarity with AWS services such as Lambda, VPC, and IAM

---

## 📜 License

See [LICENSE](LICENSE)