# Machine Learning — Story-Based Learning

---

## K-Means: The Wedding Planner

**The story:** You're a wedding planner with **K=3 tables** to arrange. You have no idea who likes sitting with whom. So:

1. **Randomly pick 3 people** as "table captains" — they define where each table is.
2. **Everyone picks the nearest captain's table.** Groups form naturally.
3. **Each captain moves to the center of their crowd** — repositions to the mean of everyone at their table.
4. **Everyone re-checks** if their nearest table changed. Some people switch.
5. **Repeat** until nobody moves.

**Everyone is now at their most appropriate table. The 3 groups are discovered.**

| Story | K-Means Term |
|-------|------------|
| Wedding tables to arrange | **K clusters** (you pick K upfront) |
| Random captains | **Centroids initialized randomly** |
| Everyone picks nearest table | **Assign points to nearest centroid** |
| Captain moves to center of crowd | **Recalculate centroid = mean of assigned points** |
| Nobody switching anymore | **Convergence** — stable clusters found |

> **K-Means = wedding planner arranging guests into K tables by repeatedly asking "who's closest to whom" until nobody moves.**

**Key properties:**
- Hard assignments (each point belongs to exactly one cluster)
- Spherical/globular clusters only
- Sensitive to random initialization (run multiple times!)
- Converges to **local minimum**, not global

---

## DBSCAN: The Party Planner

**The story:** You're at a **house party**, observing from above. Some areas have **crowds of friends** chatting. Some people are **standing alone**. You have two dials:

- **MinNeighbours** = how many people within arm's reach to call someone "part of a group"
- **EPS (ε)** = what you consider "arm's reach" (radius)

Now walk through the party:
- Anyone with ≥ MinPts within ε → **core point** → "this is a cluster, mark everyone nearby"
- Border points (fewer than MinPts but within ε of a core) → join that cluster
- Not a core, not near any core → **noise**, left alone

**The result:** You discovered clusters **without pre-deciding how many**. Loners were automatically tagged as noise.

| Story | DBSCAN Term |
|-------|------------|
| Arm's reach radius | **ε (epsilon)** — search radius |
| Min people to form a group | **MinPts** — minimum points in ε-neighbourhood |
| Crowd area | **Dense region** → cluster |
| Person standing alone | **Noise point** |
| Edge of a crowd | **Border point** |

> **DBSCAN = party planner who says "wherever X people cluster within Y meters, that's a group — everyone else is just standing alone."**

**Key properties:**
- **No K needed** — discovers clusters automatically
- Finds **any shape** (even rings, spirals)
- Outliers → **marked as noise** automatically
- **ε and MinPts are hand-picked** — the catch

**Core / Border / Noise:**
- **Core point:** ≥ MinPts within ε → dense enough to form a cluster
- **Border point:** fewer than MinPts, but IS within ε of a core point → on the edge
- **Noise point:** not a core, not near any core → loner

**The Algorithm (3 sentences):**
1. Find all core points — every point with ≥ MinPts neighbours within ε
2. Build clusters — breadth-first from every unvisited core point: mark all ε-neighbours as in the cluster; for each that is also core, add THEIR ε-neighbours too
3. Mark leftovers — any point not reached from a core = noise

---

## K-Means vs DBSCAN

| | K-Means | DBSCAN |
|--|---------|--------|
| Clusters | You pick K upfront | Algorithm discovers them |
| Shape | Assumes spherical | Finds **any shape** |
| Outliers | Forced into nearest cluster | Marked **noise** |
| Centroids | Yes | No |
| Initialization sensitive | Yes | No (deterministic) |

DBSCAN can find a ring-shaped cluster. K-Means will always force it into overlapping spheres. That's massive.

**When to use:**
- You know number of clusters → **K-Means**
- You don't know how many / clusters are weird shapes → **DBSCAN**
- Data has clear noise/outliers → **DBSCAN**

---

## K-Means Algorithm Steps

```
1. Initialize K centroids randomly
2. Assign each point to nearest centroid (Euclidean distance)
3. Recalculate each centroid = mean of assigned points
4. Repeat step 2 & 3 until convergence (no point switches)
```

**Convergence = local minimum reached.** Since initialization is random, run K-Means multiple times and pick the run with lowest within-cluster sum of squares (WCSS).
