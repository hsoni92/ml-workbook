# Analytics for E-Commerce — Revision Mind Map

> One-liners for business models, data foundations, and analytics workflows (Weeks 1–8).

## Course arc

| Week | Focus |
| --- | --- |
| 1 | Models (E-com, Q-com, D2C, marketplace, subscription); digital footprint |
| 2 | EDA on e-commerce data |
| 3 | Dashboards, KPIs, funnels, quick EDA |
| 4 | Star schema, events, governance, platform models |
| 6 | Product analytics; merchandising (makeup) |
| 7 | Behavioral analytics: journeys, paths, leakage, segments |
| 8 | CRO: diagnosis, testing, abandonment, hypotheses (ICE) |

---

## Why E-Commerce Analytics

```
CONVERSION RATE = buyers / visitors × 100%
Online wins on VOLUME of visitors, not always higher % conversion than offline
DIGITAL FOOTPRINT = events + sessions + IDs → recommenders, RFM, churn
```

| vs offline | Online advantage |
| --- | --- |
| Local reach | National/global traffic |
| Fixed hours | 24×7 orders and data |
| Limited seller insight | Rich clickstream and purchase history |

**Business models**

- **E-Com** — classic online catalog (Amazon, Flipkart)
- **Q-Com** — ~10-minute delivery (Blinkit, Instamart)
- **D2C** — manufacturer → customer; owns margin + data; must acquire traffic alone
- **Marketplace** — platform commission; volume ↑ often beats margin ↓ per unit
- **Subscription** — recurring revenue (Netflix-style); retention and LTV critical

---

## Funnel and KPIs (Weeks 1–3)

- **Funnel** — step-wise drop-off (visit → cart → checkout → purchase)
- **Step conversion** — e.g. cart→checkout $= 35/55$; always compute **between steps**, not only headline %
- **Abandonment** — $1 - \text{completion rate}$; find **largest absolute drop** (not only highest %)
- **Dashboard views** — executive (sales, profit) vs ops (delivery, returns, stock) vs brand — same data, different slices
- **Cohort table** — group by sign-up month, frequency, AOV; compare bins for targeted action
- **EDA** — distributions, outliers, missing values, correlations before modelling or dashboards

---

## Data foundations (Week 4)

| Term | Role |
| --- | --- |
| **Fact** | Numeric measure (quantity, revenue, profit) — sum/average |
| **Dimension** | Who/what/where/when — filter, group-by |
| **Star schema** | Fact table + dimension tables joined on keys |
| **Event log** | One row per action (cart_added, order_placed, return_initiated) with timestamp + session/user |
| **Session** | Sequence of events tied by session ID |

**Returns** — adjust net sales via return facts; do not rewrite original order rows

**Governance (four pillars)** — data quality, access control, documentation, **consent** (especially PII)

**Platform models**

- **Monolithic** — single DB, simpler analytics
- **SaaS** (Shopify-style) — app ecosystem; export/API for warehouse
- **ONDC** — open network; fragmented sellers → need unified event model

---

## Product and merchandising (Week 6)

- **Product analytics** — views, search queries, click-through, attach rate, conversion by SKU/category
- **Search** — zero-result rate, query reformulation, top queries vs revenue
- **Placement** — homepage, category rails, cross-sell blocks; measure lift vs control
- **Portfolio** — breadth vs depth; hero SKUs vs long tail; margin-weighted assortment

---

## Behavioral analytics (Week 7)

- **Customer journey** — ordered touchpoints across channels
- **Path analysis** — common sequences (landing → PDP → cart)
- **Leakage** — where journeys end without conversion
- **Segments** — RFM, behavioural clusters, acquisition source; personalize by **person, place, product** (3 P's)

---

## Conversion rate optimization (Week 8)

$$\text{CRO loop: Diagnose → Hypothesize → Test → Learn → repeat}$$

**Four levers** — **friction** (steps, surprise fees), **trust** (reviews, returns, payments), **relevance** (right offer, season, geo), **urgency** (real stock/deadlines — fake urgency backfires)

- **Cart abandonment analysis** — step table; biggest leak; show fees early
- **Recovery email** — needs **control group** (no email) to prove lift, not only 12% of mailed carts
- **Qualitative** — heatmaps, scroll depth, session replay explain *why*
- **Hypothesis format** — problem + change + expected outcome
- **ICE scoring** — Impact × Confidence × Ease to rank test backlog
- **A/B test** — one change, fair split, predefine success metric

---

## Exam traps

- Confusing **conversion rate** with **revenue** — more visitors at low % can still beat few visitors at high %
- **Funnel** drops are not independent — fix the biggest leak first
- **Facts vs dimensions** — never sum customer names; never use product ID as a KPI without aggregation rule
- **Events vs aggregated tables** — events for behaviour; stars for reporting
- CRO without **control** — cannot claim email or UI change "worked"
