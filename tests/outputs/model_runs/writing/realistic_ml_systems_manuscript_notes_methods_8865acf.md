Feature freshness is handled as a request-level data path rather than as a list of backend services. For each ranking request, the system takes the requested feature keys, the current local cache state, and freshness metadata as inputs. It first checks which requested keys already have usable cached values and isolates only the keys whose cached values are stale under the active freshness policy. The system then refreshes those stale entries, merges the returned values with the remaining cached values, and emits a freshness-aware feature bundle to the downstream ranker. If a refresh attempt fails, the cached value remains available for serving, while the request is annotated for later logging and analysis. This organization keeps the ranker interface stable: the ranker receives a single feature bundle whose values and freshness annotations reflect the cache check, selective refresh, merge, and fallback decisions made for that request.

Missing details / boundaries:

- No latency numbers are provided, so this paragraph does not claim overhead or SLA impact.
- No freshness-threshold formula is provided, so the threshold is described only as an active policy.
- No production incident counts are shareable, so quality drops are used only as motivation.
- Internal code module names are not exposed as paper concepts.